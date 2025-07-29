#-------------------------------------------------------
#4) sets
#-------------------------------------------------------

# Sets are unordered collections of unique elements. 
# Sets are useful when you want to store items without duplicates and do not care about the order of the items.
# Sets are mutable, that mean you can chagne it


#--------------------------------------
#This is how you make set:
a={3,5,6,7,9,11}
print(a)

# set not understands index so you cant access but you can add and update it:
this_set={"apple","banana","cherry"}
this_set.add("pear")
print(this_set)
myset={"kiwi","orange","banana"}
this_set.update(myset)
print(this_set)
#note: you can update the set with sets like it or with list:
my_list=['hi']
this_set.update(my_list)
print(this_set)

#we can usd (.remove()) to remove items:
thisset = {"apple", "banana", "cherry", 'orange'}
thisset.remove("banana")
print(thisset)
#but if we remove unexist element it will give you keyError to solve this use discard
#The discard() method removes the specified item from the set:
thisset = {"apple", "banana", "cherry", 'orange'}
thisset.discard("ana") # it will not give us error
print(thisset)
#but if we remove unexist element it will give you keyError to solve this use discard

# we use set to give us the ability to do sets operations go to slides bage 58 to read about sets operations