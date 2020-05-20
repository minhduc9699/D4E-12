from random import randint

random_num = randint(0, 100)
print(random_num)
if random_num < 30:
  print('Sunny!')
elif random_num < 60:
  print('Cloudy')
else:
  print('Rainy')