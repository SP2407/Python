#-#-# Question 2 -: write a Program Using for loop to print prime nos between 1-1000. #-#-#
# HEy I am using Pycharm IDE

print("Prime Number between 1-1000 are -: ")

for num in range(1,1000 + 1):
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           print("\t",num)
