stores = ['cá sấu', 'khủng long', 'phi thuyền']

while True:
  choices = input('what u want to do? (c r u d)')
  if choices == 'c':
    new_item = input('what u want to add? ')
    stores.append(new_item)
    print(*stores)
  elif choices == 'r':
    print(*stores)
  elif choices == 'u':
    for index, value in enumerate(stores):
      print(index+1, value)
    update_index = int(input('enter the position u want to make change'))
    update_value = input('enter new value')
    stores[update_index-1] = update_value
    print(*stores)
  elif choices == 'd':
    for index, value in enumerate(stores):
      print(index+1, value)
    delete_index = int(input('enter the position u want to delete'))
    stores.pop(delete_index-1)
    print(*stores)
  else:
    break