#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 19 22:18:45 2025

@author: jadamalone
"""

# Assign2_LASTNAME.py

# Initial engagement data using a nested dictionary
engagement_data = {
    'Instagram': {'likes': 250, 'comments': 65},
    'Twitter': {'likes': 300, 'comments': 75},
    'Facebook': {'likes': 200, 'comments': 85}
}

# Function to calculate total engagement for each platform
def calculate_total_engagement(data):
    total_engagement = {}
    for platform, metrics in data.items():
        total = metrics['likes'] + metrics['comments']
        total_engagement[platform] = total
    return total_engagement

# Function to identify the platform with the highest engagement
def find_top_platform(totals):
    top_platform = max(totals, key=totals.get)
    return top_platform, totals[top_platform]

# Function to display the engagement in a readable format
def display_engagement(totals, label=""):
    print(f"{label} {totals}")

# Initial total engagement display
totals = calculate_total_engagement(engagement_data)
display_engagement(totals, "Total engagement for each platform:")
top_platform, top_value = find_top_platform(totals)
print("Platform with the highest engagement: {} ({} interactions)".format(top_platform, top_value))

# Simulate 3 hours of engagement growth
hour = 1
while hour <= 3:
    print(f"\nHour {hour}: Monitoring social media engagement.")
    for platform in engagement_data:
        engagement_data[platform]['likes'] *= 1.05
        engagement_data[platform]['comments'] *= 1.05
        # Convert to int for simplicity and clean display
        engagement_data[platform]['likes'] = int(engagement_data[platform]['likes'])
        engagement_data[platform]['comments'] = int(engagement_data[platform]['comments'])
    
    updated_totals = calculate_total_engagement(engagement_data)
    print(f"Updated total engagement for each platform after {hour} hour(s): {updated_totals}")
    hour += 1

# Final metrics
print("\nMonitoring period has ended. Final engagement metrics:", calculate_total_engagement(engagement_data))
