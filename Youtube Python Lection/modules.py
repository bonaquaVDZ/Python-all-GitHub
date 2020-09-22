import pickle       # pickle.dump(a,b) # pickle.load(...)
import time         # time.asctime() # time.localtime() # time.sleep()
import sys          # sys.version
import keyword      # keyword.iskeyword("...")
import copy         # copy.copy (...)
import random       # random.randint(a,b)


class Auto():
    pass


my_auto1 = Auto()
my_auto1.wheels = 4

my_auto2 = copy.copy(my_auto1)  # Replicate the value of my_auto.wheels
my_auto2.wheels = 8

my_auto3 = copy.copy(my_auto1)
my_auto3.wheels = 16

my_auto4 = Auto()
my_auto4.wheels = 32

print(my_auto1.wheels)  # 4
print(my_auto2.wheels)  # 8
print(my_auto3.wheels)  # 16
print(my_auto4.wheels)  # 32


print("." * 100)
print("." * 100)


# import keyword
print(keyword.iskeyword("if"))      # True
print(keyword.iskeyword("asad"))    # False
print(keyword.iskeyword("class"))   # True
print(keyword.iskeyword("def"))     # True


print("." * 100)
print("." * 100)


# import random
# random.randint(a,b)
print("Random numbers from 0 to 100: ", random.randint(0, 100))
print("Random numbers from 1 to 10: ", random.randint(1, 10))
print("Random numbers from -30 to -10: ", random.randint(-30, -10))


print("." * 100)
print("." * 100)


# random.choice(list)
list_1 = ["AUDI", "MERS", "BMW", "RENO"]
print(random.choice(list_1))


print("." * 100)
print("." * 100)


# Game with Random
num = random.randint(0, 10)
while True:
    print("Enter number from 0 to 10: ")
    num1 = int(input())
    if num1 == num:
        print("You guessed it")
        break
    else:
        print("You did't guess")
    if num1 == 100:                      # Print 100 to know the hidden number.
        print("Mystery number %s" % num)     # (%s % num) is 100 = random (num)


print("." * 100)
print("." * 100)


# Import sys
in1 = sys.stdin.readline()
in2 = sys.stdout.write(in1)
# sys.exit()    # Close the programm.
print(in1)
print(sys.version)  # To know the version of python.


print("." * 100)
print("." * 100)


# Import time
print(time.time())
print(time.asctime())
print(time.localtime())

print("." * 100)

t1 = time.localtime()
t2 = time.asctime()
print("TIME RIGHT NOW:", t2, "\nYear:", t1[0], "\nMonth:", t1[1],
      "\nDay:", t1[2])
print("DAY IN YEAR:", t1[7])

for i in range(0, 10):
    print(i)
    time.sleep(1)

print("." * 100)
print("." * 100)

# import pickle
# CREATE AND CLOSE FILE.
game = {"Life": 123, "Armor": 200, "Level": 300}
file1 = open("test.txt", "wb")
pickle.dump(game, file1)
file1.close()


# OPEN FILE TEST.TXT
load_file = open("test.txt", "rb")
loaded = pickle.load(load_file)
load_file.close()
print(loaded)


print("." * 100)


# OPEN MY SPORTFILE
sport = {"Baseball": 10, "footbal": 100}
sport_file = open("sport.txt", "wb")
pickle.dump(sport, sport_file)
sport_file.close()


# OPEN TEST_TEXT_TRIAL.TXT
load_sportfile = open("sport.txt", "rb")
loaded_1 = pickle.load(load_sportfile)
load_sportfile.close()
print(loaded_1)
