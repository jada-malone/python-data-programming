#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  8 22:32:11 2025

@author: jadamalone
"""


# This program creates three RetailItem objects and prints their details
# using the getter (accessor) methods.

from retail_Malone import RetailItem  # Import your class from Step 1

def main():
    # Create the three RetailItem objects
    prod1 = RetailItem("Jacket", 12, 249.99)
    prod2 = RetailItem("Designer Jeans", 30, 199.99)
    prod3 = RetailItem("Shirt", 45, 49.99)

    # Display the details for each product using getter methods
    print("Product 1:")
    print(f"Description: {prod1.get_description()}")
    print(f"Units in inventory: {prod1.get_units()}")
    print(f"Price: ${prod1.get_price():.2f}\n")

    print("Product 2:")
    print(f"Description: {prod2.get_description()}")
    print(f"Units in inventory: {prod2.get_units()}")
    print(f"Price: ${prod2.get_price():.2f}\n")

    print("Product 3:")
    print(f"Description: {prod3.get_description()}")
    print(f"Units in inventory: {prod3.get_units()}")
    print(f"Price: ${prod3.get_price():.2f}")

if __name__ == "__main__":
    main()
