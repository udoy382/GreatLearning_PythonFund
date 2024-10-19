# Basic Problems in Python


# Problem 1 ==>
"""
num = int(input("Enter a number: "))
if (num % 2) == 0:
    print(num, " is even")
else:
    print(num, " is odd")
"""

# Problem 2 ==>
"""
num = float(input("Enter a number: "))
if num > 0:
    print("positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")
"""

# Problem 3 ==>
"""
num = int(input("Enter a number: "))
factorial = 1
if num < 0:
    print("Sorry, factorial does not exis for negative numbers")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1, num + 1):
        factorial = factorial * i
    print("the factorial of ", num, " is ", factorial)
"""

# Problem 4 ==>
"""
n = int(input("Enter number: "))
rev = 0
while(n > 0):
    dig = n % 10
    rev = rev * 10 + dig
    n = n // 10
print("Reverse of the number: ", rev)
"""

# Problem 5 ==>
"""
n = int(input("Enter number: "))
a = 0
b = 1
if n < 0:
    print("Incorrect input")
elif n == 0:
    print(a)
elif n == 1:
    print(a)
else:
    for i in range(2, n):
        c = a + b
        a = b
        b = c
    print(b)
"""

# Problem 6 ==>
for num in range(10):
    for i in range(num):
        print(num, end=" ")
    print("\n")