# Style the Project
# Open the file and read the grades
with open('grades.txt', 'r') as file:
    student_lines = file.readlines()[2:]  # Skip the header rows
    raw_grades = [float(line.split()[1]) for line in student_lines]
# Find the highest grade and the corresponding student name
highest_grade = max(raw_grades)
# Print the result
# Checking Error
print(highest_grade)