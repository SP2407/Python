#Try 5 different functions of Lists in python ?
# Hey! I am using the PyCharm Editor for Python coding

print("Functions of List")

Lst=["Saurabh","Pawar",1,2,3,1.2,1.3,["Daund",1,1.2],44]

#Accessing the last element of list
print(Lst[-1])

#Getting the position of specific element
print(Lst.count("Pawar"))

#Removing Element From the list
Lst.remove(44)
print(Lst)

#Inserting Element
Lst.insert(3,55)
print(Lst)

#inserting the element at last by append method
Lst.append("XYZ")
print(Lst)

#Reversing the List
Lst.reverse()
print(Lst)

#Copying the List
Lst1=Lst.copy()
print(Lst1)

#Clear the whole List
Lst.clear()
print(Lst)