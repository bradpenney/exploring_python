# Create a function that takes in 3 parameters(firstname, lastname, age) and returns a dictionary based on those values

def person(firstname: str, lastname: str, age: int) -> dict:
    person = {
        'firstname': firstname,
        'lastname': lastname,
        'age': age 
        }
    return person

me = person("Brad","Penney", 2)
for key, value in me.items():
    print(f"{key.title()}: {value}")


