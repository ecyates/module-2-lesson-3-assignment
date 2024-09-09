# 2. Advanced List Methods and Identity Operators
# Problem Statement: You have two lists of student names. 
# One list contains the names of students who have submitted their assignments, 
# and the other list contains the names of students who attended the last class.

# Task 1: Given the two lists provided, find out if Alice submitted their assignment and attended class. 

# HINT: How might the in keyword be of use here? And how can you check to see if Alice is in both submitted 
# and attended in one if statement?

# The list of students who submitted their assignments
submitted = ["Alice", "Bob", "Charlie", "David"]
# The list of students who attended the class
attended = ["Charlie", "Eve", "Alice", "Frank"]

# Report if Alice submitted the assignment AND attended the class
if "Alice" in submitted and "Alice" in attended:
    print("Alice submitted her assignment and attended the class!")
# Report if Alice submitted the assignment but did not attend the class
elif "Alice" in submitted and "Alice" not in attended:
    print("Alice submitted the assignment but did NOT attend the class!")
# Report if Alice did not submit the assignment but she did attend the class
elif "Alice" not in submitted and "Alice" in attended:
    print("Alice did NOT submit the assignment but she did attend the class")
# Report if Alice did not submit the assignment or attend the class
else:
    print("Alice did NOT submit the assignment or attend the class!")