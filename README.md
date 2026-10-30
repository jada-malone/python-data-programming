# Python Programming for Data Analysis

**Python · pandas · NumPy · Matplotlib · SciPy · Turtle** · Texas A&M University and Texas Tech University coursework (2024–2025)

## Overview
A collection of my Python work, from first programs to data analysis: loading and summarizing real datasets with pandas, grouped aggregations, exploratory analysis of the Titanic and restaurant-tips datasets, charts with Matplotlib, and object-oriented programs with classes and inheritance.

## Data analysis scripts (`scripts/data-analysis/`, summer 2025)
| Script | What it does | Data |
|---|---|---|
| [`Assign1_Malone.py`](scripts/data-analysis/Assign1_Malone.py) | Stock sale calculator: two sales of 200 shares, profit and 15% capital-gains tax | user input |
| [`Assign2_Malone.py`](scripts/data-analysis/Assign2_Malone.py) | Social-media engagement tracker using nested dictionaries (Instagram, Twitter, Facebook) | in-script |
| [`Assign3_Malone.py`](scripts/data-analysis/Assign3_Malone.py) | Retail sales summary with pandas: total sales by department, average by region, max by product | [`retail_sales.csv`](data/retail_sales.csv) |
| [`Assign4_Malone.py`](scripts/data-analysis/Assign4_Malone.py) | Grouped totals and averages with reusable functions, plus Matplotlib charts | [`salesdata.csv`](data/salesdata.csv) |
| [`T1_B_Malone.py`](scripts/data-analysis/T1_B_Malone.py) | Employee bonus calculator with input validation, and Titanic dataset analysis | [`titanic.csv`](data/titanic.csv) |
| [`T2_B_Malone.py`](scripts/data-analysis/T2_B_Malone.py) | pandas DataFrames built and sorted from dictionaries; statistics and charts on restaurant tips (SciPy, Matplotlib) | [`tips.csv`](data/tips.csv) |
| [`empMalone.py`](scripts/data-analysis/empMalone.py) + [`Assign5_Malone.py`](scripts/data-analysis/Assign5_Malone.py) | OOP: `Employee` base class and `ProductionWorker` subclass (inheritance, getters/setters) | user input |
| [`retail_Malone.py`](scripts/data-analysis/retail_Malone.py) + [`RDemo_Malone.py`](scripts/data-analysis/RDemo_Malone.py) | OOP: `RetailItem` class with accessor and mutator methods, demoed with three products | in-script |

## Python fundamentals (`scripts/fundamentals/`, Texas A&M)
Earlier programs from my introductory programming course: classes (`Customer`, `Item`, `EggTimer`), string and file processing (letter counts, vowel counts, letter-position frequency across a five-letter-word list, palindrome checker, NBA champions lookup from a text file), logic and math (leap years, a four-digit number that reverses when multiplied by 4, simple interest, temperature conversion), and Turtle graphics (shapes, colorful patterns, spirals).

## Repo structure
```
scripts/data-analysis/   pandas, Matplotlib and OOP scripts
scripts/fundamentals/    introductory Python programs and their small text inputs
data/                    public/sample datasets the scripts read (Titanic, tips, sales)
```

## How to run
```bash
pip install pandas numpy matplotlib scipy
cd data && python ../scripts/data-analysis/Assign3_Malone.py   # scripts read their CSV from the working directory
```
Several scripts are interactive and ask for input in the terminal.

_Housekeeping note: a few fundamentals files were saved from the Python shell with `>>>` prompts; those prompts were removed so the files run as normal scripts. The code itself is unchanged._

## Skills demonstrated
Python · pandas data wrangling and group-bys · exploratory data analysis · Matplotlib visualization · functions and input validation · object-oriented programming (classes, inheritance) · file I/O

---
**Jada Malone** · Data Analyst · M.S. Data Science, Texas Tech University · [GitHub profile](https://github.com/jada-malone) · [LinkedIn](https://www.linkedin.com/in/jada-malone-509170280)
