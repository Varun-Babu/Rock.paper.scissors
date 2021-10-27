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
import random
print("WELCOME TO ROCK PAPER SCISSORS")
choice = int(input("enter 0 for rock , 1 for paper and 2 for scissors"))
opponent = [rock,paper,scissors]
print(opponent[choice])
generate = random.randint(0,len(opponent)-1)
if choice < 3:
        print("computer")
        print(opponent[generate])
else:
        print("invalid input")
if choice >= 3:
        print()
if choice == 0 and generate==2:
        print("you win")
elif choice == 2 and generate ==1:
        print("you win")
elif choice == 1 and generate == 0:
        print("you win")
elif choice == generate:
        print("draw")
else:
        print("you lost")
