import random

while True:
  choices=["rock", "paper", "scissors"]

  computer=random.choice(choices)
  player=None

  while player not in choices: 
    player=input("rock, paper, or scissors?:")

  if player == computer:
   print("computer: ",computer)
   print("player: ",player)
   print("Tie!")

  elif player == "rock":
   if computer == "paper": 
     print("computer: ",computer)
     print("player: ",player)
     print("You Lose!") 
   if computer == "scissors": 
     print("computer: ",computer)
     print("player: ",player)
     print("You Win!")
  
  elif player == "scissors": 
    if computer == "rock":
      print("computer: ",computer)
      print("player: ",player)
      print("You Lose!")  
    if computer == "paper": 
      print("computer: ",computer)
      print("player: ",player)
      print("You Win!")  

  elif player == "paper":
     if computer == "scissors":
      print("computer: ",computer)
      print("player: ",player) 
      print("You Lose!") 
     if computer == "rock":
      print("computer: ",computer)
      print("player: ",player) 
      print("You Win!")  
  play_again = input("Play again? (yes/no): ") 
   
  if play_again != "yes":
       break

print("Bye!")      
