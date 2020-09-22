from sys import argv
script, filename = argv

print("Opening the file...")
target = open(filename, "w")

print("Truncating the file...")
target.truncate()

print("Rewriting the file...")
line1 = input("Print something in the first line: ")
target.write(line1)
target.write("\nWow, i can write here!")
target.write("\nWow, i can write here!")
target.write("\nWow, i can write here!")
target.write("\nWow, i can write here!")

print("Closing the file...")
target.close()
