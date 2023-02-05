d = int(input())
m = int(input())
y = max(int(input()) - 543,0)

t = 0
if m > 1:
    t += 31
if m > 2:
    if y%4 == 0 : t += 29
    else : t += 28
if m > 3:
    t += 31
if m > 4:
    t += 30
if m > 5:
    t += 31
if m > 6:
    t += 30
if m > 7:
    t += 31
if m > 8:
    t += 31
if m > 9:
    t += 30
if m > 10:
    t += 31
if m > 11:
    t += 30

t += d
print(t)
