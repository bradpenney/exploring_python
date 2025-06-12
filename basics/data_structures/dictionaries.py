"""
Explaining Dictionaries in Python
"""

# Create a dictionary to represent a vehicle
dream_car = {
    "model": "Pinto",
    "make": ["Ford", "Chevrolet"],
    "year": 1971,
    "mileage": 400
}

dream_car_engine = {
    "engine": "V8",
    "horsepower": 440,
    "cylinders": 8
}

import copy
dream_car2 = copy.deepcopy(dream_car)
print(f"Dream Car: {dream_car}")
print(f"Dream Car 2: {dream_car2}")

dream_car['make'].append("Dodge")
print(f"Dream Car after model change: {dream_car}")
print(f"Dream Car 2 after Dream Car model change: {dream_car2}")

# print(f"Dream Car Object ID: {id(dream_car)}")
# dream_car.clear()
# print(f"Dream Car after clear: {dream_car}")
# print(f"Dream Car Object ID after clear: {id(dream_car)}")

# dream_car.update(dream_car_engine)
# print(f"Dream Car: {dream_car}")
# print(f"Dream Car Engine: {dream_car_engine}")
# print(f"Dream car: {dream_car['year']} {dream_car['make']} {dream_car['model']}.")

# dream_car['make'] = "Ferrari"
# dream_car['model'] = "365 GTS/4 Daytona"
# dream_car['colour'] = "Rosso Chiaro"
# print(f"Dream car: {dream_car['year']} {dream_car['make']} \
#       {dream_car['model']} with the {dream_car['engine']} engine.")

# engine_parts = [1, 2, 3, 4, 5]
# dream_car[engine_parts] = 563 # This line will raise an error because lists cannot be used as dictionary keys


# # Create a for loop to print all keys and values
# print("Vehicle 1:")
# for key, value in my_vehicle.items():
#     print(f"{key.title()}: {value}")

# # Create a new variable vehicle2, which is a copy of my_vehicle
# my_vehicle_2 = my_vehicle.copy()

# # Add a new key 'number_of_tires' to the vehicle2 variable that is equal to 4
# my_vehicle_2['number_of_tires'] = 4

# # Delete the mileage key from vehicle2
# my_vehicle_2.pop('mileage')

# # Print just the keys from vehicle2
# print("\nVehicle 2:")
# for key in my_vehicle_2:
#     print(f"{key.title()}")
