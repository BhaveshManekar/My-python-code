# factorial(7)=7*6*5*4*3*2*1
# factorial(6)=6*5*4*3*2*1
# factorial(5)=5*4*3*2*1
# factorial(4)=4*3*2*1

# factorial(n) = n*factoral(n-1)

# def factorial(n):
#     if(n==0 or n==1):
#         return 1
#     else:
#         return n*factorial(n-1)
    
# print(factorial(5))
# print(factorial(4))
# print(factorial(3))
# 5 * factorial(4)
# 5 * 4 * factorial(3)
# 5 * 4 * 3 * factorial(2)
# 5 * 4 * 3 * 2 * factorial(1)

# Fibonacci sequence
# f(0) = 0
# f(1) = 1
# f(2) = f(1) + f(0)
# f(n) = f(n-1) + f(n-2)
    
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

terms = int(input("Enter number of terms: "))

print("Fibonacci series:")
for i in range(terms):
    print(fib(i), end=" ")
