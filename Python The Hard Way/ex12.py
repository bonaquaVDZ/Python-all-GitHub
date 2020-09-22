age = input("How old are you? ")
height = input(f"You're {age} nice. How tall are you? ")
weight = input("How much do you weigh? ")

print(f"So you're {age} years old, {height} tall and {weight} heavy.")

print(">>>> age, height, weight: ", repr(age), repr(height), repr(weight))
# repr() - return a string containing a printable representation of an object.
