import random

Numbers = input("Type in how many characters (reccomended: 8-10) for your password: ")

def password_generator(length, password) :
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()"
    password = ""
    for i in range(length) :
        password += random.choice(characters)
    return password

password = ""
password = password_generator(int(Numbers), password)
print("Your password is: " + password)


