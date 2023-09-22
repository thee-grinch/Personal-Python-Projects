#!/usr/bin/python3

"""This program calculates the weeks, months and days remaining to reach 90 years of age"""
age = int(input("Enter Your Age: "))
rem = 90 - age

days = rem * 365
weeks = rem * 52
months = rem * 12

print(f"You have {days} days, {weeks} weeks and {months} months left.")
