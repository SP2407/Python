#-#-# Question2 -: Write a function which can return a factorial of any number given in the argument. #-#-#
#Hey I am using Pycharm IDE

print("Factorial of a Number")

def fact(a):
    factorial = 1
    for i in range(1, num + 1):
        factorial = factorial * i
    print("The factorial of", num, "is", factorial)

num=int(input("Enter the Number -: "))
fact(num)