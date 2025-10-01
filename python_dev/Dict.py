# car dictionary
car1 = {
    "Make" : "Volkswegan",
    "Model": "Transporter",
    "Colour": "Black",
    "Year": "2013"
}

car2 = {
    "Make" : "Volkswegan",
    "Model": "Golf GTI",
    "Colour": "Black",
    "Year": "2005",
    "Doors": "Five"
}

car3 = {
    "Make" : "Volvo",
    "Model": "V70",
    "Colour": "Grey",
    "Year": "2008"
}

car4 = {
    "Make" : "BMW",
    "Model": "5 Series",
    "Colour": "Silver",
    "Year": "2007"
}

car5 = {
    "Make" : "Fiat",
    "Model": "Punto",
    "Colour": "White",
    "Year": "1998"
}
cars = [car1, car2, car3, car4, car5]
#print(cars)


# add item to dict
for car in cars:
    if car["Make"] == "Fiat" or car["Make"] == "Volvo":
        car["Fuel type"] = "Diesel"
    else:
        car.update({"Fuel type": "Petrol"})
    print(car)

# Access an item
print(car2["Colour"])


#Get all Identifiers 
for car in cars:
    print(car.keys())


# Get all Values
for car in cars:
    print(list(car.values()))


print('-' * 20)
# Get all Pairs
for car in cars:
    print(car.items())
    for k, v in car.items():
        print(k, v)

       
# Delete an item from list
for car in cars:
    car.pop("Colour")
print(cars)

