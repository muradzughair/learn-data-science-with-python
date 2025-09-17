# ------------------------------------------------------------
# Slicing:
# ------------------------------------------------------------

# Definition:
# Slicing is a way to extract a portion (subsequence) of a sequence type 
# like list, tuple, or string using [start:stop:step].
#
# General Syntax:
# sequence[start:stop:step]
#
# - start → index to begin from (default: 0)
# - stop → index to stop (exclusive, default: length of sequence)
# - step → jump size (default: 1, can be negative for reverse)

# ------------------------------------------------------------
# a) Basic Slicing
# ------------------------------------------------------------

my_list = list(range(1, 7, 1))
print(my_list)  # Output: [1, 2, 3, 4, 5, 6]

# Slice from index 2 to 7 (exclusive)
print(my_list[2:7])   # Output: [3, 4, 5, 6]

# Slice with step
print(my_list[2:10:2])  # Output: [3, 5]

# Slice from index 2 to end
print(my_list[2:])  # Output: [3, 4, 5, 6]

# Slice from start to index 2 (exclusive)
print(my_list[:2])  # Output: [1, 2]


# ------------------------------------------------------------
# b) Negative Indexing
# ------------------------------------------------------------

# Negative index counts from the end (-1 is last element)

print(my_list[-2:])     # Output: [5, 6] → last two elements
print(my_list[-1::-1])  # Output: [6, 5, 4, 3, 2, 1] → reverse list
print(my_list[-3:-1])   # Output: [4, 5] → from -3 to -1 (exclusive)


# ------------------------------------------------------------
# c) Reverse Slicing
# ------------------------------------------------------------

# Reverse entire list
print(my_list[::-1])  # Output: [6, 5, 4, 3, 2, 1]

# Reverse part of the list
print(my_list[4:1:-1])  # Output: [5, 4, 3]


# ------------------------------------------------------------
# d) Copying with Slicing
# ------------------------------------------------------------

numbers = list(range(1, 9))
print(numbers)  # Output: [1, 2, 3, 4, 5, 6, 7, 8]

# Copy the entire list
a = numbers[:]
print(a)  # Output: [1, 2, 3, 4, 5, 6, 7, 8]

# Modify copy → original not affected
a[2] = 100
print(a)       # Output: [1, 2, 100, 4, 5, 6, 7, 8]
print(numbers) # Output: [1, 2, 3, 4, 5, 6, 7, 8]


# ------------------------------------------------------------
# e) Modifying with Slicing
# ------------------------------------------------------------

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

# Remove element(s) with slicing
numbers[1:2] = []  
print(numbers)  # Output: [1, 3, 4, 5, 6, 7, 8]

numbers[3:6] = []
print(numbers)  # Output: [1, 3, 4, 8]

# Replace one element
numbers[2:3] = [4]
print(numbers)  # Output: [1, 3, 4, 8]

# Replace with multiple elements
numbers[2:4] = [9, 9, 9, 9]
print(numbers)  # Output: [1, 3, 9, 9, 9, 9]

# Insert without replacing (since slice is empty)
numbers[2:2] = [400]
print(numbers)  # Output: [1, 3, 400, 9, 9, 9, 9]


# ------------------------------------------------------------
# f) Slicing Strings & Tuples
# ------------------------------------------------------------

# Works the same way with strings
text = "Python"
print(text[0:3])   # Output: Pyt
print(text[::-1])  # Output: nohtyP

# Works with tuples
t = (10, 20, 30, 40, 50)
print(t[1:4])   # Output: (20, 30, 40)


# ------------------------------------------------------------
# g) Real-life Scenarios
# ------------------------------------------------------------

# 1) Extract first N items
grades = [90, 85, 70, 100, 95]
top_3 = grades[:3]
print(top_3)  # Output: [90, 85, 70]

# 2) Extract last N items
last_two = grades[-2:]
print(last_two)  # Output: [100, 95]

# 3) Reverse a string (useful in palindrome checking)
word = "level"
print(word[::-1])  # Output: level
