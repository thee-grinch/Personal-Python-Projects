#!/usr/bin/python3
"""This code attempts to calculate the bmi of a person"""
height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")

height = float(height)
weight = float(weight)

bmi = weight / (height ** 2)

print("Your BMI is {:.2f}".format(bmi))