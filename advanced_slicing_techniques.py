# 3. Advanced Slicing Techniques 
# Objective: The aim of this assignment is to use Python list slicing.
# Problem Statement: You have a list of daily temperatures for one month, 
# and you'd like to extract specific data from it.

# Task 1: Given the list of temperatures, extract the temperatures for the second week (7 days) 
# of the month (index 7 to index 14). Expected Outcome: 83, 85, 86, 87, 88, 89, 90,

# Task 2: Extract all the temperatures above 100. 
# HINT: add the temperatures over 100 to a new list, or use list slicing to get the temperatures.

# Take the list of temperatures
temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]
# Extract the temps for the 2nd week (7-14)
week_2_temps = temperatures[7:14]
# Print 
print(week_2_temps)

# Create a new list of temps over 100
temps_over_100 = []
# For each temperature that is over 100, append it to the new list
for i in temperatures: 
    if i > 100: 
        temps_over_100.append(i)

# Print
print(temps_over_100)