import math as ma
PI = ma.pi
inp = input()
spl = inp.split(" ")
bd = int(spl[0])
bm = int(spl[1])
by = int(spl[2])-543
d = int(spl[3])
m = int(spl[4])
y = int(spl[5])-543
diff_front = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
month = [31,28,31,30,31,30,31,31,30,31,30,31]
t = 0
if y - by >= 0 :
    t = 365 - diff_front[bm-1]
    if by %100 == 0 and by % 400 == 0 and bm <= 2: t+=1
    elif by % 4 == 0 and by % 100 != 0 and bm <= 2: t+=1
    t = t - bd + 1
    print(t)

if y - by >= 1 :
    t += diff_front[m-1]
    if y %100 == 0 and y % 400 == 0 and m >= 2: t+=1
    elif y % 4 == 0 and y % 100 != 0 and m >= 2: t+=1
    t += d - 1
    print(t)
if y - by > 1 :
    t += 365 * (y - by - 1)

print("{} {:.2f} {:.2f} {:.2f}".format(t,ma.sin(2*PI*t/23),ma.sin(2*PI*t/28),ma.sin(2*PI*t/33)))