#-#-# Developing Cryptography App in Python #-#-#

# Step1 -: Libraries used to convert normal text to Chiper Text
# Step2 -: take input from user and convert it into Chiper Text
# Step3 -: Display back the chiper text to user
# Step4 -: Load the key and if key is the same, based upon the input provided convert to normal Text

from cryptography.fernet import Fernet

def generatePassKey():
    key=Fernet.generate_key()
    print(key)
    print(type(key))
    # abc=open("password.key",'wb')       #Saving key into file
    # abc.write(key)
    # abc.close()
    return key

# def getMyKey():
#     abc=open('password.key','rb')
#     return abc.read()

def getContentUser():
    return input("Enter the content you want to encrypt : ")

def encryptMsg(message):
    key=bytes(input("Enter the key"))
    k=Fernet(key)
    encrypt_Msg=k.encrypt(message)
    print(encrypt_Msg)

def decryptMsg(message_sec,key):
    k=Fernet(key)
    dencrypt_Msg=k.decrypt(message_sec)
    print(dencrypt_Msg)


user_Msg=getContentUser()
print(generatePassKey())
#getMyKey()
e_msg=encryptMsg(user_Msg)
decryptMsg(user_Msg)
