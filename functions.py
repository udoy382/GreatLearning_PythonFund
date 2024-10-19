# Function in Python

"""
def hello():
    print("Hello world!")

hello()
"""

# Function with parameter ~
"""
def add10(x):
    return x + 10

y = add10(10)
print(y)
"""

"""
def even_odd(x):
    if x % 2 == 0:
        print(x, " is even")
    else:
        print(x, " is odd")

even_odd(5)
"""

# Lambda function ~
"""
g = lambda x: x * x * x
print(g(7))
"""

# Lambda function with filter ~
"""
li = [3, 5, 5, 4, 7, 6, 5, 65, 72, 5, 11, 54, 6]
first_list = list(filter(lambda x: (x % 2 != 0), li))
print(first_list)
"""


# Lambda function with map ~
"""
li = [5, 3, 6, 7, 5, 65, 54, 65, 43, 65, 61, 54, 6]
final_list = list(map(lambda x : x * 2, li))
print(final_list)
"""

# Reduce function in Python ~
from functools import reduce
li = [5, 7, 8, 24, 54, 65, 34, 5, 32, 76, 5]
sum = reduce((lambda x, y: x + y), li)
print(sum)
