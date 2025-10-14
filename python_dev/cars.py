import random
# NOTE: Used Claude to generate this, was just specific in what I wanted.

# --------------------------------------
# CHALLENGE PART 1: Create the Car Class
# --------------------------------------
# TODO: Create a Car class with the following attributes:
# - make
# - model
# - year
# - color
# - price (stick to integers)
# - mileage
# - condition

class Car:
    def __init__(self, make, model, year, colour, price:int, mileage, condition):
        self.make = make
        self.model = model
        self.year = year
        self.colour = colour
        self.price = price
        self.mileage = mileage
        self.condition = condition
    
    #def __str__(self):
        #return f"{self.make} {self.model}"

# ----------------------------------------
# CHALLENGE PART 2: Random Car Generation
# ----------------------------------------
# Here are lookup dictionaries to use with random.choice() or random integer keys
CAR_DATA = {
    'makes': {
        0: 'Toyota', 1: 'Honda', 2: 'Ford', 3: 'Chevrolet', 
        4: 'BMW', 5: 'Mercedes', 6: 'Tesla', 7: 'Nissan',
        8: 'Hyundai', 9: 'Volkswagen'
    },
    'models': {
        0: 'Sedan', 1: 'SUV', 2: 'Truck', 3: 'Coupe',
        4: 'Hatchback', 5: 'Convertible', 6: 'Minivan', 7: 'Wagon'
    },
    'colors': {
        0: 'Red', 1: 'Blue', 2: 'Black', 3: 'White',
        4: 'Silver', 5: 'Gray', 6: 'Green', 7: 'Yellow'
    },
    'conditions': {
        0: 'New', 1: 'Excellent', 2: 'Good', 3: 'Fair', 4: 'Poor'
    }
}

class Inventory:
    def __init__(self, num_cars:int=5000): # Moved 'make:str' before 'num_cars" as it did't like being after it.
        self.cars = self.create_inventory(num_cars)
        #self.find_make = self.find_cars_by_make() # Not sure if 'find_make' is correct. Does not need to be here.


    def generate_random_car(self) -> Car:  
        """
        TODO: Create a function that generates a random car using:
        - random.choice() ntto pick from the dictionaries above
        - random.randint() for year (e.g., 2010-2024)
        - random.randint() for price (e.g., 5000-80000)
        - random.randint() for mileage (e.g., 0-150000)

        Returns: A new Car object with random attributes

        """
        return Car(
            make= random.choice(CAR_DATA['makes']),
            model= random.choice(CAR_DATA['models']), ## Note: Remember to populate these (not 'none'). ##
            colour= random.choice(CAR_DATA['colors']),
            condition= random.choice(CAR_DATA['conditions']),
            year= random.randint(2010, 2025), 
            price= random.randint(5000, 80000),
            mileage= random.randint(0, 150000)  
        )
    
    def create_inventory(self, num_cars:int=5000) -> list[Car]:
        """Generate a list of random cars"""
        # TODO: Use the `generate_random_car()` function above; either loop or list comprehension.
        inventory = []
        for _ in range(num_cars):
            inventory.append(self.generate_random_car()) 
        #print(num_cars)
    
        return inventory

    def find_cars_by_make(self, make:str) -> list[Car]:
        """Find all cars of a specific make"""
        result = []

        for car in self.cars:
            if car.make == make:
                result.append(car)
        return result

    #print(find_cars_by_make()) # I am missing something here.... and/or incorrect.

inv = Inventory() 
print(len(inv.find_cars_by_make("BMW")))
print(len(inv.find_cars_by_make("Honda")))

    


# -----------------------------------------
# CHALLENGE PART 3: Generate Car Inventory
# -----------------------------------------

#print(inventory) ## add attribute to return as string. example ".make" ##

# --------------------------------------
# CHALLENGE PART 4: Query the Inventory
# --------------------------------------
# TODO: Write functions to answer these questions:


#r = find_cars_by_make(inventory, "Volkswagen")
#print(r[0].make, r[0].model)

def find_affordable_cars(cars:list[Car], max_price:int) -> list[Car]:
    """Find all cars under a certain price"""
    result = []

    for car in cars:
        if car.price <= max_price:
            result.append(car) 
            
    return result

#print(find_affordable_cars(inventory, 30000)[0].price)

def find_low_mileage_cars(cars:list[Car], max_mileage:int) -> list[Car]:
    """Find all cars with mileage below a threshold"""
    result = []

    for car in cars:
        if car.mileage <= max_mileage:
            result.append(car)
    return result

#print(find_low_mileage_cars(inventory, 12000)[0].mileage)

def find_newest_cars(cars:list[Car], min_year:int) -> list[Car]:
    """Find all cars from a specific year or newer"""
    result = []

    for car in cars:
        if car.year >= min_year:
            result.append(car)
    return result

#print(find_newest_cars(inventory, 2022)[0].year)

def get_average_price_by_make(cars:list[Car], make:str) -> int:
    """Calculate the average price for a specific make"""
    result = 0

    #for car in cars:
    #    car.make == find_cars_by_make()
    #    if make == car.make:
    #        for n in Car.price:
    #            result += n
    #            result = result / len(Car.price)
    #            print(result)

    cars = find_cars_by_make(cars, make)

    prices = []  # A list holds unlimited number or objects.
    for car in cars:
        prices.append(car.price)

    result = sum(prices) / len(prices)

    return int(result)
    
#print(get_average_price_by_make(inventory, "Honda"))


#inv2 = create_inventory(100000)
#inv2 = find_cars_by_make(inv2, "BMW")
#inv2 = find_affordable_cars(inv2, 30000)
#inv2 = find_newest_cars(inv2, 2020)
#for c in inv2:
#    if c.colour == "Green" and c.model == "Wagon":
#        print(c.make, c.model, c.colour, c.condition, c.mileage, c.price)

# ----------------------------------
# CHALLENGE PART 5: Test Your Code!
# ----------------------------------
# TODO: Uncomment and run these tests once you've implemented everything

#print(f"Total cars in inventory: {len(inventory)}")
#print(f"Toyota cars: {len(find_cars_by_make(inventory, 'Toyota'))}")
#print(f"Cars under $20,000: {len(find_affordable_cars(inventory, 20000))}")
#print(f"Low mileage cars (<30k): {len(find_low_mileage_cars(inventory, 30000))}")
#print(f"Cars from 2020+: {len(find_newest_cars(inventory, 2020))}")
#print(f"Average BMW price: ${get_average_price_by_make(inventory, 'BMW'):,.2f}")