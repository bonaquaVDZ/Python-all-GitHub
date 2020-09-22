# If we write "I "understand" Joe."
# Then Python will get confused because it will think the double-qoute...
# around "understand" actually ends the string.
print("_" * 100)
print("I am 6'2\" tall.")   # Escape double-quote inside string.
print('I am 6\'2" tall.')   # Escape single-quote inside string.
print("." * 100)


tabby_cat = "\tI'am tabbed in."
persian_cat = "I'am split\n on a line."
backslash_cat = "I'am \\ a \\ cat."
print(tabby_cat)
print("." * 100)
print(persian_cat)
print("." * 100)
print(backslash_cat)
print("." * 100)

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip
\t* Grass
"""
print(fat_cat)
print("." * 100)

my_fat_cat = """I'll do a list:\n\t* Cat food\n\t* Fishies\n\t* Catnip
\t* Grass
"""
print(my_fat_cat)
print("." * 100)


string_1 = "\aMot\aher\a"   # \a with bell or signal. Here is 3 signal.
print(string_1)

string_2 = "F\bat\bher\b"   # Answer will be "aher". \b - backspace.
print(string_2)

string_3 = "\fBrot\fher\f"  # Answer "♀rot♀er♀"
print(string_3)

string_4 = "S\rister"   # Answer ister. \r - carriage return.
print(string_4)
print("." * 100)


# New code with format strings and escape characters.
escape = "\nAh!\nHow\nMany\nNew\nLines\nIn\nThis\nList: {}"
print(escape.format("\n\tLoads!\n\tAnd some more"))
