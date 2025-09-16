# ------------------------------------------------------------
# Tuples:
# ------------------------------------------------------------

# Definition: Tuples are ordered collections of elements.
# Tuples allow duplicates.
# Tuples are immutable (once created, you cannot change, add, or remove elements).
# Accessing is done by index (tuple[index]).
# Use tuples when you want a fixed collection of data that should not change,
# and when order is important.

# When to use:
# - Store constant data (coordinates, RGB colors, records, etc.)
# - Return multiple values from a function
# - Use as dictionary keys (since tuples are hashable)

# Real-life scenario:
# Storing the latitude and longitude of a location
# Example: (31.963158, 35.930359) for Amman, Jordan.


# ------------------------------------------------------------
# a) Creating Tuples
# ------------------------------------------------------------

# 1) With parentheses
b = (2, 3, 4, "Bassam")
print(type(b))  # Output: <class 'tuple'>

# 2) Without parentheses (Python automatically makes it a tuple)
a = 2, 4, 5, 8
print(type(a))  # Output: <class 'tuple'>

# 3) Empty tuple
empty = ()
print(empty)  # Output: ()

# 4) Tuple with one element → must add a comma
single = (5,)
print(single)  # Output: (5,)


# ------------------------------------------------------------
# b) Accessing Elements
# ------------------------------------------------------------

t = (10, 20, 30, 40, 50)

# Access single element
print(t[0])    # 10

# Negative indexing
print(t[-1])   # 50

# Slicing
print(t[1:4])  # (20, 30, 40)


# ------------------------------------------------------------
# c) Tuple Unpacking
# ------------------------------------------------------------

# Assigning elements to variables
point = (4, 5)
x, y = point
print("x =", x)  # 4
print("y =", y)  # 5

# Swapping values without a temp variable
a, b = 100, 30
a, b = b, a
print("a =", a)  # 30
print("b =", b)  # 100

# Extended unpacking
b_tuple = (10, 20, 30, 40)
m, n, *z = b_tuple
print("m =", m)  # 10
print("n =", n)  # 20
print("z =", z)  # [30, 40]


# ------------------------------------------------------------
# d) Tuple Properties
# ------------------------------------------------------------

# Tuples can contain mixed data types
mixed = (1, "Murad", 3.14, [1, 2, 3])
print(mixed)

# Tuples are immutable
t = (1, 2, 3)
# t[0] = 99  # ❌ Error → 'tuple' object does not support item assignment

# But if tuple contains a mutable object (like list), that list can be changed
nested = (1, [2, 3], 4)
nested[1][0] = 99
print(nested)  # (1, [99, 3], 4)


# ------------------------------------------------------------
# e) Tuple Methods
# ------------------------------------------------------------

t = (1, 2, 2, 3, 4)

print(t.count(2))   # 2 (occurs two times)
print(t.index(3))   # 2 (position of element 3)


# ------------------------------------------------------------
# f) Nested Tuples
# ------------------------------------------------------------

nested = (1, (2, 3), (4, 5, 6))
print(nested[1])     # (2, 3)
print(nested[2][1])  # 5


# ------------------------------------------------------------
# g) Real-life Examples
# ------------------------------------------------------------

# RGB color value
color = (255, 0, 127)

# Returning multiple values from a function
def min_max(values):
    return min(values), max(values)

result = min_max([3, 7, 2, 9])
print(result)  # (2, 9)
