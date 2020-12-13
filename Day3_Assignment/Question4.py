#-#-# Question4 -: write a prog to print x prime nos using while loop take input from user #-#-#

Number = 1
a=int(input("Please Enter the number you want?"))
print("Prime numbers between", 1, "and", a, "are:")

while(Number <= a):
    count = 0
    i = 2

    while(i <= Number//2):
        if(Number % i == 0):
            count = count + 1
            break
        i = i + 1

    if (count == 0 and Number != 1):
        print(" %d" %Number, end = '  ')
    Number = Number  + 1
