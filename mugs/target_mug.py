from mug_base import Mug

class Target(Mug):
    def __init__(self):
        super().__init__("Target mug", "yellow")
    def extras(self):
        return f"This mug comes a sample of Brazilian coffee beans"
    
mug1 = Target()

print(mug1.extras())
