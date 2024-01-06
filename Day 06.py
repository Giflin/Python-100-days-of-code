import random
print("Welcome to the password generator!")
letters=["a","b","c","d","e","f","g","h","i"]
num=["1","2","3","4","5","6","7","8","9"]
sym=["@","#","!","%","&"]
password=""
num_let=int(input("Enter the length of letters: "))
num_num=int(input("Enter the length of numbers: "))
num_sym=int(input("Enter the length of symbol: "))
for i in range(1,num_let+1):
    password+=random.choice(letters)
for i in range(1,num_sym+1):
    password+=random.choice(sym)
for i in range(1,num_num+1):
    password+=random.choice(num)
print(password)


import random
password=[]
print("Welcome to the password generator!")
letters=["a","b","c","d","e","f","g","h","i"]
num=["1","2","3","4","5","6","7","8","9"]
sym=["@","#","!","%","&"]
num_let=int(input("Enter the length of letters: "))
num_num=int(input("Enter the length of numbers: "))
num_sym=int(input("Enter the length of symbol: "))
for i in range(1,num_let+1):
     password.append(random.choice(letters))
for i in range(1,num_num+1):
     password.append(random.choice(num))
for i in range(1,num_sym+1):
     password.append(random.choice(sym))
print(password)
random.shuffle(password)
for k in password:
     print(k,end="")

