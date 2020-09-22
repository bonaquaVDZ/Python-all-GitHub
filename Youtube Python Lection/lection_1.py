import math

x = y = z = 0
a, b, c = 1, 2, 3
print(x, y, z)
print(a, b, c)

i = 1
j = 3
i, j = j, i

print(i)
print(j)

print(9**0.5)  # Answer 3.0
print(2**2**2)  # Answer 16


abc = 12 % 5
print(abc)

print(-12//10)  # Answer -2
print(-12 % 10)  # Answer 8
print(12//10)  # Answer 1
print(12 % 10)  # Answer 2

j = j+1
m = j
m += 1+i
print(j)
print("Print m:", m)

abcd = 100
abcd = abcd - 10  # The same like "abcd -= 10"
abcd -= 10
print(abcd)  # Answer = 80
abcd /= 2
print(abcd)  # Answer = 40.0
abcd *= 3
print(abcd)  # Answer = 120.0
abcd += 60
print(abcd)  # Answer = 180.0
abcd //= 2.1
print(abcd)  # Answer = 85

for xy in 1, 5, 2, 4, 8:
    print(xy**2, end=",")  # Answer = 1,25,4,16,64, 0.5


#  range (start,stop,step)
for xyz in range(1, 11, 2):
    print(xyz / 2)

for zyx in range(10, 1, -1):
    print(zyx)

print("----------------------------------------------------------------------")

# help(print)
arm = 15
leg = 12
body = 140
print(arm, leg, body, sep=":")
print("----------------------------------------------------------------------")


formatting = '{:,.2f}'.format(232642427)
print(formatting)
print("----------------------------------------------------------------------")

print("%2d:%2d:%2d" % (arm, leg, body))
print("%11d:%11d:%11d:" % (arm, leg, body))

print("----------------------------------------------------------------------")


# Import math

print(math.pi)
print(math.sin(math.pi))
print(math.cos(90))
print(math.cos(180))
print(math.tan(90))
print(math.tan(1))
print(math.sqrt(81))    # 9.0
print(81**0.5)      # 9.0
print(2**2**2)      # 16
print(2**2**2 == 2**4)  # True
print(2+2 != 5)   # True

print("----------------------------------------------------------------------")

print(">>>> What is your name? ")
name = input("---> ")
print(">>>> I am glad to hear you, " + name + ".")
print(">>>> I would like to know, how old are you, " + name + "?")
age = int(input("---> "))
print(">>>> Wow, I thought that you", age + 1, "years old!")
print(f">>>> Ok, {name}. Could you say, where are you from? ")
city = input("---> ")
print(f">>>> Wow, I was also in {city}.")

print("----------------------------------------------------------------------")

print("Сколько тебе лет, " + name)
age_1_rus_v = int(input("---> "))
print("А я думал, что тебе", age_1_rus_v + 1, end=" ")
x = age_1_rus_v + 1
if 11 <= x <= 19:
    print("лет!")
elif x % 10 == 1:
    print("год!")
elif x % 10 >= 2 and x % 10 <= 4:
    print("года!")
else:
    print("лет!")

print(21 % 10)
