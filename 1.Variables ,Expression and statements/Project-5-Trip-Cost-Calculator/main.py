# Trip Cost Calculator Project 

print("Welcome to the Trip Cost Calculator!")
numOfDays=int(input("How many days will you stay?"))
cost=int(input("How much does hotel cost per night? "))
flightCost=int(input("How much does flight cost?"))
carrent=int(input("If you need rental car please enter the price otherwise enter zero. "))
othercost=int(input("Enter other possible expenses  "))
## Output
total=float(numOfDays* cost+flightCost+carrent*numOfDays+othercost)
print(f"Total Cost: ${total}")
