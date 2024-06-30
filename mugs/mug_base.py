class Mug:
    def __init__(self, name, colour):
        self.name = name
        self.colour = colour
        self.status = "Full"

    def drink(self):
        self.status = "Empty"
        return f"I'm drinking from the {self.name}."

    def fill(self):
        self.status = "Full"
        return f"I'm filling the {self.name}"
    
mug1 = Mug("Kmart mug", "white")
mug2 = Mug("Target mug", "pink")


mug1.drink()
mug1.fill()

mug2.drink()

print(f"The {mug1.name} is currently {mug1.status}")
print(f"The {mug2.name} is currently {mug2.status}")

print(mug1.drink())