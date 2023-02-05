inp = input()
spl = inp.split(" ")
a = int(spl[0])
b = int(spl[1])
c = int(spl[2])
d = int(spl[3])

if a > b :
    a,b = b,a
    if d >= a :
        if c > d :
            c -= a
    else :
        c += a
    b = a + c + d
else :
    if c > a and a >= b :
        d += a
    if d > c :
        b += 2
    else :
        b *= 2

print("{} {} {} {}".format(str(a),str(b),str(c),str(d)))