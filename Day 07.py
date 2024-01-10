# while condition

i=1
while i<7:
    print(i)
    i=i+1

import random
words=["messi","ronaldo","neymar"]
chosen=random.choice(words)
print(f"{chosen}")
lives=6
display=[]
for i in chosen:
    display+="_"
end_of_game=False
while not end_of_game:
    guess=input("Enter a letter:").lower()
    for position in range(len(chosen)):
        letter=chosen[position]
        if guess==letter:
            print(f"Correct,You guessed a letter {guess} which is in the list.")
            display[position]=letter
    print(f"{' '.join(display)}")
    if guess not in chosen:
        print(f"You guessed a letter {guess} not in the list.")
        lives-=1
        if lives==0:
            end_of_game=True
            print("You lose")
    if "_" not in display:
        end_of_game=True
        print("You Won")
