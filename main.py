rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
n = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
comp_choice = random.randint(0,2)
print(f"Computer chose {comp_choice}")
if (n == 0 and comp_choice == 0):
    #print(rock)
    print("It's a tie")
elif (n == 0 and comp_choice == 1):
    print(paper)
    print("You lose")
elif (n == 0 and comp_choice == 2):
    print(scissors)
    print("You win")
elif (n == 1 and comp_choice == 0):
    print(rock)
    print("You win")
elif (n == 1 and comp_choice == 1):
    print(paper)
    print("It's a tie")
elif (n == 1 and comp_choice == 2):
    print(scissors)
    print("You lose")
elif (n == 2 and comp_choice == 0):
    print(rock)
    print("You lose")
elif (n == 2 and comp_choice == 1):
    print(paper)
    print("You win")
elif (n == 2 and comp_choice == 2):
    print(scissors)
    print("It's a tie")
else:
        print("Invalid input!Please give a number between 0 and 2")
              
