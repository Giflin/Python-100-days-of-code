# Datatypes
# string
#
# a="564774" is a string
#
# b=4578
#
# len(b)
# cannot be determined because b is a integer datatype.


# 34.56 is a float datatype.

# Adding the individual number to get a sum
#
a =input("Enter  a number:")
a1=a[0]
a2=a[1]
b=int(a1)+int(a2)
print(b)


weight=input("Enter your weight(in Kg):")
height=input("Enter your height(in m):")
bmi=int(weight)/(float(height)**2)
print("Your bmi is:",int(bmi))

print(8/3)
print(8//3)
print(round(8/3,2))

print(int(8/3))
score=7
performance=3.5
result=False
print(f"Your score is {score} and your performance is {performance},You passed the test is {result}")
age = input("Enter your age:")
weeks_left=(90-int(age)) * 52
print(f"You have {weeks_left} weeks left.")

# Tip calculator.
print("Welcome to the tip calculator.")
a=int(input("What was the total bill? $"))
b=int(input("what percentage tip would you like to give?10,12, or 15?"))
c=int(input("How many people to split the bill?"))
result=round((a*(b/100))/c,2)
print(f"Each person should pay :${result}")

