
noerror=True
try :  
  hours=int(input("Enter Hours:"))
  if noerror:
    noerror=False
    rate=int(input("Enter Rate:"))
  
except:
  if noerror==True:
    print("Error, please enter numeric input for Hours")
  else:
    print("Error, please enter numeric input for Rate")
else:
  total=float(rate*hours)
  print(f"pay {total}")
finally:
  print("Thanks for using")
  