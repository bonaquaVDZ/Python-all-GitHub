# Open a file!
fo = open("ex20add.txt", "r+")
print("Name of the file: ", fo.name)

# Assuming file has folowing five lines.
# This is 1st line
# This is 2nd line
# This is 3rd line
# This is 4th line
# This is 5th line

# OUR FILE IS
# Python is perfect!
# Python is a great language!
# Welcome to Python!!!
# Python is one of the best!
# I love python!

line = fo.readline()
print("Read line 1: %s" % (line))       # Python is perfect!

# Again set the pointer to the beginning
fo.seek(0, 0)
line = fo.readline()
print("Read line 2: %s" % (line))       # Python is perfect!

line = fo.readline()
print("Read line 3: %s" % (line))       # Python is a great language!

line = fo.readline()
print("Read line 4: %s" % (line))       # Welcome to Python!!!

fo.seek(23, 0)
line = fo.readline()
print("Read line 5: %s" % (line))       # Python is a great language!

line = fo.readline()
print("Read line 6: %s" % (line))       # Python is one of the best!

fo.seek(111, 0)
line = fo.readline()
print("Read line 7: %s" % (line))       # I love python!

# Close opend file
fo.close()


# % s is used as a placeholder for string values you want to inject into a formatted string.
# % d is used as a placeholder for numeric or decimal values
