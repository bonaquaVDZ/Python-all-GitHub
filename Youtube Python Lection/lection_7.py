class Goat:
    "age, nickname and weight are attributes"

    nickname = ""
    age = 3
    weight = 0.0

    def show(self):     # (self) - compulsory. Reference to object for which this method is called.
        "Class methods"
        print(self.nickname)
        print(self.age)
        print(self.weight)


a = Goat()
a.nickname = "Marusia"
a.age = 2
a.weight = 35

b = Goat()
b.nickname = "Klara"
b.age = 5
b.weight = 33
a.show()
b.show()


print("------------------------------------------------------------------------------------------------------------------------")
print("------------------------------------------------------------------------------------------------------------------------")


class Student_lec:
    def __init__(self, name, age, arrears):     # Constructor
        self.name = name
        self.age = age
        self.arrears = arrears
        print(name, "+", arrears)


stud_1 = Student_lec("Vadzim", 25, "Physics")
stud_2 = Student_lec("Julia", 22, None)
stud_3 = Student_lec("Arhip", 16, None)

print("------------------------------------------------------------------------------------------------------------------------")
print("------------------------------------------------------------------------------------------------------------------------")


class Student:
    def __init__(self, name, surname, age, city, specialty):
        self.name = name
        self.surname = surname
        self.age = age
        self.city = city
        self.specialty = specialty
        print(">>>> ", name, surname, age, city, specialty)


stud_1 = Student("Vadzim", "Ramaniuk", 25, "Warsaw", "Economics")
stud_2 = Student("Julia", "Kravchuk", 22, "Warsaw", "Management")


print("---------------------------------------------------------------------------------------------------------------------")
print("---------------------------------------------------------------------------------------------------------------------")


class Monkeys:
    species = ""
    age = 0
    habitat = ""
    weight = 0.0

    def addition_all_inf(self):
        print(">>>> ", self.species, self.age, self.habitat, self.weight)


type_1 = Monkeys()
type_1.species = "Grivet"
type_1.age = 12
type_1.habitat = "Jungle"
type_1.weight = 45
type_1.addition_all_inf()

type_2 = Monkeys()
type_2.species = "The rhesus macaque"
type_2.age = 15
type_2.habitat = "Forest"
type_2.weight = "38 kg"
type_2.addition_all_inf()
