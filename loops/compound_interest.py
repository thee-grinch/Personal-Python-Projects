#!/usr/bin/python3

# this is a function that calculates compound interest after 10 years
principle, interest = input("Please enter principle, interest: ").split()
principle = float(principle)
interest = float(interest)
interest = interest / 100
for i in range(10):
    principle = principle + (principle * interest)
# printing the outcome
print("The total amount accumulatted is {:.2f}".format(principle))
