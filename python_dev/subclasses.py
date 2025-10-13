class Mammal:
    def __init__(self):
        self.fur = True
        self.birth = "live"


class Dog(Mammal):
    def __init__(self):
        super().__init__()
        self.num_paws = 4


d = Dog()
print(d.num_paws)
print(d.birth)