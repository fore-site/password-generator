# password generator

import random

print('Welcome to the PyPassword Generator!')

alphabets = 'abcdefghijklmnopqrstuvwxyz'

# create an empty list to store the lower and uppercase alphabets
alphabets_list = []
symbols = "!@#$%&*()+"

# create an empty list to store the symbols
symbols_list = []

number_list = [0,1,2,3,4,5,6,7,8,9]

# iterate over the alphabets string, and append to list, also capitalize the alphabets and append them to the list
for i in alphabets:
    alphabets_list.append(i)
    alphabets_list.append(i.upper())

# iterate over the symbols string and append to list
for j in symbols:
    symbols_list.append(j)

# receive password specifications from user
letter_length = int(input("How many letters would you like in your password?\n"))
symbol_length = int(input("How many symbols would you like?\n"))
number_length = int(input("How many numbers would you like?\n"))

# store length of password
password_length = letter_length + symbol_length + number_length

# create a list of the same size as the length of password. set each value to None
password_list = [None] * password_length


# randomly generate the letters, symbols, and numbers from their respective list, limit to the number of each the user wants in their password. assign the them to a randomly selected index
for k in range (0, letter_length):
    r = random.randint(0,password_length-1)
    if password_list[r] == None:
        password_list[r] = random.choice(alphabets_list)
    else:
        index = password_list.index(None)
        password_list[index] = random.choice(alphabets_list)


for j in range (0, number_length):
    r = random.randint(0, password_length - 1)
    if password_list[r] == None:
        password_list[r] = str(random.choice(number_list))
    else:
        index = password_list.index(None)
        password_list[index] = str(random.choice(number_list))

for k in range(0, symbol_length):
    r = random.randint(0, password_length - 1)
    if password_list[r] == None:
        password_list[r] = random.choice(symbols_list)
    else:
        index = password_list.index(None)
        password_list[index] = random.choice(symbols_list)
            
print(password_list)

# convert the password list to a string
password = "".join(password_list) 

# print the result
print(f'Here is your password: {password}')

