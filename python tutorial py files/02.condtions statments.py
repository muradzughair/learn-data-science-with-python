#-----------------------------------------------
# Python conndition statements:
#-----------------------------------------------

# a) if statement
#------------------------------------

x = -5

if x < 0:
    print("x is negative") # output: x is negative


# b) teranary operator (else if and else)
#------------------------------------

# structure:

if x > 0:
    print("x is positive")
elif x == 0:
    print("x is zero") 
else:
    print("x is negative")  # output: x is negative


# c) One line if statement
#------------------------------------

# One-line ternary
value = 'Non-negative' if y == 1 else 'Negative'
print(value)
# Nested ternary
choice = input("Say something: ")
value = "hi" if choice == "hi" else ("no" if choice == "nah" else "bye")
print(value)  