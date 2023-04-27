# Style the Project
# Open the file and read the grades
with open('grades.txt', 'r') as file:
    student_lines = file.readlines()[2:]  # Skip the header rows
    raw_grades = [float(line.split()[1]) for line in student_lines]
# Find the highest grade and the corresponding student name
highest_grade = max(raw_grades)
highest_grade_index = raw_grades.index(highest_grade)
with open('grades.txt', 'r') as file:
    lines = file.readlines()[2:]  # Skip the header rows
    highest_grade_student_name = lines[highest_grade_index].split()[0]
# Print the result
print("\033[32m" + f"The highest grade is {highest_grade} and it belongs to {highest_grade_student_name}" + "\033[0m")
# Checking Error
# print(highest_grade)
# print(highest_grade_student_name)