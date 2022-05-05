import random

letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','o','r','s','t','u','v','w','x','y','z']
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=["!",'#','$','%','(',')','*','+']

print('===paswoord generator===')
num_letters=int(input("how many letters you want in passowrds?\n"))
num_symbols=int(input(f"how many symbols in password?\n"))
num_numbers=int(input("how many numbers in passowod ?\n"))

passowrd=''

for char in range (1,num_letters+1):
    passowrd+= random.choice(letters)

for char in range (1,num_numbers+1):
    passowrd+= random.choice(numbers)

for char in range (1,num_symbols+1):
    passowrd+= random.choice(symbols)

print(passowrd)

print(type(passowrd))
