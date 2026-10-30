#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 29 22:00:21 2025

@author: jadamalone
"""

# Author: Jada Malone
# Description: Contains solutions for tasks B-1, B-2, and B-3 as per assignment instructions.

# -----------------------------------
# B-1: Employee Bonus Calculation
# -----------------------------------

# Create a list to store employee data
employee_data = []

while True:
    # Prompt user for employee name
    name = input("Enter employee's name (or 'done' to finish): ")
    if name.lower() == 'done':
        break  # Exit the loop if user types 'done'
    
    # Prompt user for monthly sales and convert to float
    sales_input = input(f"Enter monthly sales for {name}: $")
    try:
        sales = float(sales_input.replace(',', ''))  # Remove commas for safety
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
        continue

    # Calculate bonus based on sales ranges
    if sales < 10000:
        bonus = "No Bonus"
    elif 10000 <= sales <= 20000:
        bonus = f"${sales * 0.05:.2f}"
    else:
        bonus = f"${sales * 0.10:.2f}"

    # Store the data as a tuple in the list
    employee_data.append((name, sales, bonus))

# Print results in table format
print("\nEmployee Data:")
print(f"{'Name':<10} {'Monthly Sales':<15} {'Bonus'}")
print("-" * 40)
for name, sales, bonus in employee_data:
    sales_formatted = f"${sales:,.2f}"
    print(f"{name:<10} {sales_formatted:<15} {bonus}")

# -----------------------------------
# B-2: Tuition Projection for 5 Years (Corrected)
# -----------------------------------

# Base tuition before increase
base_tuition = 25000.00
increase_rate = 0.03
total_cost = 0.0

print("\nYear  Projected Tuition (per Year)")
print("-----------------------------------")

# Loop to calculate projected tuition for next 5 years
tuition = base_tuition
for year in range(1, 6):
    # Apply increase before printing year 1
    tuition *= (1 + increase_rate)

    # Display tuition for the year
    print(f"{year:<6} ${tuition:,.2f}")

    # Add to total cost
    total_cost += tuition

# Print total tuition cost after 5 years
print(f"\nTotal tuition cost after five years: ${total_cost:,.2f}")


# -----------------------------------
# B-3: SAC Aggregation with Titanic Data (Full Output)
# -----------------------------------

import pandas as pd

# Step 1: Load the Titanic dataset
df = pd.read_csv('titanic.csv')

# Step 2: Create a new 'class' column by mapping Pclass numbers to names
df['class'] = df['Pclass'].map({1: 'First', 2: 'Second', 3: 'Third'})

# Step 3: Generate a Series of unique class labels
class_series = pd.Series(df['class'].unique(), name='class')

# Step 4: Create a Boolean Series for Second and Third classes
mask = class_series.isin(['Second', 'Third'])

# Step 5: Set index to class names to match desired output format
mask.index = class_series

# Define all possible classes in order
ordered_classes = ['First', 'Second', 'Third']

# Create a Boolean Series using isin(), then align with ordered index
mask = pd.Series(ordered_classes, name='class').isin(['Second', 'Third'])
mask.index = ordered_classes

# Step 6: Display mask
print("class")
print(mask)

# Step 7: Filter Second class passengers and show specific columns
second_class = df[df['class'] == 'Second']
print("\n", second_class[['Age', 'Sex', 'class', 'Fare', 'Survived']].head())

# Step 8: Filter Third class passengers and show specific columns
third_class = df[df['class'] == 'Third']
print("\n", third_class[['Age', 'Sex', 'class', 'Fare', 'Survived']].head())
