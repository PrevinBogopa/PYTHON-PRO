import random

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
nums = "1234567890"
symbols = "-+=!@#$%^&*"

num_letters = int(input("How many letters do you want in your password? "))
num_nums = int(input("How many numbers do you want in your password? "))
num_symbols = int(input("How many symbols do you want in your password? "))

password_list = []

# add letters to the password
for i in range(num_letters):
    password_list.append(random.choice(letters))

# add numbers to the password
for i in range(num_nums):
    password_list.append(random.choice(nums))

# add symbols to the password
for i in range(num_symbols):
    password_list.append(random.choice(symbols))

# shuffle the password list
random.shuffle(password_list)

# convert the password list to a string
password = "".join(password_list)

print("Your password is:", password)