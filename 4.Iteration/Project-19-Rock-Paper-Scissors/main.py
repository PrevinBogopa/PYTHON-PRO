import random 
play='Y'
while play=='Y':
  options=("rock", "paper", "scissors")
  user=input(print("Enter a choice (rock, paper, scissors):"))
  
  computer=random.choice(options)

  if user == computer:
    print(f"You chose {user} ,computer chose {computer} ,its a draw")
  if user=="paper" and computer=="scissors":
    print("You chose paper, computer chose scissors.")
    print("Scissors cuts paper! You lose.")

  if user=="scissors" and computer=="rock":
    print("You chose scissors, computer chose rock.")
    print("rock beats scissors You lose.")
 
  if user=="rock" and computer=="paper":
    print(f"You chose rock, computer chose paper")
    print("Paper covers rock! You lose.")

  if user=="paper" and computer=="rock":
    print(f"You chose paper, computer chose rock")
    print("Paper covers rock! You win.")
    
  if user=="scissors" and computer=="paper":
    print(f"You chose scissors, computer chose paper")
    print("Scissors cuts paper! You win.")

  if user=="rock" and computer=="scissors":
    print(f"You chose rock, computer chose scissors")
    print("rock breaks scissors You win.")
  play=input("Play again (Y/N)?")   

