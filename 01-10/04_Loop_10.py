import math as m
a = float(input())
L = 0
cnt = 0
tmp = a
while not tmp == 0 :
  tmp //= 10
  cnt += 1
U = cnt
x = (L+U) / 2
while not abs(a-pow(10,x)) <= pow(10,-10) * max(a,pow(10,x)) :
  if pow(10,x) > a :
    U = x
  elif pow(10,x)  <= a :
    L = x
  x = (L+U)/2
print(round(x,6))