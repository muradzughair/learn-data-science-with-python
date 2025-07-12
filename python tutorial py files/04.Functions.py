# ------------------------------------------------------------
# Functions In Python
# ------------------------------------------------------------


# a) functions syntax
# ------------------------------------------------
def My_function(x,y):
    return (x / y)
    
# also in functions you can put default value for parameters in case the user dont enter one 
def sum_func(x,y=0):
    return x/y
    
# here how you call a function:

print(My_function(10,2))
print(sum_func(x))

# in python you can put the parameters where you want like this:
print(My_function(y=2,x=10))

# python functions give you a ability to return multiple values:
def f():
    a = 5
    b = 6
    c = 7
    return a, b, c

# b) Lambda functions
# ------------------------------------------------

check=lambda x: 'negative' if x<0 else('posetive' if x>0 else'0')
print(check(10))

x = lambda a, b : a * b if (a < 0) else None
print(x(5, 6))
