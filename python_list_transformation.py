# 1 - Python List Transformation
# Objective: The aim of this assignment is to practice list operations and transformations.
# Problem Statement: You've been given a list of grades from an exam. 
# You need to process and analyze these grades.

# Task 1: Given the list of grades, sort the grades in descending order and print the sorted list.
# Task 2: Calculate the average grade and print it.

# Take a list of grades
grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
# Sort the list in ascending order first
grades.sort()
# Reverse that order to make it descending order
grades.reverse()
# Print the sorted list
print("Grades:", grades)

# To calculate the average, we need to add up each item and divide by the length
ave = 0
# For each grade, add it to the average
for i in grades:
    ave += i
# Divide by the length
ave /= len(grades)
# Print the average grade
print("Average Grade:", ave)