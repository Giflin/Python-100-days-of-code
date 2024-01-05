student_heights = input("Enter heights:").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
total_heights=0
for i in student_heights:
  total_heights+=i
num=len(student_heights)
print(f"total height = {total_heights}")
print(f"number of students = {num}")
average=round(total_heights/num)
print(f"average height = {average}")

#Highest number in the list
student_scores = input("Enter  many numbers to find the max:").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

num=0
for i in student_scores:
  if i>num:
    num=i
print(f"The highest score in the class is: {num}")

print(50*101)

# To find the sum of all  even numbers between a range
target=int(input("Enter a range: "))
num=0
for i in range(2,target+1):
  if i%2==0:
    num+=i
print(num)


for i in range(1,101):
  if i%3==0 and i%5==0:
    print("FizzBuzz")
  elif i%3==0:
    print("Fizz")
  elif i%5==0:
    print("Buzz")
  else:
    print(i)
