#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  8 22:25:23 2025

@author: jadamalone
"""

class RetailItem:
    def __init__(self, description, units, price):
        # Constructor to initialize attributes
        self.description = description
        self.units = units
        self.price = price

    # Getter (Accessor) methods
    def get_description(self):
        return self.description

    def get_units(self):
        return self.units

    def get_price(self):
        return self.price

    # Setter (Mutator) methods
    def set_description(self, description):
        self.description = description

    def set_units_in_inventory(self, units):
        self.units = units

    def set_price(self, price):
        self.price = price

