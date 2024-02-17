#password encryptor and decryptor

import base64

choice = input("If you want to encrypt your password, press 1 \nIf you want to decrypt your password, press 2 \n--->")

if(choice == '1'):
    user_password = input("Enter your password:- ")
    encode = base64.b64encode(user_password.encode())
    print("Your encoded password is:- ", encode)
elif(choice == '2'):
    encrypted_password = input("Enter your encrypted password:- ")
    decode = base64.b64decode(encrypted_password.encode().decode())
    print("Your decoded password is:- ", decode)