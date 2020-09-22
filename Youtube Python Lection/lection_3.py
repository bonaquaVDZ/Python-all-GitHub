x = 10
y = 5
list = [1, 2, "EROR", [3, 22, True], x+y, ("Mother", "father")]

print(list)
list[3][2] = False
print(list)
list.append(4444)
print(list)
list.insert(2, "CHANGED")
print(list)  # [1, 2, 'CHANGED', 'EROR', [3, 22, False], 15, ('Mother'...]


print("----------------------------------------------------------------------")
print(list[3][1])


print("----------------------------------------------------------------------")


print(list[3])
print(list[4])
print(list[5])


print("----------------------------------------------------------------------")


ab = int("AB", base=16)    # 10*16+11 = 171
ac = int("AC", base=16)    # 10*16+12 = 172
ad = int("AD", base=16)    # 10*16+13 = 173
ae = int("AE", base=16)    # 10*16+14 = 174
af = int("AF", base=16)    # 10*16+15 = 175
ff = int("FF", base=16)    # 15*16+15 = 255

print(ab)      # 171
print(ac)      # 172
print(ad)      # 173
print(ae)      # 174
print(af)      # 175
print(ff)      # 255


print("----------------------------------------------------------------------")


hex(1)        # hexadecimal number
oct(1)        # oct number


a = 10
b = a
print(b is a)       # True
a += 1
print(b is a)       # False


print("----------------------------------------------------------------------")


list_1 = range(1, 101, 1)
list_2 = []
for i in range(len(list_1)):
    if list_1[i] % 7 == 0:
        list_2.append(list_1[i])
        print(list_2)


print("----------------------------------------------------------------------")


# list_4 = [x for x in list_3 if x % ==9]
list_3 = range(1, 101, 1)
list_4 = []
for x in list_3:
    if x % 9 == 0:
        list_4.append(x)
        print(list_4)
