import random
print ("Let's play Gun vs Snake vs Water")
options = ["Gun", "snake", "Water"]
user = input("Enter your choice: ")
computer = random.choice(options)
print("Opponent choice is :",computer)
if user == computer:
  print("Draw,Try again!")
elif user == "Gun" and computer == "snake":
  print("You win")
elif user == "snake" and computer == "Water":
  print("you win")
elif user == "Water" and computer == "Gun":
  print("you win")
else:
  print("You lose")

