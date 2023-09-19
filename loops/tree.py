#!/usr/bin/python3

# This program attempts to draw a tree
height = int(input("Enter Your tree height: "))
space = height - 1
char = 1
for _ in range(height):
    for _ in range(space):
        print(" ", end="")
    print('#' * char)
    char += 2
    space -= 1
for _ in range(height - 1):
    print(" ", end="")
print("#")
