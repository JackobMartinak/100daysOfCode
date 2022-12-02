# TODO: RANDOM PASSWORD GENERATOR

import random

letters = ['a', 'b', 'c', 'd','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','v','w','u','x','y','z']
numbers = [0,1,2,3,4,5,6,7,8,9]
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')','+', '=', '_']

nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = []

for _ in range(0, nr_letters + 1):
    password.append(random.choice(letters))

for _ in range(0, nr_symbols + 1):
    password.append(random.choice(symbols))

for _ in range(0, nr_numbers + 1):
    password.append(random.choice(numbers))

random.shuffle(password)
full_pass = ''.join(map(str,password))
print(full_pass)
