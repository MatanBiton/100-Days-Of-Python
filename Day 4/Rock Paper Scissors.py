import random

ROCK = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

PAPER = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

SCISSORS = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

draw_dict = {
    0: ROCK,
    1: PAPER,
    2: SCISSORS
    }

user_selection = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors.\n"))
computer_selection = random.randint(0,2)
print(draw_dict[user_selection])
print("Computer chose:")
print(draw_dict[computer_selection])
if user_selection == computer_selection:
    print("Draw!")
elif user_selection > computer_selection:
    if computer_selection == 0 and user_selection == 2:
        print("You Lose!!!")
    else:
        print("You Won!!!")
else:
    if user_selection == 0 and computer_selection == 2:
        print("You Won!!!")
    else:
        print("You Lose!!!")
    
