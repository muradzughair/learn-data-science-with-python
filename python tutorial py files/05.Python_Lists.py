# ------------------------------------------------------------
# Lists:
# ------------------------------------------------------------


# Definition: Lists is a dynamic sized arrray (Automatically grows and shrinks)
# List Can store all types of data (int, float, string, list, tuple, dictionary, set)
# List can contain duplicate values
# List is mutable (you can change it)
# List Accessing is done by index (list[index])
# (Append) is the the operation we use to add elements to the list
# If you want to add element in specific position you can use (insert)
# Extend is used to add multiple elements to the list
# We use (pop) to remove elements by index and return this value
# We use (remove) to remove elements by value


# This is how we make list:
a=[2,4,6,8,"Bassam","Data science",[2,3,4]] 
print(type(a)) # Output: <class 'list'>

# you can make an empty list and fill it whenever you want:
a_list=[]
print(a_list) # Output: []
# or
a_list=list()


# This is how we access the elements of the list (vartiable[index]):
print(a[4]) # Output: Bassam

# To print the lists elements one by one:
for i in range(len(a)) :
    print(a[i]) # Output: 2, 4, 6, 8, Bassam, Data science
    


# This how we use append to add elements
a.append("murad")
print(a) # Output: [2, 4, 6, 8, 'Bassam', 'Data science', [2, 3, 4], 'murad']
    

# This is how we use insert to add elements in specific position
a.insert(2,"mr") 
print(a) # Output: [2, 4, 'mr', 6, 8, 'Bassam', 'Data science', [2, 3, 4], 'murad']

# This is how you use extend
a=[2,4,6,8,"Bassam","Data science"]
a.append([2,3,4]) # It will add the list as one element
print(a) # Output: [2, 4, 6, 8, 'Bassam', 'Data science', [2, 3, 4]]

a.extend([2,3,4]) # It will add 2,3,4
print(a) # Output: [2, 4, 6, 8, 'Bassam', 'Data science', [2, 3, 4], 2, 3, 4]

# Note: if you use extend  to add string value it will be added as char because string is a array of char
a.extend('murad') # It will add "m", "u", "r", "a", "d"

# We can use (pop) and (remove) to delete elememts
a.pop(1)           #its delete by the digit
a.remove('Bassam') #its delete the specific elememt

#---------------------------------
# a) List operations:
#---------------------------------

# We can combine lists:
a1=[1,2,3]
b1=[4,6,7]

a2=a1+b1
print(a2) # Output: [1, 2, 3, 4, 6, 7]

# Note: Using extend to combine Lists is faster and better
a1 = [1,2,3]
b1 = [4,6,7]

a1.extend(b1)  
print(a1)  # Output: [1, 2, 3, 4, 6, 7]



#---------------------------------
# b) nested list
#---------------------------------


a=[2,4,[5,10,15],20,24,[2,[40,80],100]]

print(a) # Output: [2, 4, [5, 10, 15], 20, 24, [2, [40, 80], 100]]
print(a[2][1]) # Output: 10
a[2][2]=150 
print(a) # Output: [2, 4, [5, 10, 150], 20, 24, [2, [40, 80], 100]]

lst=[[1,2],[4,5],[7,8]]

# You can access the elements of the nested list like this:
for x,y in  lst:
    print(x,y) # Output: 1 2, 4 5, 7 8


#---------------------------------
# List comprehantion
#---------------------------------


# List comprehantion is a way to create lists in a more concise and readable manner.

# List comprehension structuer: [variable for variable in iterable if condition] 

lst=[value for value in range(1,5)] # this is list comprehantion
print(lst) # Output: [1, 2, 3, 4]


# List comprehension Example (1):

# Check if a character is in a string and create a new list with those characters:

# Without list comprehantion:
f=['apple' , 'bannana','cherry','mangi','kiwi']
newlst=[]

for i in f:    # We use (in) to check all the element in the list
    if 'a' in i:
        newlst.append(i)
print(newlst) # Output: ['apple', 'bannana', 'mangi']

# With list comprehantion:
my_lst=[item for item in f if 'a' in item]
print(my_lst) # Output: ['apple', 'bannana', 'mangi']


# List comprehension Example (2):
# Create a new list that contains the numbers that greater than 5 from the original list:
original_lst=[2,4,6,8,11,5]
new_lst=[value for value in original_lst if value>5]
print(new_lst) # Output: [6, 8, 11] 