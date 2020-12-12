# Try 5 different functions of string in python ?
# Hey! I am using the PyCharm Editor for Python coding


print("Functions of String")

Name="Saurabh S. pawar"

#converting all string into lower case
print(Name.lower())

#converting all string into upper case
print(Name.upper())

#Getting index of Specific Alphabet
print(Name.index("S"))

#Calculatig occurance of specific alphabet in String
print(Name.count("a"))

#Check if there all letters in string are the alphabets. it returns boolean value True/False
print(Name.isalpha())

#The title() is used to convert the first character in each word to Uppercase and
# remaining characters to Lowercase in the string
print(Name.title())

#Finding the substring inside the given string.
print(Name.find("S."))

#The isdecimal() method returns True if all the characters are decimals
print(Name.isdecimal())


