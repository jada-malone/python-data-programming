#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 31 22:01:00 2025

@author: jadamalone
"""

import pandas as pd
import matplotlib.pyplot as plt

def grouped_summary(df, group_col, agg_col):
    """Calculate total and average values grouped by a specific column."""
    total = df.groupby(group_col)[agg_col].sum().reset_index()
    average = df.groupby(group_col)[agg_col].mean().reset_index()
    return total, average

def plot_grouped_data(total_df, avg_df, group_col, agg_col):
    """Generate bar chart for total and line chart for average values."""
    # Bar chart
    plt.figure(figsize=(10, 4))
    plt.bar(total_df[group_col], total_df[agg_col], color='skyblue')
    plt.title(f"Total {agg_col} by {group_col}")
    plt.xlabel(group_col)
    plt.ylabel(f"Total {agg_col}")
    plt.xticks(rotation=45)
    plt.grid(True, axis='y')
    plt.tight_layout()
    plt.show()

    # Line chart
    plt.figure(figsize=(10, 4))
    plt.plot(avg_df[group_col], avg_df[agg_col], marker='o', color='green')
    plt.title(f"Average {agg_col} by {group_col}")
    plt.xlabel(group_col)
    plt.ylabel(f"Average {agg_col}")
    plt.xticks(rotation=45)
    plt.grid(True, axis='y')
    plt.tight_layout()
    plt.show()

def main():
    # Load the dataset
    data = pd.read_csv("salesdata.csv")

    # Display available columns
    print("Available columns:", data.columns.tolist())

    # User selects columns
    group_col = input("Enter the column to group by (e.g., 'Region'): ")
    agg_col = input("Enter the numeric column to aggregate (e.g., 'Quantity'): ")

    # Validate input
    if group_col not in data.columns or agg_col not in data.columns:
        print("Invalid column names provided. Please try again.")
        return

    # Grouped data
    total_df, avg_df = grouped_summary(data, group_col, agg_col)

    # Visualizations
    plot_grouped_data(total_df, avg_df, group_col, agg_col)

    # Summary
    max_total = total_df.loc[total_df[agg_col].idxmax()]
    max_avg = avg_df.loc[avg_df[agg_col].idxmax()]

    print("\n----- Summary -----")
    print(f"{max_total[group_col]} has the highest total {agg_col}: {max_total[agg_col]:,.2f}")
    print(f"{max_avg[group_col]} has the highest average {agg_col}: {max_avg[agg_col]:,.2f}")

if __name__ == "__main__":
    main()
