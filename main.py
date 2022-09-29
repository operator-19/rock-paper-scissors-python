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

gameImg = [rock, paper, scissors]

userChoice = int(input('What do you choose? Type 0 for rock, 1 for Paper or 2 for Scissors.\n'))

if userChoice >= 3 or userChoice < 0:
  print('Invalid input!')
else:
  print(gameImg[userChoice])

  computerChoice = random.randint(0,2)
  
  print(f'Computer chose {computerChoice}{gameImg[computerChoice]}')
  
  if userChoice == 0 and computerChoice == 2:
    print('You Win!')
  elif computerChoice > userChoice: 
    print('You Lose!')
  elif computerChoice < userChoice: 
    print('You Win!')
  elif userChoice == computerChoice:
    print('Draw!')
  
