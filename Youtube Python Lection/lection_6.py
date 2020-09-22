objects = []


def create_object(name):
    objects.append("object[" + name + "]")


def print_object():
    print("All added objects")
    for obj in objects:
        print(obj)


def function_addition(x, y, z):
    return x*2 + y*2 + z*3


print(function_addition(1, 2, 3))


print("---------------------------------------------")
list = [33, 44, ["EROR", "not EROR"], 123]
print(list)

print("---------------------------------------------")

if __name__ == "__main__":
    print("This file is MAIN!")
