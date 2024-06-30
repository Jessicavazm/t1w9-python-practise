class Mug:
    def __init__(self, name, colour):
        self.name = name
        self.colour = colour
        self.status = "Full"

    def drink(self):
        self.status = "Empty"

    def fill(self):
        self.status = "Full"

mug1 = Mug("Kmart mug", "white")
mug2 = Mug("Target mug", "pink")


mug1.drink()
mug1.fill()

mug2.drink()

print(f"The {mug1.name} is currently {mug1.status}")
print(f"The {mug2.name} is currently {mug2.status}")

