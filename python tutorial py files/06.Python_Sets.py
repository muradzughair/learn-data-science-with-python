# ------------------------------------------------------------
# Sets:
# ------------------------------------------------------------

# Definition:
# 1) Sets are unordered collections of unique elements.
# 2) They do not allow duplicates.
# 3) Sets are mutable (you can add or remove elements, but not change them directly).
#
# Use sets when:
# - You want to remove duplicates automatically.
# - You want to perform mathematical set operations (union, intersection, difference).
# - You don’t care about order of elements.
#
# Real-life scenario:
# Finding mutual friends between two people (intersection of friend lists).


# ------------------------------------------------------------
# a) Creating Sets
# ------------------------------------------------------------

a = {3, 5, 6, 7, 9, 11}
print(a)  # Output: {3, 5, 6, 7, 9, 11}

# Empty set → must use set(), {} creates a dictionary
empty_set = set()
print(empty_set)  # Output: set()


# ------------------------------------------------------------
# b) Adding Elements
# ------------------------------------------------------------

# Add a single element
a.add(12)
print(a)  # Output: {3, 5, 6, 7, 9, 11, 12}

# Add multiple elements (list, tuple, set, or dict keys)
a.update([13, 14, 15])
print(a)  # Output: {3, 5, 6, 7, 9, 11, 12, 13, 14, 15}

# Adding another set (duplicates ignored)
this_set = {"apple", "banana", "cherry"}
myset = {"kiwi", "orange", "banana"}
this_set.update(myset)
print(this_set)  # Output: {'banana', 'cherry', 'kiwi', 'orange', 'apple'}

# Adding from a list
my_list = ["hi"]
this_set.update(my_list)
print(this_set)


# ------------------------------------------------------------
# c) Removing Elements
# ------------------------------------------------------------

thisset = {"apple", "banana", "cherry", "orange"}

# Remove an item (KeyError if not found)
thisset.remove("banana")
print(thisset)  # Output: {'cherry', 'orange', 'apple'}

# Discard an item (no error if not found)
thisset.discard("ana")
print(thisset)  # Output: {'cherry', 'orange', 'apple'}


# ------------------------------------------------------------
# d) Checking Membership
# ------------------------------------------------------------

fruits = {"apple", "banana", "orange"}
print("apple" in fruits)   # True
print("pear" in fruits)    # False


# ------------------------------------------------------------
# e) Set Operations
# ------------------------------------------------------------

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# Union → all unique elements from both sets
print(A | B)          # {1, 2, 3, 4, 5, 6}
print(A.union(B))

# Intersection → elements common to both sets
print(A & B)          # {3, 4}
print(A.intersection(B))

# Difference → elements in A but not in B
print(A - B)          # {1, 2}
print(A.difference(B))

# Symmetric Difference → elements in A or B but not both
print(A ^ B)          # {1, 2, 5, 6}
print(A.symmetric_difference(B))
