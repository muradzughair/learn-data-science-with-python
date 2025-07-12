#-----------------------------------------------
# Python Loops:
#-----------------------------------------------

#------------------------------------
# For loop
#------------------------------------

# a) range() Function
#------------------------------------

'''
The range() function is one of the most important functions used in loops.
It defines the number of iterations the loop will execute.
'''
print(list(range(5)))  # Output: [0, 1, 2, 3, 4]

# b) For loop with range()
#------------------------------------

for i in range(5):
    print(i, end='')  # Output: 0 1 2 3 4

print()  # New line for better readability

name = "hi mohammed"
for char in name:
    print(char  , end=' ') # Output: h i   m o h a m m e d


# d) Nested loops
#------------------------------------   

for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} * {j} = {i * j}") 
# Output:
'''
1 * 1 = 1
1 * 2 = 2
1 * 3 = 3   
2 * 1 = 2
2 * 2 = 4
2 * 3 = 6
3 * 1 = 3
3 * 2 = 6
3 * 3 = 9
'''

#------------------------------------
# While loop
#------------------------------------

'''
"repeating action until condition is met"
Example
Error starts at 50
Divide error by 4 on every run
Continue until error no longer > 1
'''

error = 50.0
while error > 1:
    error = error / 4
    print(error) # Output: 12.5, 3.125, 0.78125
 
#------------------------------------
# Break and Continue    
#------------------------------------

'''
| Keyword    | What it Does                                                  | When to Use                                                     |
| ---------- | ------------------------------------------------------------- | --------------------------------------------------------------- |
| continue   | Skips the current iteration and moves to the next one           | When you want to ignore certain cases but keep looping          |
| break      | Exits the entire loop immediately                               | When you want to **stop the loop completely** under a condition |
'''

# continue Example

for i in range(5):
    if i == 2:
        continue
    print(i) # Output: 0 1 3 4

# break Example
for i in range(5):
    if i == 2:
        break
    print(i) # Output: 0 1