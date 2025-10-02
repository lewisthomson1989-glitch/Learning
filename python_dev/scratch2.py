from cars import CAR_DATA
import random

make = random.choice(CAR_DATA['makes'])
model = random.choice(CAR_DATA['models'])
colour = random.choice(CAR_DATA['colors'])
condition = random.choice(CAR_DATA['conditions'])

print(make, model, colour, condition)

