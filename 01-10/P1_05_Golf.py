import math as m
total_stroke = 0
total_par = 0
total_fixpar = 0
for i in range(9) :
    inp = input().split(" ")
    par = int(inp[0])
    stroke = int(inp[1])
    choose = int(inp[2])
  
    total_par += par
    total_stroke += stroke
    if choose == 1 : total_fixpar += min(par+2 , stroke)

tor = m.floor(0.8 * (1.5 * total_fixpar - total_par) )
final = total_stroke - tor
print(total_stroke)
print(tor)
print(final)