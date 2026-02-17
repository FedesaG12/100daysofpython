class Animal():
    def __init__(self):
        self.eyes = 2
    def behavior(self):
        print("Moving,Eating and running")
    
animal = Animal()

class Whale(Animal):
    def __init__(self):
        super().__init__()
    def behavior(self):
        super().behavior()
        print("Moving under water.")
whaley = Whale()

print(whaley.eyes)
print(whaley.behavior())