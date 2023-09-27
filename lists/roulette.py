#!/usr/bin/python3

import random
names_as_csv = input("Give me everybody's names:  ")
names = names_as_csv.split(", ")
limit = len(names) - 1
index = random.randint(0, limit)
print(names[index])