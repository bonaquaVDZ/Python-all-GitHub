
from sys import argv
script, filename_1, filename_2, filename_3 = argv


txt_1 = open(filename_1)
txt_2 = open(filename_2)
docx = open(filename_3)


print(f"Here is your the first file {filename_1}")
print(txt_1.read())

print(f"Here is your the se'pcond file {filename_2}")
print(txt_2.read())

print(f"The third file in docx format {filename_3}")
print(docx.read())


print("-----------------------------------------------------------------------------------------------------------")
print("-----------------------------------------------------------------------------------------------------------")


filename_1_txt = input("Please write it down the first file.txt: ")
text_again_1 = open(filename_1_txt)

print(text_again_1.read())    # In the bracets after .read(), you can enter any numerical parameters.


print("-----------------------------------------------------------------------------------------------------------")


filename_2_txt = input("Please write it down the second file.txt: ")
text_again_2 = open(filename_2_txt)

print(text_again_2.read())


print("-----------------------------------------------------------------------------------------------------------")


filename_3_txt = input("The third name of the file.docx: ")
docx_1 = open(filename_3_txt)

print(docx_1.read())


print(text_again_1.close())
