# Looping Statements in Python

"""
i = 1
while i <= 10:
    print(i)
    i += 1
"""

"""
i = 1
n = 2

while i <= 10:
    print(n, " * ", i, " = ", n*i)
    i += 1
"""

"""
l1 = [1, 2, 3, 4, 5]
i = 0

while i < len(l1):
    l1[i] = l1[i] + 100
    i += 1

print(l1)
"""

"""
f1 = ["apple", "banana", "orange"]

for i in f1:
    print(i)
"""


l1 = ["orange", "blue", "green"]
l2 = ["book", "chair", "phone"]

for i in l1:
    for j in l2:
        print(i, j)
