import random
run='Y'
while run=='Y':
  

    dice1=random.randint(1,7)
    dice2=random.randint(1,7)
    print(f"Dice1: {dice1}")
    print(f"Dice2: {dice2}")
    
    run=input("Roll the dice again? (Y/N)")
   