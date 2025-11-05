# Fuzzy Logic System (Mamdani Inference)

This project implements a **fuzzy logic system** using the **Mamdani method**.  
It takes *temperature* and *humidity* as inputs and determines an *output intensity level* — e.g. fan speed, cooling power, etc.

---

## Overview

- Reads fuzzy rules from a CSV file  
- Uses **Triangular Fuzzy Numbers (TFN)** for membership functions  
- Dynamically aggregates fuzzy rules  
- Visualizes results using Matplotlib  

---

## Example Rule Base (CSV)

```csv
Temperature/Humidity;Low;High
Low;Low;Low
Medium;Medium;Medium
High;High;High
