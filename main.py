import random
password = "+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
password_length = int(input("Enter the length of each password: "))
password_count = ""
for i in range(password_length):
    password_count += random.choice(password)
print("Your password is: " + password_count)
    
