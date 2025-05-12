import random

stone = '''
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

user_input=int(input("What  do you choose? Type 1 for Rock, 2 for Papaer, 3 for Scissor "))
index = random.randint(0,2)
element=[stone,paper,scissors]
print("Your choice:")
print(element[user_input-1])
print("compuer choice:")
print(element[index])
if element[user_input-1] == element[index]:
    print("It's a draw ")
elif(element[user_input-1] == "rock" and element[index]=="scissors") or(element[user_input-1] == "paper" and element[index]=="rock") or (element[user_input-1] == "scissors" and element[index]=="paper"):
    print("you win !")
else:
    print("you lose!")