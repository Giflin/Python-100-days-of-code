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
