#-#-# Question-1 #-#-#
#Use If Else and Elif to write a program in python for your Report cards.
#Hey I am using Pycharm IDE

print("Report Card")

a=int(input("Enter Your Marks -: "))

if a<=100 and a>90:
    print("You got 'A+' Grade")
elif a>85 and a<=90:
    print("You got 'A' Grade")
elif a>80 and a<=85:
    print("You got 'B+' Grade")
elif a>70 and a<=80:
    print("You got 'C+' Grade")
elif a>60 and a<=70:
    print("You got 'C' Grade")
elif a>40 and a<=60:
    print("You got 'D' Grade")
else:
    print("You Failed")