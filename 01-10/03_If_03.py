inp = input()
spl = inp.split(" ")
n1 = float(spl[0])
n2 = float(spl[1])
n3 = float(spl[2])
n4 = float(spl[3])

sum = n1+n2+n3+n4
maxx = n1
minn = n1

if maxx < n2 : maxx = n2
if minn > n2 : minn = n2
if maxx < n3 : maxx = n3
if minn > n3 : minn = n3
if maxx < n4 : maxx = n4
if minn > n4 : minn = n4

sum -= maxx + minn
print(round(sum/2,2))
