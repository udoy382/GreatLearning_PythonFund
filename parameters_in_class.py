# Adding Parameters to a Class Method


class Phone:
    def make_call(self):
        print("Making a call")

    def play_game(self):
        print("Playing a game")

    def set_color(self, color):
        self.color = color

    def set_cost(self, cost):
        self.cost = cost

    def show_color(self):
        return self.color

    def show_cost(self):
        return self.cost


p2 = Phone()

p2.set_color("blue")
p2.set_cost(500)

print(p2.show_color())
print(p2.show_cost())

p2.play_game()
p2.make_call()
