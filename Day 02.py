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
# print(b)


weight=input("Enter your weight(in Kg):")
height=input("Enter your height(in m):")
bmi=int(weight)/(float(height)**2)
print("Your bmi is:",int(bmi))
