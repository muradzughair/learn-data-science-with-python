#-------------------------------------------------------
#4) sets
#-------------------------------------------------------

# 1) Sets are unordered collections of unique elements.

# 2) They do not allow duplicates.

# 3) Sets are mutable (you can add or remove elements, but not change them directly).

# Use sets when you want to remove duplicates or do mathematical set operations (union, intersection, difference).

# When to use: When you need a collection of unique items and don’t care about order and you want to use sets operation like (and, or, not ).

# Real-life scenario: system to see the matual friends between two people.



#--------------------------------------
#This is how we make a set:
a={3,5,6,7,9,11}
print(a)


#--------------------------------------
# We use add function to add elements to the set:
a.add(12)   
print(a) # Output: {3, 5, 6, 7, 9, 11, 12}

# we use update to add multiple elements:
a.update([13,14,15])    
print(a) # Output: {3, 5, 6, 7, 9, 11, 12, 13, 14, 15}

# ANd as I said sets are unordered collections of unique elements, so if you try to add duplicate elements, they will be ignored.:
this_set={"apple","banana","cherry"}
myset={"kiwi","orange","banana"}
this_set.update(myset) 
print(this_set) # Output: {'banana', 'cherry', 'kiwi', 'orange', 'apple', 'pear'}

#note: you can use update to add list, tuple, set, or dictionary to the set:
my_list=['hi']
this_set.update(my_list)
print(this_set)

#---------------------------------------
# We use remove to remove elements from the set:
thisset = {"apple", "banana", "cherry", 'orange'}
thisset.remove("banana")
print(thisset) # Output: {'cherry', 'orange', 'apple'}
# But if we remove unexist element it will give you keyError to solve this use (discard)
#The discard() method removes the specified item from the set:
thisset = {"apple", "banana", "cherry", 'orange'}
thisset.discard("ana") # Its not exist vlaue
print(thisset) # Output: {'cherry', 'orange', 'apple', 'banana'} without error


#----------------------------------
# Sets operations:
#----------------------------------

fruits = {"apple", "banana", "orange", "apple"}  


# -----------------------------
# Checking Membership

print("apple" in fruits)   # True
print("banana" in fruits)  # False


A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

#----------------------------------
# Union: all unique elements from both sets
print(A | B)        # {1, 2, 3, 4, 5, 6}
print(A.union(B))   # same result

#----------------------------------
# Intersection: elements common to both sets
print(A & B)        # {3, 4}
print(A.intersection(B))  

#----------------------------------
# Difference: elements in A but not in B
print(A - B)        # {1, 2}
print(A.difference(B))

#----------------------------------
# Symmetric Difference: elements in A or B, but not both
print(A ^ B)        # {1, 2, 5, 6}
print(A.symmetric_difference(B))
