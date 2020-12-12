#Experiment 5 default functions of dictonary in python ?
## Hey! I am using the PyCharm Editor for Python coding

print("Functions for Dictonary")

dictonary={"name":"Value","key1":1,"Key2":5.6,"Age":13,'SubDict':{"key1":1,"key2":2,"key3":3}}

#Getting only keys from the dictonary
print(dictonary.keys())

#Getting only values from dictonary
print(dictonary.values())

#Getting element from dect from key
print(dictonary.get("SubDict"))

#Getting all items from dict
print(dictonary.items())

#updating the dictonary
dict={"call":413801}
dictonary.update(dict)
print(dictonary)

#Pop out last inserted key value pair
dictonary.popitem()
print(dictonary)

#Pop out the element using Key-Value
dictonary.pop("name","Value")
print(dictonary)

#Clearing all elements from dictonary
dictonary.clear()
print(dictonary)