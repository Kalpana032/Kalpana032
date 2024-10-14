# functions - block of code
def greeting():
    print("Hello world")
greeting()
# parameters and arguments
def greetings(name):
    msg = f"Welcome, {name}"
    return msg
#msg = greetings("Kalpana")
print(greetings("Kalpana"))
# Even and odd number
def checkEven():
    for i in range(1,20):
        if i % 2 == 0:
            print(f"{i} is Even number")
        else:
            print(f"{i} is Odd number")
print(checkEven())
# pass
def checkOdd():
    for i in range(1,20):
        if i % 2 == 0:
            pass # skip
        else:
            print(f"{i} is Odd number")
print(checkOdd())
# break
def num():
    for i in range(10):
        if i == 5:
            break # loop stops
        else:
            print(f"{i}")
print(num())
