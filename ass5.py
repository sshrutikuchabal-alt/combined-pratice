# Ask the user for input
name = input("Enter your name: ")
age = int(input("Enter your age: "))

marks1 = int(input("Enter marks for subject 1: "))
marks2 = int(input("Enter marks for subject 2: "))
marks3 = int(input("Enter marks for subject 3: "))

# Calculate average marks
average_marks = (marks1 + marks2 + marks3) / 3

# Display the result
print("Name:", name)
print("Age:", age)
print("Average Marks:", average_marks)
