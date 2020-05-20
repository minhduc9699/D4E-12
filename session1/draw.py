from turtle import *
shape('turtle')
speed(-1)

n = int(input())
for i in range(3, n+1):
  for j in range(i):
    forward(50)
    left(360/i)


mainloop()