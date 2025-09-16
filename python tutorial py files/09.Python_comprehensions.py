# ------------------------------------------------------------
# Comprehensions in Python
# ------------------------------------------------------------

# Definition:
# Comprehensions provide a concise and readable way to create collections 
# (list, dictionary, set) in a single line of code.
# They are often more efficient and cleaner than using loops.

# General Syntax:
# [expression for item in iterable if condition]

# ------------------------------------------------------------
# 1) List Comprehension
# ------------------------------------------------------------

# Create a list of numbers from 1 to 5
lst = [value for value in range(1, 6)]
print(lst)  # Output: [1, 2, 3, 4, 5]

# Example (1): Filtering → get words that contain 'a'
fruits = ['apple', 'banana', 'cherry', 'mango', 'kiwi']
new_lst = [item for item in fruits if 'a' in item]
print(new_lst)  # Output: ['apple', 'banana', 'mango']

# Example (2): Filtering → numbers greater than 5
original_lst = [2, 4, 6, 8, 11, 5]
new_lst = [value for value in original_lst if value > 5]
print(new_lst)  # Output: [6, 8, 11]

# Example (3): Squaring numbers
squares = [x**2 for x in range(6)]
print(squares)  # Output: [0, 1, 4, 9, 16, 25]


# ------------------------------------------------------------
# 2) Dictionary Comprehension
# ------------------------------------------------------------

# Example (1): Filter values > 10
original = {'a': 5, 'b': 15, 'c': 20, 'd': 8}
new_dict = {k: v for k, v in original.items() if v > 10}
print(new_dict)  # Output: {'b': 15, 'c': 20}

# Example (2): Swap keys and values
original_dict = {'apple': 'fruit', 'carrot': 'vegetable', 'pear': 'fruit'}
swapped = {v: k for k, v in original_dict.items()}
print(swapped)  # Output: {'fruit': 'pear', 'vegetable': 'carrot'}

# Example (3): Uppercase keys
original = {'a': 5, 'b': 15, 'c': 20, 'd': 8}
filtered = {k.upper(): v for k, v in original.items() if v > 10}
print(filtered)  # Output: {'B': 15, 'C': 20}

# Example (4): Filter dictionary by keys
original_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
filtered_dict = {k: v for k, v in original_dict.items() if k in ['a', 'c']}
print(filtered_dict)  # Output: {'a': 1, 'c': 3}

# Example (5): Dictionary from list of tuples
list_of_tuples = [('a', 1), ('b', 2), ('c', 3)]
dict_from_tuples = {k: v for k, v in list_of_tuples}
print(dict_from_tuples)  # Output: {'a': 1, 'b': 2, 'c': 3}

# Example (6): Character frequency from string
text = "hello"
char_frequency = {char: text.count(char) for char in text}
print(char_frequency)  # Output: {'h': 1, 'e': 1, 'l': 2, 'o': 1}

# Example (7): Dictionary from list (squares)
numbers = [1, 2, 3, 4, 5]
my_dict = {n: n**2 for n in numbers}
print(my_dict)  # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


# ------------------------------------------------------------
# 3) Set Comprehension
# ------------------------------------------------------------

# Create a set of unique lengths of words
fruits = ['apple', 'banana', 'cherry', 'kiwi', 'Avocado']
unique_lengths = {len(x) for x in fruits}
print(unique_lengths)  # Output: {4, 5, 6, 7}

# Example (2): Unique squares
unique_squares = {x**2 for x in [1, 2, 2, 3, 3, 4]}
print(unique_squares)  # Output: {16, 1, 4, 9}


# ------------------------------------------------------------
# 4) Generator Expression (Extra)
# ------------------------------------------------------------

# Like list comprehension but uses () instead of []
# It does not create the whole list in memory → generates values one by one
gen = (x**2 for x in range(5))
print(next(gen))  # Output: 0
print(next(gen))  # Output: 1
print(next(gen))  # Output: 4

# Convert generator to list
print(list(gen))  # Output: [9, 16]
