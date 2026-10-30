#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  4 23:59:32 2025

@author: jadamalone
"""


class Employee:
    def __init__(self, name, id_number):
        self.name = name
        self.id_number = id_number

    def set_name(self, name):
        self.name = name

    def set_id_number(self, id_number):
        self.id_number = id_number

    def get_name(self):
        return self.name

    def get_id_number(self):
        return self.id_number


class ProductionWorker(Employee):
    def __init__(self, name, id_number, shift, hourly_pay):
        super().__init__(name, id_number)
        self.shift = shift
        self.hourly_pay = hourly_pay

    def set_shift(self, shift):
        self.shift = shift

    def set_hourly_pay(self, hourly_pay):
        self.hourly_pay = hourly_pay

    def get_shift(self):
        return self.shift

    def get_hourly_pay(self):
        return self.hourly_pay
