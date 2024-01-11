def greet():
    print("hello")
greet()

def intro(name,place):
    print(f"My name is {name}")
    print(f"I am from {place}")
intro("Hari","Chennai")

def intro(name,place):
    print(f"My name is {name}")
    print(f"I am from {place}")
intro(place="Chennai",name="Hari")

import math
def paint_calc(height,width,cover):
  num=(height*width)//coverage
  print(f"You'll need {num} cans of paint.")
test_h = int(input("Enter the height: ")) # Height of wall (m)
test_w = int(input("Enter the width: ")) # Width of wall (m)
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)

def prime_checker(number):
  is_prime=True
  for i in range(2,number):
    if number%i==0:
      is_prime=False
  if is_prime:
      print("It's a prime number.")
  else:
      print("It's not a prime number.")
n = int(input("Enter a number to check whether the number is prime or not.")) # Check this number
prime_checker(number=n)


