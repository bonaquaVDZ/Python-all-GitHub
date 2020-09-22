dict_1 = {1: "one", 2: "two", 3: "three"}   # {1: 'one', 2: 'two', 3: 'three'}
dict_2 = dict(short=2, longer=4)            # {'short': 2, 'longer': 4}
dict_3 = dict([(1, 33), (2, 44)])           # {1: 33, 2: 44}
dict_4 = dict.fromkeys([1, 2, 3], ["some", "any"])  # {1: ['some', 'any'], 2: ['some', 'any'], 3: ['some', 'any']}
dict_5 = dict.fromkeys([1, 2, 3, 4, 5])     # {1: None, 2: None, 3: None, 4: None, 5: None}
dict_6 = {a: a ** 2 for a in range(7)}      # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36}

print(dict_1)
print(dict_2)
print(dict_3)
print(dict_4)
print(dict_5)
print(dict_6)


person_inf = {'name': {'last_name': 'Ramaniuk', 'first_name': 'Vadzim', 'middle_name': 'Vitalievich'},
              'adress': ['pr. Nezavisimosti', 'd.168', 'kv 68 g. Minsk'],
              'phone': {'home_phone': '3456778'}}
print(person_inf)
print(person_inf['name']['last_name'])      # Ramaniuk
print(person_inf['name']['first_name'])     # Vadzim
print(person_inf['name']['middle_name'])    # Vitalievich
print(person_inf['adress'][0])              # pr. Nezavisimosti
print(person_inf['adress'][2])              # kv 68 g. Minsk
print(person_inf['phone']['home_phone'])    # 3456778

# Dictionary tools
# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# dict.items() method returns a view object that displays a list of a given dictionary's (key, value) tuple pair.
dic1 = {"Mother": 33, "Father": 43}
print(dic1.items())     # dict_items([('Mother', 33), ('Father', 43)])

# How items() works when a dictionary is modified?
items = dic1.items()
print("Original dic1:", items)

# delete an item from a dictionary
del[dic1["Mother"]]
print("Updated dic1 without one argument:", items)

# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# dict.keys()
dictionary_1 = {"Stop": "red", "Go": "green"}
print(dictionary_1.keys())      # dict_keys(['Stop', 'Go'])

# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# dict.values()
dictionary_1 = {"Stop": "red", "Go": "green"}
print(dictionary_1.values())    # dict_values(['red', 'green'])

# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# dict.popitem() this method removes and returns the last element (key, value) inserted into the dictionary
dictionary_1 = {"Stop": "red", "Go": "green", "Slowly go": 'yellow'}
print(dictionary_1.popitem())    # ('Slowly go', 'yellow')
print(dictionary_1)              # {'Stop': 'red', 'Go': 'green'}

person = {'name': 'Phill', 'age': 22, 'salary': 3500.0}

# ('salary', 3500.0) is inserted at the last, so it is removed.
result = person.popitem()

print('Return Value = ', result)    # Return Value =  ('salary', 3500.0)
print('person = ', person)          # person =  {'name': 'Phill', 'age': 22}

# inserting a new element pair
person['profession'] = 'Plumber'
print('person = ', person)          # person =  {'name': 'Phill', 'age': 22, 'profession': 'Plumber'}

# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# dict.setdefault(key[,default_value]) method returns the value of a key (if the key is in dictionary). If not, it inserts key with a value to the dictionary.
dictionary_1 = {"Stop": "red", "Go": "green", "Slowly go": 'yellow', "Numb Pie": 3.14159}

go = dictionary_1.setdefault("Go")
print("Go =", go)   # Go = green

print(dictionary_1.setdefault("Stop"))  # red
print(dictionary_1.setdefault("Numb Pie"))  # 3.14159

# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# dict.update ([other]) method updates the dictionary with the elements from the another dictionary object or from an iterable of key/values pair.
someone = {'name': 'Phill', 'age': 22, }

print('Before dictionary is updated')
keys = someone.keys()
print(keys)         # dict_keys(['name', 'age'])

# adding an element to the dictionary
someone.update({'salary': 3500.0})
print('\nAfter dictionary is updated')
print(keys)         # dict_keys(['name', 'age', 'salary'])

# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# dict.clear() method removes all items from the dictionary.

# dict.copy() method returns a shallow copy of the dictionary.
original = {1: 'one', 2: 'two'}
new = original.copy()

# removing all elements from the list
new.clear()

print('new: ', new)     # new:  {}
print('original: ', original)       # original:  {1: 'one', 2: 'two'}


# dict.clear() method removes all items from the dictionary.
# dict.copy(). This method returns a shallow copy of the dictionary. It doesn't modify the original dictionary.
# dictionary.fromkeys(sequence[, value]). Method returns a new dictionary with the given sequence of elements as the keys of the dictionary.
# dict.get(key[, value]). Method takes maximum of two parameters
# dictionary.items(). Method returns a view object that displays a list of a given dictionary's (key, value) tuple pair.
# dict.keys(). Method returns a view object that displays a list of all the keys in the dictionary
# dict.popitem(). Method removes and returns the last element (key, value) pair inserted into the dictionary.
# dict.setdefault(key[, default_value]). Method returns the value of a key (if the key is in dictionary). If not, it inserts key with a value to the dictionary.
# dictionary.pop(key[, default]). Method removes and returns an element from a dictionary having the given key.
# dictionary.values(). Method returns a view object that displays a list of all the values in the dictionary.
# dict.update([other]). Method adds element(s) to the dictionary if the key is not in the dictionary. If the key is in the dictionary, it updates the key with the new value.
