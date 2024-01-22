from random import randint
TURN_EASY=10
TURN_HARD=5
def guess(user_,computer_,turns):
    if user_>computer_:
        print("Too High")
        return turns-1
    elif user_<computer_:
        print("Too low")
        return turns-1
    else:
        print(f"You guessed it correctly.It was {computer_}")
def set_level():
    level=input("Do you want easy or hard:")
    if level=="easy":
        return TURN_EASY
    else:
        return TURN_HARD
def game():
    print("Guessing Game")
    computer_=randint(1,100)
    print(f"Answer is {computer_}")
    turns=set_level()
    user_=0
    while user_!=computer_:
        print(f"You have {turns} attempts remaining to guess the number.")
        user_=int(input("Enter the Guess:"))
        turns=guess(user_,computer_,turns)
        if turns==0:
            print("Run out of life")
            return
        elif user_!=computer_:
            print("Guess Again")
game()
