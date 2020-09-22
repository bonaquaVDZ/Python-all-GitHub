import math

my_name = 'Ramaniuk Vadzim'
my_age = 25
my_height = 74  # inches
my_weight = 180  # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Blond'

print(f"Lets talk about {my_name}.")
print("Lets talk about", my_name)  # My sample without point at the end.
print(f"He's {my_height} inches tall.")
print(f"He's {my_weight} pounds heavy.")
print("Actually that is not too heavy.")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f"His teeth are usually {my_teeth} depending on the coffee.")

# This line is tricky, try to get it exactly right.
total = my_age + my_height + my_weight
print(f"If I add {my_age}, {my_height} and {my_weight} I get {total}.")


# Study drills
# Try to write some variables that convert the inches and pounds to centimeters
# and kilograms.
# Convert to centimeters
inch = my_height
height_in_cent = my_height*2.54
print(height_in_cent)  # 187.96
print(round(height_in_cent))  # 188

# Convert to kilograms
pounds = my_weight
weight_in_kilo = pounds * 0.453592
print(weight_in_kilo)  # 81.64656
print(round(weight_in_kilo, 2))  # 81.65
