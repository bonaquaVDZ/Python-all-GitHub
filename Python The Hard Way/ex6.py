types_of_people = 10
x = f"There are {types_of_people} types of people."

binary = 'binary'
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)

print(f" I said: {x}")
print(f" I also said: '{y}'")

hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"
print(joke_evaluation.format(hilarious))

numb = float(12.3456)
ask_1 = "How high is your number? {}"
print(ask_1.format(numb))


w = "This is the left side of..."
e = "a string with a right side."
print(w+e)  # We add two variables with different strings.
