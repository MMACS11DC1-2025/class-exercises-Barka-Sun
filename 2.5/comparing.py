"""
Create a program that uses counting and comparison operators (< > <= >=).
You must use the class' datafile, 'responses.csv' and analyze it
    to make at least 2 interesting observations.
You must use user input to add interactivity to the program.
You must design your algorithm in English first, then translate it to Python code.
Test as you go! Describe in your comments what steps you took to test your code.
"""

# barak sun
# data analysis assignment
# compares your answers with a classmate's
# observation: prints matching answers to see similarities
# tested with barak sun and steven zhang

# open the csv file and skip the header
file = open("2.4/responses.csv")
lines = file.readlines()[1:]
file.close()

# ask user for their name and classmate's name
name = input("type your name: (full name) ").lower()
classmate = input("type your classmate's name: ").lower()

# find the rows for the user and classmate
your_line = []
classmate_line = []

for line in lines:
    parts = line.strip().split(",")
    if parts[1].lower() == name:
        your_line = parts
    if parts[1].lower() == classmate:
        classmate_line = parts

# compare answers and print matches
if len(your_line) > 0 and len(classmate_line) > 0:
    print("your matching answers are:")
    printed = False
    for i in range(2, len(your_line)):
        if your_line[i] == classmate_line[i]:
            print(your_line[i])
            printed = True
    if not printed:
        print("you didn't have any matching answers")
else:
    if len(your_line) == 0:
        print("your name not found")
    if len(classmate_line) == 0:
        print("classmate not found")
