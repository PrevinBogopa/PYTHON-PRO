
name1=input("Name 1 =")
name2=input("Name 2 =")
name=name1+name2
score1=0
score2=0

name=name.lower()
score1=name.count('t')
score1=name.count('r')+score1
score1=name.count('u')+score1
score1=name.count('e')+score1

score2=name.count('l')+score2
score2=name.count('o')+score2
score2=name.count('v')+score2
score2=name.count('e')+score2


score=score1*10+score2

print
if score <10 or score >85:
  print(f"Your score is {score}, you go together like coke and mentos.")

elif score>39 and score<71:
  print(f"Your score is {score}, you are alright together.")

else: 
  print(f"Your score is {score}.")
