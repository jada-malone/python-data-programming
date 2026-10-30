#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 24 01:06:06 2025

@author: jadamalone
"""

import pandas as pd

def compute_sales_summary(df):
    """Returns total sales by department, average sales by region, and max sales by product"""
    total_sales_by_department = df.groupby('Department')['SalesAmount'].sum()
    average_sales_by_region = df.groupby('Region')['SalesAmount'].mean()
    max_sales_by_product = df.groupby('Product')['SalesAmount'].max()
    return total_sales_by_department, average_sales_by_region, max_sales_by_product

def compute_hierarchical_groupings(df):
    """Returns total sales by region+department and region+store"""
    sales_by_region_department = df.groupby(['Region', 'Department'])['SalesAmount'].sum()
    sales_by_region_store = df.groupby(['Region', 'StoreID'])['SalesAmount'].sum()
    return sales_by_region_department, sales_by_region_store

def evaluate_regional_performance(df, threshold=50000):
    total_sales_by_region = df.groupby('Region')['SalesAmount'].sum().sort_values(ascending=False)
    high_performers = total_sales_by_region[total_sales_by_region > threshold]
    return total_sales_by_region, high_performers


def main():
    # Load data
    try:
        df = pd.read_csv("retail_sales.csv")
    except FileNotFoundError:
        print("Error: 'retail_sales.csv' not found in the current directory.")
        return

    # 1. Sales Summary
    print("\n===== Sales Summary =====")
    dept_sales, region_avg, product_max = compute_sales_summary(df)
    print("\nTotal Sales by Department:")
    print(dept_sales)

    print("\nAverage Sales by Region:")
    print(region_avg)

    print("\nMaximum Sales by Product:")
    print(product_max)

    # 2. Hierarchical Grouping
    print("\n===== Hierarchical Grouping =====")
    region_dept_sales, region_store_sales = compute_hierarchical_groupings(df)
    print("\nSales by Region and Department:")
    print(region_dept_sales)

    print("\nSales by Region and StoreID:")
    print(region_store_sales)

    # 3. Regional Performance Evaluation
    print("\n===== Regional Performance Evaluation =====")
    total_region_sales, high_performance = evaluate_regional_performance(df)

    print("\nTotal Sales by Region, sorted in descending order:")
    print(total_region_sales)
    
    print("\nRegions with Total Sales above $50000:")
    print(high_performance)
    print("\n")
    
    for region, sales in total_region_sales.items():
        print(f"{region} is below target with ${sales:,.2f} in sales.")


if __name__ == "__main__":
    main()
