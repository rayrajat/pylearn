import random
import os 

print("saving file in :", os.getcwd())

path = r"C:\Users\KIIT\OneDrive\Desktop\python\pylearn\practice\filemystry\task1.txt"

length = int(input("enter the length of password:"))

alphabets = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
special_characters = "!@#$%^&*"

password = alphabets + numbers + special_characters

with open(path,"w") as file:
    for i in range(5):
        result = "".join(random.choices(password, k=length))
        #print("generated password:", result)
        file.write("generated password: " + result + "\n")

print("password saved in file task1.txt")