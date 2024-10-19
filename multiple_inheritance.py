# Types of Inheritance


# Multiple Inheritance ~
"""
class Parent1:
    def assign_str1(self, str1):
        self.str1 = str1

    def show_str1(self):
        print(self.str1)


class Parent2:
    def assign_str2(self, str2):
        self.str2 = str2

    def show_str2(self):
        print(self.str2)


class Child(Parent1, Parent2):
    def assign_str3(self, str3):
        self.str3 = str3

    def show_str3(self):
        print(self.str3)


c1 = Child()

c1.assign_str1("Udoy")
c1.assign_str2("Mariyam")
c1.assign_str3("Sara")

c1.show_str1()
c1.show_str2()
c1.show_str3()
"""

# Multi-Level Inheritance ~


class Parent:
    def assign_name(self, name):
        self.name = name

    def show_name(self):
        print(self.name)


class Child(Parent):
    def assign_age(self, age):
        self.age = age

    def show_age(self):
        print(self.age)


class GrandChild(Child):
    def assign_gender(self, gender):
        self.gender = gender

    def show_gender(self):
        return self.gender


g1 = GrandChild()

g1.assign_name("Anne")
g1.assign_age(10)
g1.assign_gender("Female")

g1.show_name()
g1.show_age()
x = g1.show_gender()
print(x)