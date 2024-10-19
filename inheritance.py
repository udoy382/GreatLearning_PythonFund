# Inheritance in Python


class Vehicle:
    def __init__(self, mileage, cost):
        self.mileage = mileage
        self.cost = cost

    def show_details(self):
        print("I am a vehicle")
        print(f"The mileage is {self.mileage} and cost is {self.cost}")


v1 = Vehicle(300, 1000)

# v1.show_details()


class Car(Vehicle):
    def __init__(self, mileage, cost, tyres, hp):
        super().__init__(mileage, cost)

        self.tyres = tyres
        self.hp = hp

    def show_car_details(self):
        print("I am a car")
        print(f"Number of tyres of {self.tyres} and horse power is {self.hp}")


# c1 = Car(100, 2000)

# c1.show_details()
# c1.show_car_details()
# v1.show_details()


c1 = Car(500, 50000, 8, 200)

# c1.show_details()
c1.show_car_details()