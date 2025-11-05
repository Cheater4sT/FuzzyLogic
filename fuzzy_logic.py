import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Get rules from CSV
df = pd.read_csv('data/FuzzyLogic.csv', sep=';')
rules=[]
for _, row in df.iterrows():
    temp = row['Temperature/Humidity']
    for hum, speed in row.items():
        if hum == 'Temperature/Humidity':
            continue
        rules.append((temp, hum, speed))

# Triangular Fuzzy Number class
class TFN:
    """Triangular Fuzzy Number"""
    def __init__(self, a, m, b):
        self.a = a
        self.m = m
        self.b = b

    def mu(self, x):
        mu = 0
        if x <= self.a:
            mu = 0
        elif self.a <= x <= self.m:
            mu = (x - self.a) / (self.m - self.a)
        elif self.m <= x <= self.b:
            mu = (self.b - x) / (self.b - self.m)
        elif x >= self.b:
            mu = 0

        return mu

# Fuzzy sets definitions
temp_dict = {'Low':TFN(15,20,25), 'Medium':TFN(20,25,30), 'High':TFN(25,30,35)}
hum_dict = {'Low':TFN(0,20,40), 'High': TFN(30,50,70)}
speed_dict = {'Low':TFN(0,25,50), 'Medium': TFN(25,50,75), 'High': TFN(50,75,100)}

# Input Values
t, h = 27, 49
x = np.linspace(0,100, 500)

# Rule evaluation
rule_act={}
for rule in rules:
    y=[]
    tfn_and = min(temp_dict[rule[0]].mu(t), hum_dict[rule[1]].mu(h))
    if tfn_and !=0:
        tfn = speed_dict[rule[2]]
        for num in x:
            y.append(min(tfn.mu(num),tfn_and))
        rule_act[rule[2]] = np.asarray(y)

# Aggregation & defuzzification
output = np.maximum.reduce(list(rule_act.values())) if rule_act else np.zeros_like(x)
defuzzified = np.sum(output * x) / np.sum(output) if np.sum(output) != 0 else 0

# Visualization
for key in speed_dict:
    plt.plot(x, [speed_dict[key].mu(num) for num in x], linestyle='--', label=f'{key.capitalize()} TFN')

plt.axvline(defuzzified, color='purple', label=f'Deffuzified y*={defuzzified:.2f}')
plt.plot(x,output, color='black', label='Aggregated output')
plt.ylim(bottom=0)
plt.grid(linewidth=0.5, linestyle='--', zorder=0)
plt.legend()

plt.savefig('results.png')
plt.show()