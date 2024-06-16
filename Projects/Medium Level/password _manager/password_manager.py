"""
key = Fernet.generate_key()
init = Fernet(key)
userMessage = input("Enter your message: ")
userMessage_byte = userMessage.encode()
message = init.encrypt(userMessage_byte)
decoding = init.decrypt(message)
print(decoding.decode())
"""
from cryptography import fernet
# create  master password and user name(for each user name different files)
# login to the account for accessing the password
# add website name and password
# token is generated for the particular password
# to access the password you have to use the token
# similarly has the ability to edit the password
# also has the ability to delete password

from cryptography.fernet import Fernet


def masterPassword():
    key = Fernet.generate_key()
    init = fernet.Fernet(key)
    # encodedMasterPassword = userDetail()
    encryptedMasterPassword = init.encrypt(userDetail()[0])  # needs to assign a variable in future if needed
    return encryptedMasterPassword


def createFile():  # creates a copy of the username and password
    path = 'copy.txt'
    with open(path, 'a') as f:
        f.write(userDetail()[2])
        print("\n")


def userDetail():
    print("This is for the master password")
    userName = input("Enter your name: ")
    userName_byte = userName.encode()
    password = input("Enter your password: ")
    password_byte = password.encode()
    return userName_byte, password_byte, userName


def login():
    pass


def addDetails():
    pass


def accessPassword():
    pass


def deletePassword():
    pass


print(masterPassword())
# createFile()
