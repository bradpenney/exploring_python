# Based on the dictionary:
dream_car = {
    "model": "Pinto",
    "make": "Ford",
    "year": 1971,
    "mileage": 400
}

print(dream_car.get('engine', 'V8'))
# print(dream_car['make'])
# print(f"Dream car: {dream_car['year']} {dream_car['make']} {dream_car['model']}.")

# dream_car['make'] = "Ferrari"
# dream_car['model'] = "365 GTS/4 Daytona"
# dream_car['colour'] = "Rosso Chiaro"
# print(f"Dream car: {dream_car['year']} {dream_car['make']} {dream_car['model']} of the colour {dream_car['colour']}.")

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
