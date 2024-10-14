Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # mathematical -,+,*,/,%,**,//
>>> num1 = 12
>>> num2 = 2
>>> print(num1 - num2)
10
>>> print(num1 + num2)
14
>>> print(num1 * num2)
24
>>> print(num1 / num2)
6.0
>>> print(num1 // num2)
6
>>> print(num1 ** num2)
144
>>> # comparison operator <.>,<=,>=,==,!=
>>> num1 = 150
>>> num2 = 250
>>> is_equal = (num1 == num2)
>>> print(is_equal)
False
>>> print(num1 < num2)
True
>>> print(num1 > num2)
False
>>> print(num1 <= num2)
True
>>> print(num1 >= num2)
False
>>> print(num1 != num2)
True
>>> # logical and,or,not
>>> print(num1 == 100 and num2 == 200)
False
>>> print(num1 == 100 or num2 == 250)
True
>>> # Assignment operator
>>> num1 = 90
>>> num2 = 88
>>> num3 = num2 + num1
>>> print(num3)
178
>>> num1 -= num2
>>> print(num1)
2
>>> num1 *= num2
>>> print(num1)
176
>>> num1 /= num2
>>> print(num1)
2.0
>>> num1 //= num2
>>> print(num1)
0.0
>>> x = 5
>>> x + 4
9
>>> print(x)
5
>>> x = x + 3
>>> print(x)
8
>>> # identity is, is not
>>> print(8 is 8)
True
>>> print(9 is not 10)
True
>>> print("Apple" is "Orange")
False
>>> print("Beetroot" is "Beetroot")
True
>>> print("Swizerland" is not "Egypt")
True
>>> # membership operator in, not in
>>> fruits_list = ["Mango","Guava","Cherry","Papaya","Watermelon"]
>>> print(fruits_list)
['Mango', 'Guava', 'Cherry', 'Papaya', 'Watermelon']
>>> is_available = "Muskmelon" in fruits_list
>>> print(is_available)
False
>>> print("Guava" in fruits_list)
True
>>> print("Strawberry" not in fruits_list)
True
>>> # BODMAS
>>> 5 * (8+2/5) - 2 + (6*4)
64.0
>>> 
