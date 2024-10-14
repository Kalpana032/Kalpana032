#Q1
num = int(input("Q1\nEnter a number: "))
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")
#Q2
age = int(input("Q2\nEnter your age: "))
if age >= 18:
    print("You are Eligible to vote")
else:
    print("You are not eligible to vote")
#Q3
year = int(input("Q3\nEnter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")
#Q4
num = float(input("Q4\nEnter a number: "))
if num > 0:
    print("The given number is Positive")
elif number < 0:
    print("The given number is Negative")
else:
    print("The given number is Zero")
#Q5
num1 = int(input("Q5\nEnter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
if num1 >= num2 and num1 >= num3:
    print(f"The largest number is {num1}")
elif num2 >= num1 and num2 >= num3:
    print(f"The largest number is {num2}")
else:
    print(f"The largest number is {num3}")
