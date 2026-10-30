#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  5 00:00:35 2025

@author: jadamalone
"""


from empMalone import ProductionWorker

def main():
    # Get input from user
    name = input("Enter your name: ")
    id_number = input("Enter your ID number: ")
    shift = int(input("Enter the shift number: "))
    hourly_rate = float(input("Enter your hourly rate: "))

    # Create ProductionWorker instance
    worker = ProductionWorker(name, id_number, shift, hourly_rate)

    # Display information
    print("\nProduction Worker Information:")
    print("Name: ", worker.get_name())
    print("ID number: ", worker.get_id_number())
    print("Shift:", worker.get_shift())
    print("Hourly Pay Rate: ${:,.2f}".format(worker.get_hourly_pay()))


if __name__ == "__main__":
    main()
