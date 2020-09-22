cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")


# The =(single-equal) assigns value on the right to a variable to the left.
# The ==(double-equal) tests wether two things have the same value.
x = 10
i = 3
j = 10
m = j
if x == j:
    print(bool(1))
else:
    print("10 and 10 is unequal")
if x == i:
    print(bool(0))
else:
    print("10 is not equal 3")
if m == x:
    print("Of course M is equal X and inversely")
else:
    print("M doesnt equal X")
