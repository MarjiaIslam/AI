import math
import random
import csv
from collections import deque

# File paths (adjust if necessary)
engine_file = "engines.txt"
tire_file = "tires.txt"
transmission_file = "transmissions.txt"
valid_cars_file = "valid_cars.csv"

valid_cars = set()

class Car:
    def __init__(self, engine, tire, transmission, roof):
        # write code here

    def __eq__(self, other):
        # write code here

    def __hash__(self):
        return hash((self.engine, self.tire, self.transmission, self.roof))

    def __repr__(self):
        return f"({self.engine}, {self.tire}, {self.transmission}, {self.roof})"

def load_cars(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header if present
        for engine, tire, transmission, roof in reader:
            valid_cars.add(Car(engine, tire, transmission, roof))

def content_reader(filename):
    with open(filename) as file:
        return [line.strip() for line in file]

def compare_with_target(car1, car2):
    # write code here

def delta_e(current, candidate, target):
    return compare_with_target(current, target) - compare_with_target(candidate, target)

def get_e(delta, level):
    t = 1.0 / level
    return math.exp(delta / t)

# Load data
engines = content_reader(engine_file)
transmissions = content_reader(transmission_file)
tires = content_reader(tire_file)
roofs = ["Sunroof", "Moonroof", "Noroof"]
load_cars(valid_cars_file)

# Define start and goal
start_car = Car("EFI", "Danlop", "AT", "Noroof")
goal_car = Car("V6", "Hankook", "AT", "Moonroof")

# comment out the above line and uncomment the below line to test with a different goal
#goal_car = Car("V12", "Pirelli", "CVT", "Sunroof")


# Check if goalis valid
if goal_car not in valid_cars:
    print("Goal car is not valid.")
    exit(1)

# BFS with Simulated Annealing heuristic
current_level_cars = deque()
seen = set()
seen.add(start_car)
current_level_cars.append(start_car)

goal_reached = False
year = 0

while current_level_cars:
    year += 1
    next_level_cars = deque()
    
    while current_level_cars:
        current_car = current_level_cars.popleft()
        print(f"Year {year}: {current_car}")

        # Explore one-component changes
        for engine in engines:
            candidate = # create new car object with new engine
            if candidate != current_car and candidate in valid_cars and candidate not in seen:
                # calculate delta_e
                # check if delta_e > 0, then just pick the child car
                # else check if delta_e < 0, then pick the child car with some probability
                # if the car is picked, add it to next_level_cars
                # and add it to seen
        if goal_reached: break

        # do the same for tires
        if goal_reached: break

        # do the same for transmissions
        if goal_reached: break

        # do the same for roofs
        if goal_reached: break
    
    if goal_reached:
        break
    current_level_cars = next_level_cars

print(f"\nTotal years (steps) taken: {year + 1 if goal_reached else 'Not reached'}")
