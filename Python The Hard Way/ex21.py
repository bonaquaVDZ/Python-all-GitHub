def add(a, b):
    print(f"Adding {a} + {b}.")
    return a + b


def subtract(a, b):
    print(f"Subtracting {a} - {b}.")
    return a - b


def multiply(a, b):
    print(f"Multiplying {a} * {b}.")
    return a * b


def divide(a, b):
    print(f"Dividing {a} / {b}.")
    return a / b


print("Let's do some math with just functions.")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print(f"Age: {age}, height: {height}, weight: {weight}, iq: {iq}")

# a puzzle for the extra credit, type it anyway.
print("Here is a puzzle.")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("That becomes:", what, " Can you do it by hand?")

# ///////////////////////////////////////////////////////////////////////////////////////////////////
# ///////////////////////////////////////////////////////////////////////////////////////////////////

adding_and_subtract_a = int(input(" Please enter the first integer number: "))
adding_and_subtract_b = int(input(" Please enter the second integer number: "))
question_1 = input("Do you want to know an answer, if we will add this two numbers?")
answer = question_1


# Function subtracting
def subtract_a_b(adding_and_subtract_a, adding_and_subtract_b):
    return adding_and_subtract_a - adding_and_subtract_b


# Function adding
def adding_a_b(adding_and_subtract_a, adding_and_subtract_b):
    return adding_and_subtract_a + adding_and_subtract_b


if answer == "Yes":
    print("Let's do it, man!")
    print(f"If we add {adding_and_subtract_a} and {adding_and_subtract_b}, we will get:", adding_a_b(adding_and_subtract_a, adding_and_subtract_b))
elif answer == "yes":
    print("Let's do it, man!")
    print(f"If we add {adding_and_subtract_a} and {adding_and_subtract_b}, we will get:", adding_a_b(adding_and_subtract_a, adding_and_subtract_b))
elif answer == "of course":
    print("Let's do it, man!")
    print(f"If we add {adding_and_subtract_a} and {adding_and_subtract_b}, we will get:", adding_a_b(adding_and_subtract_a, adding_and_subtract_b))
elif answer == "no":
    print("Ok, man, then for you I will subtract these two numbers.")
    print(f"We subtract {adding_and_subtract_a} - {adding_and_subtract_b} and we will get:", subtract_a_b(adding_and_subtract_a, adding_and_subtract_b))
else:
    print("Ok, man, then for you I will subtract these two numbers.")
    print(f"We subtract {adding_and_subtract_a} - {adding_and_subtract_b} and we will get:", subtract_a_b(adding_and_subtract_a, adding_and_subtract_b))
