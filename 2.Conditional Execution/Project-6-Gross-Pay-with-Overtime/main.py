hours=int(input("Enter Hours: "))
rate=int(input("Enter Rate: "))
overtime=0
if hours > 40 :
  overtime=float((hours-40)*1.5*rate)
  hours=40
total=float(overtime+rate*hours)

print(f"pay {total}")
