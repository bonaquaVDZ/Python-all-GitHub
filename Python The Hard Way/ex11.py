print("How old are you?", end=" ")
age = input()
print("How tall are you?", end=" ")
height = input()
print("How much do you weigh?", end=" ")
weight = input()

print(f"So, you're {age} old, {height} tall, {weight} heavy.")
print("." * 100)


name = input("What is your name? ")
surname = input("What is your surname? ")
residence = input("Where are you living right now? ")
print(f"""The whole information is:
\t\t\t* Your name is {name}.
\t\t\t* Your surname is {surname}.
\t\t\t* You live in {residence}.""")
print("." * 100)


exp_1 = int(input("Could you calculate 2+2? Print please the answer: "))
incorrect = False
if exp_1 == 4:
    print("Yes, exactly, 2+2=4")
else:
    print(f"It is {incorrect}, try it again.")
