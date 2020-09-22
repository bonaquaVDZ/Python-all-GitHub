# open/read/rewrite the file
# we will change here the pdf-file.
from sys import argv, exit
script, filename = argv

pdf_file = open(filename, "r")
print(pdf_file.read())

pdf_file = open(filename, "w")
line1 = input("Line 1: ")
line2 = input("Line 2: ")

pdf_file.write("I can write any text here and this text will be showed in our file!\n")
pdf_file.write(f"{line1}\n{line2}\n")   # It is much more compact, than writing 4 lines. One line instead of four or more.

pdf_file.close()
