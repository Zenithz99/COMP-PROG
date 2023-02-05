import math as m
inp = input()
l = inp.split(",")

l1 = l[0]
l2 = "0" + l[1]
l3 = l[2]

up = int(l2+l3) - int(l2)
down = int("9"*len(l3) + "0"*len(l[1]))
up += int(l1) * down

g = m.gcd(up,down)
up = up//g
down = down//g

print(str(up) + " / " + str(down))

# 0,4,57
