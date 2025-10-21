
from datetime import date
today = date.today()
CURRENT_YEAR = today.year  # Block caps means a constant that is never going to change, technically year can change, but for this scope, it's fine.

class Trim:
    def __init__(self, features):
        self.features = features

class Car:
    def __init__(self, brand, model, year, features, power, tyres):
        self.brand = brand
        self.model = model 
        self.year = year
        self.trim = Trim(features)
        self.power = power
        self.tyres = tyres
        self.colour = "primed"
        self.age = self.calc_age()  # OR: self.age = CURRENT_YEAR - year
    
    def is_sold(self):
        if self.year == 1998:
            print(f"{self.model} is Sold.")
        else:
            print("Car still owned")    

# Hmm, discussion in one line, maybe useful.

    def upgrade(self):
        if self.power <= 120:
            if self.tyres == "worn":
                print(f"The {self.brand} needs a remap and needs new tyres")
            elif self.tyres == "good":
                print(f"{self.brand}'s tyres are in good condition, only needs remap.")
        else:
            if self.tyres == "worn":
                print(f"{self.brand} has sufficient power, but needs new tyres.")
            elif self.tyres == "good":
                print(f"{self.brand} has sufficient power and tyres are good!")


    def calc_age(self):
            # Seems a bit basic to be a method on it's own, but it's good to abstract in case you want to do more later, but you could do this in the init method.
            self.age = CURRENT_YEAR - self.year




    def paint_v2(self, new_colour:str, repaint:bool=False):
        if self.colour == "primed":
            print(f"{self.model} was primed, has now been painted {new_colour}.")
            self.colour = new_colour
        else:  # Already has a colour.
            if repaint:  # Checking passed bool value is True.
                print(f"{self.model} was {self.colour}, is now painted {new_colour}.")
                self.colour = new_colour
            else:
                print(f"Not allowed to paint {self.model} {new_colour}, remains {self.colour}.")

car1 = Car(
    brand="Volkswagen",
    model="Transporter",
    year=2014,
    features=["big", "heavy"],
    power=140,
    tyres="worn",
)
car2 = Car(
    brand="Fiat",
    model="Punto",
    year=1998,
    features=['sporty'],
    power=100,
    tyres="good",
)

print(car1.brand)
print(car2.year)

car1.is_sold()

print(car1.trim.features)
print('-' * 20)

car1.upgrade()
car2.upgrade()
car1.paint_job()

car1.paint_v2('red')

print(car1.age)