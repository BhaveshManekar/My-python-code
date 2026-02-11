def func1():
    try:
        l=[1,3,4,6]
        i=int(input("enter the index: "))
        print(l[i])
        return 1
    except:
        print("some error occurred")
        return 0
    
    finally:
        print("i am always executed")

x= func1()
print(x)