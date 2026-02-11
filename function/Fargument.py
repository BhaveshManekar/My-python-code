# def Avarage(a,b):
#     print("The avarage is",(a+b)/2)
# Avarage(5,5)

# def Avarage(a=5,b=6):
#     print("The avarage is",(a+b)/2)
# Avarage()

# def Avarage(a=5,b=6):
#     print("The avarage is",(a+b)/2)
# Avarage(4,9) #it use this new value insted of older value

#default argument
# def Avarage(a=5,b=6):
#     print("The avarage is",(a+b)/2)
# Avarage(4)

# def Avarage(a=5,b=6):
#     print("The avarage is",(a+b)/2)
# Avarage(b=6)

# def name(fname, mname="Ashok", lname="Manekar"):
#     print("hello",fname,mname,lname)
# name("bhavesh")

# def avarage(*numbers):
#     print(type(numbers))
#     sum=0
#     for i in numbers:
#         sum = sum+i
#     print("the avarage is",sum/len(numbers))

# avarage(5,6)

# def name(**name):
#     print(type(name))
#     print("hello",name["fname"],name["mname"],name["lname"])
# name(fname="bhavesh",mname="ashok",lname="manekar")

def avarage(*numbers):
    # print(type(numbers))
    sum=0
    for i in numbers:
        sum = sum+i
    # print("the avarage is",sum/len(numbers))
    return (sum/len(numbers))

c=avarage(5,6.7)
print(c)
