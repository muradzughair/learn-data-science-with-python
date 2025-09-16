# ------------------------------------------------------------
# Dictionaries:
# ------------------------------------------------------------

# Definition: A dictionary is a collection of key-value pairs.
# Each key must be unique and immutable (string, number, tuple), 
# while values can be of any type (int, float, string, list, tuple, dictionary, set).
# Dictionaries are mutable (you can add, change, and remove key-value pairs).
# Accessing is done by the key (dict[key]).
# Duplicate keys are not allowed (the latest one will overwrite the previous).

# ------------------------------------------------------------
# a) Creating dictionaries
# ------------------------------------------------------------

# 1) Using curly braces {}
city = {"amman": 300, "irbed": 100, "aqapa": 200, "jarash": 400}
print(type(city))  # Output: <class 'dict'>

# 2) Using dict() constructor
my_dict = dict(name="Murad", age=21, country="Jordan")
print(my_dict)  # Output: {'name': 'Murad', 'age': 21, 'country': 'Jordan'}


# ------------------------------------------------------------
# b) Accessing elements
# ------------------------------------------------------------

# 1) Using key directly
print(city["amman"])  # Output: 300

# 2) Using .get() → safer (avoids KeyError, allows default value)
print(city.get("irbed"))  # Output: 100
print(city.get("n"))      # Output: None
print(city.get("murad", "the wanted value is not exist in the dictionary"))
# Output: the wanted value is not exist in the dictionary


# ------------------------------------------------------------
# c) Adding and updating items
# ------------------------------------------------------------

city["salt"] = 400
print(city)  # Adds new key-value pair

# Updating with another dictionary
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
dict1.update(dict2)
print(dict1)  # Output: {'a': 1, 'b': 3, 'c': 4}


# ------------------------------------------------------------
# d) Removing items
# ------------------------------------------------------------

# Using del
del city["aqapa"]
print(city)

# Using pop() → removes and returns the value
deleted_city = city.pop("amman")
print(deleted_city)  # Output: 300

# pop() with default value (avoids KeyError)
gender = city.pop("murad", "there is no key called murad")
print(gender)

# Clear dictionary
cars = {"bmw": 300, "Gtr": 200}
cars.clear()
print(cars)  # Output: {}


# ------------------------------------------------------------
# e) Dictionary properties
# ------------------------------------------------------------

# Duplicate keys → only one is kept
cars = {"bmw": 300, "bmw": 300, "Gtr": 200, "Gtr": 200}
print(cars)  # Output: {'bmw': 300, 'Gtr': 200}


# ------------------------------------------------------------
# f) Dictionary views
# ------------------------------------------------------------

print(city.keys())   # Returns dict_keys([...])
print(city.values()) # Returns dict_values([...])
print(city.items())  # Returns dict_items([...]) → list of tuples


# ------------------------------------------------------------
# g) Iterating over dictionaries
# ------------------------------------------------------------

student = {"name": "John Doe", "age": 21, "courses": ["Math", "Science"]}

# Iterate over keys
for k in student:
    print(k)

# Iterate over values
for v in student.values():
    print(v)

# Iterate over keys & values
for k, v in student.items():
    print(f"{k}: {v}")


# ------------------------------------------------------------
# h) Checking for keys or values
# ------------------------------------------------------------

print("name" in student)                  # True
print("John Doe" in student.values())     # True
print("Jane Doe" in student.values())     # False


# ------------------------------------------------------------
# i) Storing complex data
# ------------------------------------------------------------

students = {"Name": "Ahmad", "age": 20, "Courses": ["DSP", "Database"]}
print(students)
