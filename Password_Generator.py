import random, string

length = int(input("How long should the password be? "))
num_of = int(input("How many passwords do you want? "))
print("\n")
print("Passwords:")

letters = string.ascii_letters
numbers = string.digits
symbols = string.punctuation

chars = letters + numbers + symbols
num = 1

while num <= num_of:
  password = random.choices(chars, k = length)
  password = '  '.join(password)
  print(password)
  num += 1
