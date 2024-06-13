from cryptography.fernet import Fernet

"""
key = Fernet.generate_key()
init = Fernet(key)
userMessage = input("Enter your message: ")
userMessage_byte = userMessage.encode()
message = init.encrypt(userMessage_byte)
decoding = init.decrypt(message)
print(decoding.decode())
"""

# 1. do you want to add password