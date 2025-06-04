class Dog:
    """A class to define a dog"""
    def __init__(self, name: str = "Gimli", age: int = 13):
        self.legs: int = 4
        self.ears: int = 2
        self.name: str = name
        self.age: int = age

gimli = Dog('gimli',13)
print(gimli.legs)
print(gimli.age)
