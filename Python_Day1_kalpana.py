# Q1.
print("Q1: \nHello World")
# Q2.
a = "Global_variable"
def function():
    a = "Local_variable"
    print("\nQ2: \nInside function:", a)
function()
print("Outside function:", a)
# Q3.
def error():
 print("\nThis code shows an Indentation Error")
# Q4.
b = 10
def roles_function():
    b = 20
    print("\nQ4: \nLocal:", b)
roles_function()
print("Global:", b)
# Q5.
student_name = 'Kalpana Madhavan'
student_marks = 450
student_cgpa = 9.07
print(f"\nQ5: \nName: {student_name} \nMarks: {student_marks} \nCGPA: {student_cgpa}")

