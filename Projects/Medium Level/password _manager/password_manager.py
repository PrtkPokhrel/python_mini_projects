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


def masterPassword(usrname, passwd):
    userName_byte = userName.encode()
    password_byte = password.encode()
    key = Fernet.generate_key()
    init = fernet.Fernet(key)
    encryptedMasterPassword = init.encrypt(password_byte)
    return encryptedMasterPassword


def copyUsername(username):  # creates a copy of the username and password
    path = 'copy.txt'
    with open(path, 'a') as f:
        f.write(username)
        f.write('\n')

# def createNewUser():


if __name__ == '__main__':
    userName = input("Enter your username for master password:")
    password = input("Enter your password for master password")
    print(masterPassword(userName, password))
    copyUsername(userName)



"""
reminder:
checks whethther the username is available or not 
if not then return an error message
else create a unique file for the user
"""