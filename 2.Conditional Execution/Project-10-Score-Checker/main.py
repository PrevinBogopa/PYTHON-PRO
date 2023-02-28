try:
  score=float(input("Enter score: "))
  if score < 0.0 or score > 1.0:
    raise ValueError
except:
  print("Bad score")
else:
  grade={
    'A' : float(0.9), 
    'B' : 0.8,
    'C' : 0.7, 
    'D' : 0.6, 
    'F' : 0.5,
  }
  for key in grade:
    if score >= grade[key]:
      print(key)
      break

finally:
  print("Thanks for using")
