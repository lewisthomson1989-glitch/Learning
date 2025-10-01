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
make = random.choice(CAR_DATA['makes'])
model = random.choice(CAR_DATA['models'])
colour = random.choice(CAR_DATA['colors'])
condition = random.choice(CAR_DATA['conditions'])

print(make, model, colour, condition) # prints a random car.
def generate_random_car() -> Car:  # I had noticed you passed self as an arg here, that only applies for methods, which are functions inside classes.
    """
    TODO: Create a function that generates a random car using:
    - random.choice() ntto pick from the dictionaries above
    - random.randint() for year (e.g., 2010-2024)
    - random.randint() for price (e.g., 5000-80000)
    - random.randint() for mileage (e.g., 0-150000)
    
    Returns: A new Car object with random attributes

    """
    # Ok, Car() first arg needs to be a make. Here's a clue for getting random make value.
    # random.randint(start, stop) = lowest and highest possible values, they need to match the number of elements in your iterable.
    # You know with an int, you can match that to the key in your dictionary. Eg CAR_DATA["makes"][6] is "Tesla"
    # randint() returns an int, you can use that to get a random key.
    # Random choice actually works better here, save randint for those monetary/mileage values.

    # Example: model = random.choice(CAR_DATA["models"])  # not self.model?
    for r in car:
        make = random.choice(CAR_DATA['makes'])
        model = random.choice(CAR_DATA['models'])
        colour = random.choice(CAR_DATA['colors'])
        condition = random.choice(CAR_DATA['conditions'])

    print(make, model, colour, condition)
    
    car = Car(
        # You need to figure all these None's out. You can save as variables and pass them in, or just call on random for the value.
        make=None,
        model=None,
        year=None,
        colour=None,
        price=None, # Not from CAR_DATA
        mileage=None,
        condition=None  # From CAR_DATA again.
    )
    return car

# -----------------------------------------
# CHALLENGE PART 3: Generate Car Inventory
# -----------------------------------------
# TODO: Create a list of 5000 random cars

def create_inventory(num_cars:int=5000) -> list[Car]:
    """Generate a list of random cars"""
    # TODO: Use the `generate_random_car()` function above; either loop or list comprehension.
    inventory = []
    return inventory

inventory = create_inventory(5000)

# --------------------------------------
# CHALLENGE PART 4: Query the Inventory
# --------------------------------------
# TODO: Write functions to answer these questions:

def find_cars_by_make(cars:list[Car], make:str) -> list[Car]:
    """Find all cars of a specific make"""
    result = []
    return result

def find_affordable_cars(cars:list[Car], max_price:int) -> list[Car]:
    """Find all cars under a certain price"""
    result = []
    return result

def find_low_mileage_cars(cars:list[Car], max_mileage:int) -> list[Car]:
    """Find all cars with mileage below a threshold"""
    result = []
    return result

def find_newest_cars(cars:list[Car], min_year:int) -> list[Car]:
    """Find all cars from a specific year or newer"""
    result = []
    return result

def get_average_price_by_make(cars:list[Car], make:str) -> int:
    """Calculate the average price for a specific make"""
    result = 0
    return result

# ----------------------------------
# CHALLENGE PART 5: Test Your Code!
# ----------------------------------
# TODO: Uncomment and run these tests once you've implemented everything

# print(f"Total cars in inventory: {len(inventory)}")
# print(f"Toyota cars: {len(find_cars_by_make(inventory, 'Toyota'))}")
# print(f"Cars under $20,000: {len(find_affordable_cars(inventory, 20000))}")
# print(f"Low mileage cars (<30k): {len(find_low_mileage_cars(inventory, 30000))}")
# print(f"Cars from 2020+: {len(find_newest_cars(inventory, 2020))}")
# print(f"Average BMW price: ${get_average_price_by_make(inventory, 'BMW'):,.2f}")