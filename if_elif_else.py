# if statement in Python

a = 10
b = 20
c = 40

"""
if a > b:
    print("a is greater then b")

if a < b:
    print("b is greater then a")
"""

"""
if a > b:
    print("a is greater then b")
else:
    print("a is not greater then b")
"""

"""
if (a > b & a > c):
    print("a is the greater")
elif (b > a & b > c):
    print("b is the greater")
else:
    print("c is the greater")
"""

"""
tup1 = (1, 2, 3, 4, 5)
if 6 in tup1:
    print("6 is present in tuple")
else:
    print("6 is not present in tuple")
"""

l1 = [1, 2, 3, 4, 5]
"""
if l1[1] == 2:
    l1[1] = l1[1]+100

print(l1)
"""

"""
if l1[4] == 10:
    l1[1] = l1[1]+100
else:
    l1[4] = l1[4]+500

print(l1)
"""

d1 = {"a":1, "b":2, "c":3, "d":4}
if d1["b"] == 2:
    d1["b"] = d1["b"] + 100
    
print(d1)