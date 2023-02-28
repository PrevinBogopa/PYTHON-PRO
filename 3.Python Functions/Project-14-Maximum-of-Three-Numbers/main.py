def max_of_three(n1,n2,n3):
  if n1>n2 and n1>n3:
    return n1
  elif n2>n1 and n2>n3:
    return n1
  else:
    return n3

max_value = max_of_three(4, 5, 3)

print("The maximum value is:", max_value)