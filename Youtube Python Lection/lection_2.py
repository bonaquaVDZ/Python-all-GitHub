number_1 = int(input(">>>> Print any number:"))
x = number_1    # START/STOP/STEP

while x > 0:    # ITERATION # STOP
    x += 1      # The circularity or looping. STEP
    print(x, end=",")

    if x == 17:
        print("\n>>> ", number_1, "is the number between 0 and 17")
        break
    elif x == 100:
        print(number_1, "is the number between 17 and 100")
        break
    elif x == 1000:
        print(number_1, " is the number between 100 and 1000")
        break
else:
    print(f"{number_1} is negative number")


print("-----------------------------------------------------------------")


for y in range(0, 6):
    print(y, "WOW", end="\n")


print("-----------------------------------------------------------------")


for OP in ('Customer', 'Kunde'):
    print(OP * 2)


print("-----------------------------------------------------------------")

numb_start = 1  # Start
while numb_start < 101:     # stop
    print(numb_start, end=",")
    numb_start += 1     # STEP

print("\n-----------------------------------------------------------------")

for numb_start in range(1, 10, 2):
    print("LOOP FOR", numb_start)

print("\n-----------------------------------------------------------------")


def add(x: "int > 0", y: "int > 0", z: "0 < int < 5") -> int:
    "addition x and y and z"
    return x + y + z


print("The answer of function is:", add(2, 3, (add(-1, 2, 25))))
print(type(add))

print("\n-----------------------------------------------------------------")
sentence = "I would like to describe, how could you \
write the enormous huge sentence with the \
special symbol (backslash) \\ ."
print(sentence)
print("\n-----------------------------------------------------------------")
