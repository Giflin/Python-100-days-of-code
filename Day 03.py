# conditional statements
print("Welcome to the rollercoaster")
height=int(input("What is your height(in cm):"))
if height>=120:
    print("You can ride the rollercoaster")
else:
    print("Sorry,you have to grow")


number = int(input("Enter a number: "))
if number%2==0:
  print("This is an even number.")
else:
  print("This is an odd number.")

height=int(input("What is your height(in cm):"))
if height>=120:
    print("You can ride.")
    age=int(input("Enter your age:"))
    if age>=18:
        print("You have to pay $18.")
    else:
        print("You have to pay $10.")
else:
    print("You have to grow.")

height = float(input("Enter your height(in m):"))
weight = int(input("Enter your weight(in kg):"))
bmi=weight/(height**2)
if(bmi<18.5):
  print(f"Your BMI is {bmi}, you are underweight.")
elif (bmi>=18.5 and bmi<25):
  print(f"Your BMI is {bmi}, you have a normal weight.")
elif (bmi>=25 and bmi<30):
  print(f"Your BMI is {bmi}, you are slightly overweight.")
elif (bmi>=30 and bmi<35):
  print(f"Your BMI is {bmi}, you are obese.")
else:
  print(f"Your BMI is {bmi}, you are clinically obese.")

year=int(input("Enter a year:"))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print(f"{year} is a leap year.")
        else:
            print(f"{year} is not a leap year.")
    else:
        print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")


height=int(input("What is your height(in cm):"))
bill=0
if height>=120:
    print("You can ride.")
    age=int(input("Enter your age:"))
    if age<12:
        bill=5
        print("Kids have to pay $5.")
    elif age<=18:
        bill=10
        print("Teens have to pay $10.")
    else:
        bill=15
        print("You have to pay $15.")
    pic=input("Do you need photo,Y or N:")
    if(pic=="Y"):
        bill+=3
        print(f"You have to pay ${bill}.")
    else:
        print(f"You have to pay ${bill}.")
else:
    print("You have to grow.")

# PIZZA ORDER

print("Thank you for choosing Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L: ")
add_pepperoni = input("Do you want pepperoni? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
bill=0
if size=="S":
  bill=15
  if add_pepperoni=="Y":
    bill+=2
    if extra_cheese=="Y":
      bill+=1
      print(f"Your final bill is: ${bill}.")
    else:
      print(f"Your final bill is: ${bill}.")
  else:
    if extra_cheese=="Y":
      bill+=1
      print(f"Your final bill is: ${bill}.")
    else:
      print(f"Your final bill is: ${bill}.")
elif size=="M":
  bill=20
  if add_pepperoni=="Y":
    bill+=3
    if extra_cheese=="Y":
      bill+=1
      print(f"Your final bill is: ${bill}.")
    else:
      print(f"Your final bill is: ${bill}.")
  else:
    if extra_cheese=="Y":
      bill+=1
      print(f"Your final bill is: ${bill}.")
    else:
      print(f"Your final bill is: ${bill}.")
else:
  bill=25
  if add_pepperoni=="Y":
    bill+=3
    if extra_cheese=="Y":
      bill+=1
      print(f"Your final bill is: ${bill}.")
    else:
      print(f"Your final bill is: ${bill}.")
  else:
    if extra_cheese=="Y":
      bill+=1
      print(f"Your final bill is: ${bill}.")
    else:
      print(f"Your final bill is: ${bill}.")

# LOVE CALCULATOR
print("The Love Calculator is calculating your score...")
name1 = input("What is your name?")
name2 = input("What is their name?")
name3=name1+name2
lower_name=name3.lower()
t=lower_name.count("t")
r=lower_name.count("r")
u=lower_name.count("u")
e=lower_name.count("e")
first_digit=t+r+u+e

l=lower_name.count("l")
o=lower_name.count("o")
v=lower_name.count("v")
e=lower_name.count("e")
second_digit=l+o+v+e

final=str(first_digit)+str(second_digit)
if int(final)<10 or int(final)>90:
  print(f"Your score is {final}, you go together like coke and mentos.")
elif int(final)>40 and int(final)<50:
  print(f"Your score is {final}, you are alright together.")
else:
  print(f"Your score is {final}.")




