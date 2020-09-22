import math
# this one is like your scripts with argv


def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")


# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")


# this just takes one argument
def print_one(arg1):
    print(f"arg1: {arg1}")


# this one takes no arguments
def print_none():
    print("I got nothin' .")


def addition_and_product(*args):
    val_a, val_b, val_c, val_d = args
    x = val_a + val_b
    y = val_b + val_c
    z = val_b * val_c
    a = 10
    b = math.pi
    print("Adding of val_a and val_b = ", x)
    print("Adding of val_b and val_c = ", y)
    print("Product of val_b and val_c = ", z)
    print("Product of 10 and number pie = ", a * b)


def product_of_two_arg(n1, n2):
    x = n1
    y = n2
    return x * n1 * y


def product(*args):
    a, r, o = args
    return a * r * o * 2


print_two("Vadzim", "Ramaniuk")
print_two_again("Julia", "Kravchuk")
print_one("It is one argument. Sorry! ")
print_none()
addition_and_product(1, 2, 3, 4)
print("Product of two different arguments =", product_of_two_arg(11, 11))
print("Product of a,r,o and 2 = ", product(1, 3, 2))
