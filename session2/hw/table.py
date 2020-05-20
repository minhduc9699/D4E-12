for y in range(1, 10):
  for x in range(1, 10):
    if x*y >= 10:
      print(x*y, end=" ")
    else:
      print(x*y, end="  ")
  print()