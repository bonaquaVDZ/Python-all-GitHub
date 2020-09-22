# This file can open/truncate/write/close.
# The main idea is to create a new file and enter some information there.
# With this code you can create a new file and fill up it, or open early existed file and change him.
# Try to use this code for two various reasons.
from sys import argv
script, filename = argv

print(f"I am going to erase {filename}")
print("If you don't want that, hit CTRL-C (^C). ")
print("If you do want that, hit RETURN.")

input("?")


# Create a new file with the name "target" and after that we truncate it and enter necessary data.
print("Opening the file...")
target = open(filename, "w")    # Symbol "w" has value "write".


# If you are going to truncate a file, you need to put before into the brackets letter "w"! It is important!
print("Truncating the file. Goodbye.")
target.truncate()               # The whole file will be deleted.


print("Now, I am going to ask you for three lines.")

line1 = input("Line 1: ")
line2 = input("Line 2: ")
line3 = input("Line 3: ")

print("I am going to write these lines to the file.")    # Right now, we can write down new information in this file.

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally, we close it!")
target.close()      # Finally, we close this file and you can see him in the same directory as this file ex16.def
