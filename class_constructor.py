# Creating a Class with Constructor 


class Employee:
    def __init__(self, name, age, salary, gender):
        self.name = name
        self.age = age
        self.salary = salary
        self.gender = gender

    
    def show_details(self):
        print("The name of Employee is ", self.name)
        print("The age of Employee is ", self.age)
        print("The salary of Employee is ", self.salary)
        print("The gender of Employee is ", self.gender)

e1 = Employee("Udoy", 18, 112000, "Male")

e1.show_details()