sheep_flocks = [5, 7, 300, 90, 24, 50, 75]
for i in range(4):
  print('month', i+1)
  max_sheep = sheep_flocks[0]
  for sheep in sheep_flocks:
    if sheep > max_sheep:
      max_sheep = sheep
  max_index = sheep_flocks.index(max_sheep)
  sheep_flocks[max_index] = 8
  print(sheep_flocks)
  for index, sheep in enumerate(sheep_flocks):
    sheep_flocks[index] = sheep + 50
  print(sheep_flocks)
total_size = 0
for sheep in sheep_flocks:
  total_size = total_size + sheep
total_money = total_size * 2
print(total_money, '$')
