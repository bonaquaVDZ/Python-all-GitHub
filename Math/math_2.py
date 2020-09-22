# Mathematical functions
import math
prompt = ">>>>"

# NUMBER-THEORETIC AND REPRESENTATION FUNCTIONS.

# Return the ceiling of x, the smallest integer greater than or equal x.
print(prompt, "math.ceil(x) =", math.ceil(3.14))                # 4
print(prompt, "math.ceil(x) =", math.ceil(-3.14))               # -3
print(prompt, "int(434).__ceil__() =", int(434).__ceil__())     # 434 , only integer, not a float.


# n! / (k!* (n - k)!) "Without repetion and without order"
print(prompt, "math.comb(n, k) =", math.comb(4, 3))         # 4


# Return a float with the absolute value of x but the sign of y.
print(prompt, "math.copysign(x, y) =", math.copysign(5, 2))         # 5.0


# Return the absolut value of x.
print(prompt, "math.fabs(x) =", math.fabs(-6.28))           # 6.28


# Return x factorial as an integer.
print(prompt, "math.factorial(x) =", math.factorial(4))     # 24


# Return the floor of x, the largest integer less than or equal to x. If x is not a float, delegates to x.__floor__(), which should return an integral value.
print(prompt, "math.floor(x) =", math.floor(-3.14))          # -4
print(prompt, "math.floor(x) =", math.floor(3.14))           # 3
print(prompt, "math.floor(x) =", math.floor(3.54))           # 3
print(prompt, "math.floor(x) =", math.floor(-3.54))          # -4
print(prompt, "int(x).__floor__() =", int(323).__floor__())  # 323


# This function is generally preferred when working with floats. Python's x % y is preferred when working with integers.
print(prompt, "math.fmod(x, y) =", math.fmod(math.pi, 1))   # 0.14159265358979312
print(prompt, "math.fmod(x, y) =", math.fmod(10, 3))        # 1.0
print(prompt, 10 % 3)                                       # 1


# Return the mantissa and exponent of x as the pair (m, e). m - is a float and e is an integer such that x == m*2**e
print(prompt, "math.frexp(x) =", math.frexp(2))     # It is incomprehensible. # (0.5, 2)
print(prompt, "math.frexp(x) =", math.frexp(4))     # It is incomprehensible. # (0.5, 3)
print(prompt, "math.frexp(x) =", math.frexp(5))     # It is incomprehensible. # (0.625, 3)


# Return the accurate floating point sum of values in the iterable.
print(prompt, "math.fsum([x,y..]) =", math.fsum([2, 4, 6, 8, 3.14159]))
print(prompt, "math.fsum([x,y..]) =", math.fsum([.1, .1, .1, .1]))
print(prompt, "math.fsum([x,y..]) =", math.fsum([.1, .1, .8, .3]))


# Return the greatest common divisor of the integers a and b.
print(prompt, "math.gcd(a, b) =", math.gcd(3, 6))
print(prompt, "math.gcd(a, b) =", math.gcd(12, 1200))


# Return True if the values a and b are close to each other and False otherwise.
print(prompt, "math.isclose(a, b, *, rel_tol = 0.000000001, abs_tol = 0) =", math.isclose(12, 15, abs_tol=3))           # True
print(prompt, "math.isclose(a, b, *, rel_tol = 0.000000001, abs_tol = 0) =", math.isclose(12, 12.01, rel_tol=0.0001))   # False
print(prompt, "math.isclose(a, b, *, rel_tol = 0.000000001, abs_tol = 0) =", math.isclose(12, 12.000000001))            # True


# Return True if x is neither an infinity nor NaN, and False otherwise.
print(prompt, "math.isfinite(x) =", math.isfinite(6))           # True
print(prompt, "math.isfinite(x) =", math.isfinite(6.28318))     # True
print(prompt, "math.isfinite(x) =", math.isfinite(math.pi))     # True
print(prompt, "math.isfinite(x) =", math.isfinite(math.tau))    # True
print(prompt, "math.isfinite(x) =", math.isfinite(math.nan))    # False


# Return True if x is a positive or negative infinity, and False otherwise.
print(prompt, "math.isinf(x) =", math.isinf(1))                # False
print(prompt, "math.isinf(x) =", math.isinf(3.14))             # False
print(prompt, "math.isinf(x) =", math.isinf(-2))               # False
print(prompt, "math.isinf(x) =", math.isinf(math.e))           # False
print(prompt, "math.isinf(x) =", math.isinf(math.inf))         # True


# Return True if x is a NaN (not a number), and False otherwise.
print(prompt, "math.isnan(x) =", math.isnan(1))                # False
print(prompt, "math.isnan(x) =", math.isnan(math.nan))         # True


# Return the integer square root of the nonnegative integer "n". This is the floor of the exact square root of "n" or equivalently the greatest integer.
print(prompt, "math.isqrt(n) =", math.isqrt(64))               # 8
print(prompt, "math.isqrt(n) =", math.isqrt(82))               # 9
print(prompt, "math.isqrt(n) =", math.isqrt(8))                # 2


# Return x * (2 ** i). This is essentially the inverse of function frexp()
print(prompt, "math.ldexp(x, i) =", math.ldexp(3, 3))          # 24.0
print(prompt, "math.ldexp(x, i) =", math.ldexp(100, 4))        # 1600


# Return the fractional and integer parts of x. Both results carry the sign of x and are floats.
print(prompt, "math.modf(x) =", math.modf(math.pi))        # (0.14159265358979312, 3.0)
print(prompt, "math.modf(x) =", math.modf(math.tau))       # (0.28318530717958623, 6.0)
print(prompt, "math.modf(x) =", math.modf(math.e))         # (0.7182818284590451, 2.0)


# n! / (n - k)! " Without repetition and with order"
print(prompt, "math.perm(n, k =None) =", math.perm(5))      # 120
print(prompt, "math.perm(n, k =None) =", math.perm(5, 3))   # 60
print(prompt, "math.perm(n, k =None) =", math.perm(36, 8))  # 1220096908800


# Calculate the product of all the elements in the input iterable. The default start value for the product is 1.
print(prompt, "math.prod(iterable,*, start = 1) =", math.prod([1, 3, 5]))        # 15
print(prompt, "math.prod(iterable,*, start = 1) =", math.prod([1, 3, 5, 7]))     # 105
print(prompt, "math.prod(iterable,*, start = 1) =", math.prod((2, 4)))           # 8


# Return the remainder of x with respect of y.
print(prompt, "math.remainder(x, y) =", math.remainder(10, 9))      # 1.0
print(prompt, "math.remainder(x, y) =", math.remainder(4, 6))       # -2.0
print(prompt, "math.remainder(x, y) =", math.remainder(10, 7))      # 3.0
print(prompt, "math.remainder(x, y) =", math.remainder(100, 96))    # 4.0


# Return the Real value x truncated to an integral (usually an integer).
print(prompt, "math.trunc(x) =", math.trunc(6.28))          # 6
print(prompt, "math.trunc(x) =", math.trunc(math.pi))       # 3
print(prompt, "math.trunc(x) =", math.trunc(math.e))        # 2


# Return e raised to the power x, where e = 2.718281... is the base of natural logarithms.
# This is usually more acurate that math.e ** x or pow (math.e, x)
print(prompt, "math.exp(x) =", math.exp(2))     # 7.38905609893065
print(prompt, "math.exp(x) =", math.exp(3))     # 20.085536923187668
