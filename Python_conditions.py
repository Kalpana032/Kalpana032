# condition
# if else - Two conditions
name = input("Enter username for login: ")
password = input("Enter your password: ")
if(name == "Kalpana" and password == "admin@123"):
   print(f"Welcome {name} to Anudip Foundation")
else:
   print("Invalid credentials, please try again later")
print("Credits earned")
score = 22
if score > 18:
   print("Pass")
else:
   print("Fail")
# if elif - multiple conditions
print("Lets play a game: Guess a number")
num = int(input("Enter any number of your choice: "))
if num == 0:
   print("The number is not zero")
elif num > 10:
   print("The number is greater, Try again")
elif num < 10:
   print("The number is smaller, Try again")
elif num == 10:
   print("Its correct, you won!!!")
else:
   print("Try again later")
# for loop - defined range
print("Lets learn Even and Odd numbers")
for num in range(1,100):
   if num % 2 ==0:
      print(f"{num} is Even number")
   else:
      print(f"{num} is Odd number")
