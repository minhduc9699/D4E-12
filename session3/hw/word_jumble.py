from random import shuffle, randint, choice

word = 'champion'
list_word = list(word)
# another_list_word = word.split(',')
shuffle(list_word)
# temp = list_word[0]
# list_word[0] = list_word[1]
# list_word[1] = temp
for char in list_word:
  print(char, end=' ')