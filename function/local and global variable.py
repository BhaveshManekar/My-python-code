x = 10 # global variable

def my_function():
    global x # if we want to change the golbal variable inside the function
    x = 4
    y = 5 # local variable 
    print(y)

my_function()
print(x)
# print(y) # this will cause an error because y is a local variable and is not accessible outside of the function