#-#-# Project4 -: Read and write a real time database to a server using firebase #-#-#

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account
cred = credentials.Certificate('python-project4-firebase-adminsdk-zun8w-835a9d69c4.json')
firebase_admin.initialize_app(cred)
print(cred)
db = firestore.client()

### Writing Data into cloud Firebase ###
doc_ref = db.collection(u'users').document(u'abc')
doc_ref.set({
    u'first': u'Saurabh',
    u'last': u'Pawar',
    u'born': 1999
})


def dataEnter(name,lastName,age):
    doc_ref = db.collection(u'users').document()
    dit={}
    dit["firstName"]=name
    dit["lastName"]=lastName
    dit["age"]=age
    doc_ref.set(dit)

FirstName=input("Enter Your Name -: ")
LastNAme=input("Enter YOur Last Name -: ")
Age=int(input("Enter Your Age -: "))
dataEnter(FirstName,LastNAme,Age)

### Read data from firebase DB ###
users_ref = db.collection(u'users')
docs = users_ref.stream()
for doc in docs:
    print(f'{doc.id} => {doc.to_dict()}')
    print("ID - ",doc.id)
    print("Name -: ",doc.to_dict().get("firstName"))
    print("LastName -: ", doc.to_dict().get("lastName"))
    print("Age -: ", doc.to_dict().get("age"))
    print("--------------------------------------")

### Update a Entry in firebase ###

def Update(uid,UpdatedAge):
    doc_ref = db.collection(u'users').document(uid)

    doc_ref.update({"age":UpdatedAge})

Update('9ix4rjMCopQcvxaZejoZ',30)

### Delete Data from Firebase ###
def deletedata(uid):
    doc_ref = db.collection(u'users').document(uid).delete()

deletedata('9ix4rjMCopQcvxaZejoZ')




