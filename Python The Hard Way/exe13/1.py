from sys import argv

script, argv_1, argv_2, argv_3 = argv

argv_1 = input("Print please the first arguments: ")
argv_2 = input(f"Thanks for '{argv_1}'. Print the second: ")
argv_3 = input(f"Thanks for '{argv_1}' and '{argv_2}'. Insert the third: ")


print("Our script is: ", script)
print("Our argument_1:", argv_1)
print("Our argument_2:", argv_2)
print("Our argument_3:", argv_3)
