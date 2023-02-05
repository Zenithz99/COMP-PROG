inp = input()
spl = inp.split(" ")
d = int(spl[0])
m = int(spl[1])
y = int(spl[2])

y -= 543
n = 31

end_with_yon = [False,False,False,True,False,True,False,False,True,False,True,False]
if end_with_yon[m-1] :
    n = 30
else :
    if m == 2 :
        n = 28
        if y % 400 == 0 :
            n = 29
        if y % 4 == 0 and not y % 100 == 0 :
            n = 29

d += 15
if d > n :
    d -= n
    m += 1
if m > 12 :
    m -= 12
    y += 1
y += 543

print("{}/{}/{}".format(str(d),str(m),str(y)))