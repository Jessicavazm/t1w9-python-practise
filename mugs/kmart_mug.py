from mug_base import Mug

class Kmart(Mug):
    def __init__(self):
        super().__init__("Kmart mug", "purple")

    def extras(self):
        return f"This mug comes with small gift"
    
kmart_mug = Kmart()

print(kmart_mug.extras()) 