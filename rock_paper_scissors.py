import random
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

rps = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
compChoice = random.randint(0, 2)
choiceLst = ['rock', 'paper', 'scissors']
if rps >= 3 or rps < 0:
  print("Invalid choice, you lose!")
else:
  print(f"You chose {choiceLst[rps]} and the computer chose {choiceLst[compChoice]}")
if rps == 0 and compChoice == 0:
  print(rock,'\n'"It's a draw!")
if rps == 1 and compChoice == 1:
  print(paper,'\n'"It's a draw!")
if rps == 2 and compChoice == 2:
  print(scissors,'\n'"It's a draw!")
if rps == 0 and compChoice == 1:
  print(paper,'\n'"Computer Wins!")
if rps == 0 and compChoice == 2:
  print(rock, '\n'"You Win!")
if rps == 1 and compChoice == 2:
  print(scissors,'\n'"Computer Wins!")
if rps == 1 and compChoice == 0:
  print(paper, '\n'"You Win!")
if rps == 2 and compChoice == 0:
  print(rock,'\n'"Computer Wins!")
if rps == 2 and compChoice == 1:
  print(scissors, '\n'"You win!")