def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses.")
    print(f"You have {boxes_of_crackers} boxes of crackers. ")
    print("Man that's enough for the party.")
    print("Get a blanket.\n")


print("We can just give the functions numbers directly:")
cheese_and_crackers(30, 20)


print("Or, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 33
cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print("We can even do math inside too:")
cheese_and_crackers(23 + 53, 21 * 2)


print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese * 2, amount_of_crackers + 27)


cheese_count_1 = int(input("Please enter the number of KG, how much cheese do you want? "))
boxes_of_crackers_1 = int(input("Enter, how many boxes of crackers do you need?"))
cheese_and_crackers(cheese_count_1, boxes_of_crackers_1)


def add(x, y):
    return x + y


print(add(5, 12))


def multiply(m, r):
    return m * r


print(multiply(add(2, 30), 3))
