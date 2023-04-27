#Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = random.randint(8, 10)
nr_symbols = random.randint(2, 4)
nr_numbers = random.randint(2, 4)

print(nr_letters)
print(nr_symbols)
print(nr_numbers)

# new_list = [new_item for item in list]

password_list = []

for char in range(nr_letters):
  password_list.append(random.choice(letters))

# Using list comprehension
password_letters = [random.choice(letters) for char1 in range(nr_letters)]
print(password_letters)

for char in range(nr_symbols):
  password_list += random.choice(symbols)

# Using list comprehension
password_symbols = [random.choice(symbols) for item in range(nr_symbols)]
print(password_symbols)

for char in range(nr_numbers):
  password_list += random.choice(numbers)

# Using list comprehension
password_numbers = [random.choice(numbers) for item in range(nr_numbers)]
print(password_numbers)

random.shuffle(password_list)

password = ""
for char in password_list:
  password += char

print(f"Your password is: {password}")