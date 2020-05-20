name = 'trứng rán'
name1 = 'bắp'
name2 = 'bơ'
name3 = 'mỡ'
name4 = 'mắm tôm'
#list, array
mon_an = ['trứng rán', 'bắp', 'mỡ', 'bơ', 'mắm tôm', 'thịt chó'] #init
print(mon_an)
# print(mon_an)
# name = 'củ giềng'
mon_an.append(name) # CREATE
mon_an[0] = 'bạch tuộc' # UPDATE
# print(mon_an)
# for i in range(len(mon_an)):
#   print(i+1, mon_an[i]) # READ
mon_an.pop() # DELETE

# for index, value in enumerate(mon_an):
#   print(index+1, value)


# old_value = input('enter the value you want to edit')
# value = input('new value ')
# index = mon_an.index(old_value)
# mon_an[index] = value
# for index, value in enumerate(mon_an):
#   print(index+1, value)