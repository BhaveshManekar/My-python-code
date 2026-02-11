num=int(input("enter your number: "))
print("your number is: ", num)
if(num<0):
    print("your number is negitive")
elif(num>0):
    if(num<=10):
        print("your num is in between 1 to 10")
    elif(num>=10):
        print("your num is in between 11 to 20")
    elif(num==0):
        print("your num is zero")
else:
    print("your number is invalid")