Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import sys
>>> # int
>>> age = 21
>>> print(f"The size of int is {sys.getsizeof(age)} bytes")
The size of int is 28 bytes
>>> # str
>>> name = 'Kalpana'
>>> print(f"The size of str is {sys.getsizeof(name)} bytes")

The size of str is 56 bytes
>>> # float
>>> pi = 3.14
>>> print(f"The size of float is {sys.getsizeof(pi)} bytes")
The size of float is 24 bytes
>>> # list
>>> subjects = ['AO','ML','DV','SDN','CC']
>>> print(f"The size of list is {sys.getsizeof(subjects)} bytes")
The size of list is 120 bytes
>>> # boolean
>>> statement = True
>>> print(f"The size of boolean is {sys.getsizeof(statement)} bytes")
The size of boolean is 28 bytes
>>> # to check type of container/variable
>>> address = 123
>>> name = 45
>>> print(type(address))
<class 'int'>
>>> print(type(name))
<class 'int'>
>>> # complex number
>>> z=7+9j
>>> print(f"The size of complex number is {sys.getsizeof(z)} bytes")
The size of complex number is 32 bytes
>>> print("Real number is: ",z.real)
Real number is:  7.0
>>> print("Imaginary number is: ",z.imag)
Imaginary number is:  9.0
>>> # input statement
>>> name = input("Enter your name: ")
Enter your name: Kalpana
>>> print(f"Hello {name} Good to see you back")
Hello Kalpana Good to see you back
>>> 
