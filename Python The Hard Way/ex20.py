from sys import argv, exit
script, input_file = argv


# Function 1
def print_all(f):
    "Give us the possibilities to read a file."
    print(f.read())


# Function 2
def rewind(f):
    f.seek(0)


# Function 3
def print_a_line(line_count, f):
    print(line_count, f.readline(0))


current_file = open(input_file)

print("First lets print the whole file:\n")

# We call the first function!
print_all(current_file)

print("Now let's rewind, kind of like a tape.")

# We call the second function!
rewind(current_file)

print("Let's print three lines:")

# Further we call the third function three times.
current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
