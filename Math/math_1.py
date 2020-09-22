# https://stackabuse.com/the-python-math-library/

# SPECIAL CONSTANTS
# Pie
# Pie denotes the ratio of circumference to diameter of a circle and it has a value of 3.141592653589793
import math
print(">> TA1 PIE is:", math.pi)

# You can use this constant to calculate the area of circumference of a circle.
radius = 3
diametr = 2 * radius                # D = 2r
area = math.pi*radius*radius        # A = πr²
circumference = 2*math.pi*radius    # Circle = 2πr

print(">> TA3:", f"The DIAMETR with a radius '{radius}' is = %.2f" % diametr)
print(">> TA4:", f"The AREA with a radius '{radius}' is = % .5f" % area)
print(">> TA5:", f"The CIRCUMFERENCE with a radius '{radius}' is = % .5f" % circumference)


print("---------------------------------------------------------------------------------------------------------------")
print("---------------------------------------------------------------------------------------------------------------")

# Python Programm to Calculate Diametr Area Circumference of a circle


def find_diametr(radius_1):
    return 2 * radius_1


def find_area(radius_1):
    return math.pi*radius_1*radius_1


def find_circumference(radius_1):
    return 2 * math.pi * radius_1


r = float(input(">> TA6: Please Enter radius of a circle: "))
diametr_of_circle = find_diametr(r)
area_of_circle = find_area(r)
circumference_of_circle = find_circumference(r)

print("\nDiametr of a circle is =% .2f" % diametr_of_circle)
print("The area of a circle is =% .2f" % area_of_circle)
print("The circumference of a circle is =% .2f" % circumference_of_circle)


print("---------------------------------------------------------------------------------------------------------------")
print("---------------------------------------------------------------------------------------------------------------")


# Euler's number
print(">> TA7: Euler's number is:", math.e)

print("---------------------------------------------------------------------------------------------------------------")
print("---------------------------------------------------------------------------------------------------------------")

# Exponents and Logarithms
# The exp() Function
# The Python math library comes with the exp() function that we can use to calculate the the power of e.
# The value of "e" is 2.718281828459045.
# The parameter "x" can be a positive and negative number.If x is not a number, the method will return an error.
a_int = 10
a_neg_int = -8
a_float = 2.15
print(">> TA8:", math.exp(a_int))
print(">> TA9:", math.exp(a_neg_int))
print(">> TA10:", math.exp(a_float))

# We can also apply this method to inbuilt constants as demonstrated below.
print(">> TA11:", math.exp(math.e))
print(">> TA12:", math.exp(math.pi))

print("---------------------------------------------------------------------------------------------------------------")
print("---------------------------------------------------------------------------------------------------------------")

# The log() function
# This function returns the logarithm of the specified number.
# The natural logarithm is computed with the respect to the base "e".
print(">> TA13: log (100)=", math.log(100))


# The log10() function
# This method returns the base-10 logarithm of specified number.
print(">> TA14: log10(100)=", math.log10(100))

# The log2() function
# This function calculates the base-2 logarithm.
print(">> TA15: log2(32)=", math.log2(32))

# The log(x,y) function
# This function returns the logarithm of "x" with "y" being the base.
print(">> TA16: log(16,2)=", math.log(16, 2))
print(">> TA17: log(27,3)=", math.log(27, 3))
print(">> TA18: log(9,3)=", math.log(9, 3))
print(">> TA19: log(81,81)=", math.log(81, 81))
print(">> TA20: log(1)=", math.log(1))

print("---------------------------------------------------------------------------------------------------------------")
print("---------------------------------------------------------------------------------------------------------------")


# Arithmetic function
# Arithmetical functions are used to represent numbers in various forms and perform math operations on them.
# Some of the most common arithmetic functions are discussed below.

# ceil(): returns the ceiling value of the specified number.
# fabs(): returns the absolute value of the specified number.
# floor(): returns the floor value of the specified number.
# gcd(a, b): returns the greatest common divisor of a and b.
# fsum(iterable): returns the sum of all elements in an iterable objects.
# pow(): takes two float arguments and raises the first argument to the second argument and returns the result.
# sqrt(): returns the square root of the specified number.

num_1 = 3.14
num_2 = -3.14
num_3 = 15
num_4 = 30
num_5 = 9
num_6 = 2
list_for_sum = [12, 34, 27, 100, 1.3768]

print(f">> TA21: The ceiling of {num_1} = ", math.ceil(num_1))
print(f">> TA22: The ceiling of {num_2} = ", math.ceil(num_2))

print(f">> TA23: Absolute value of {num_2} = ", math.fabs(num_2))

print(f">> TA24: The floor value of {num_1} = ", math.floor(num_1))
print(f">> TA25: The floor value of {num_2} = ", math.floor(num_2))

print(f">> TA26: The greatest common divisor for {num_3} and {num_4} is", math.gcd(num_3, num_4))

print(f">> TA27: Summation of the {list_for_sum} = ", math.fsum(list_for_sum))

print(f">> TA28: Raise to the {num_6} power the numb {num_5} = ", math.pow(num_5, num_6))

print(f">> TA29: The square root of {num_5} = ", math.sqrt(num_5))


print("---------------------------------------------------------------------------------------------------------------")
print("---------------------------------------------------------------------------------------------------------------")


# Trigonometric functions
# The Python Math module supports all Trigonometric functions. Some of them have been enlisted below.
# math.sin(a): returns the sine of "a" in radians.
# math.cos(a): returns the cosine of "a" in radins.
# math.tan(a): returns the tangent of "a" in radians.
# math.asin(a): returns the inverse of sin. Also, "acos", "atan".
# math.degrees(a): converts the angle "a" from radian to degrees.
# math.radians(a): converts the angle "a" from degrees to radian.
# Consider the following example.

angle_in_degrees = 90
angle_in_radians = math.radians(angle_in_degrees)

print(">> TA30: The value of the angle is:", angle_in_radians)
print(">> TA31: sin(x) is", math.sin(angle_in_radians))
print(">> TA32: cos(x) is", math.cos(angle_in_radians))
print(">> TA33: tan(x) is", math.tan(angle_in_radians))
# Note that we fisrt converted the value of the angle from degrees to radians before performing other operations.
