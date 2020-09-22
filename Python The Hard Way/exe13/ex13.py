# Parameters, Unpacking, Variables
from sys import argv
# Read thwe WYSS section for how ti run this.
script, first, second, third = argv     # Unpacks argv
# You can actually replace first,second,third and fourth with another things.
# Argv is argument variables.
fourth = input("Enter the fourth value: ")

print(">>>> argv:", repr(argv))

print("The script is called   :", script)
print("Your first variable is :", first)
print("Your second variable is:", second)
print("Your third variable is :", third)
print("Your fourth variable is:", fourth)

# In PowerShell you must path three command line arguments.
# Run the programm like this: python ex13.py first 2nd 3rd 4th
# Or run like: python ex13.py X Y Z Q
exit(argv)
