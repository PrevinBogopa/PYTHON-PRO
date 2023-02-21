import random

names=input("Enter names separated by ,")
list=names.split(",")
selected=random.choice(list)
print(f"{selected} is going to pay for the meal today!")
