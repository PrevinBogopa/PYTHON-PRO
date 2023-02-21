def checkLeap(year):
 
  if year %4 ==0:
    then="Leap Year"
    if year %100==0:
      then="Not leap Year"
      if year % 400 ==0:
        then="Leap Year"
  else:
    then="Not leap Year"
  print(f"{then}")

year=int(input())
checkLeap(year)