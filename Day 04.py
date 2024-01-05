import random
res=random.randint(0,1)
if res==1:
  print("Tails")
else:
  print("Heads")

# Python code to find smallest K-digit
# number divisible by X

def answer(X, K):
  MIN = pow(10, K-1)

  if(MIN % X == 0):
    return (MIN)

  else:
    return ((MIN + X) - ((MIN + X) % X))
X = 9
K = 5
print(answer(X, K));



fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]

print(dirty_dozen[1][1])

#banker roulette
line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input("Enter a number with letter of combination a,b,c and 1,2,3: ")
letter=position[0].lower()
abc=["a","b","c"]
num=abc.index(letter)
num1=int(position[1])
map[num1-1][num]="X"
print(f"{line1}\n{line2}\n{line3}")
