def f1(a, b, c):
    minn = 1001
    if (a > 0) : minn = min(a,minn)
    if (b > 0) : minn = min(b,minn)
    if (c > 0) : minn = min(c,minn)
    return minn
def f2(a, b, c):
    maxx = -1001
    if (a < 0) : maxx = max(a,maxx)
    if (b < 0) : maxx = max(b,maxx)
    if (c < 0) : maxx = max(c,maxx)
    return maxx
def f3(a, b, c):
    sum = abs(a + b + c)
    while (sum >= 10) :
        sum //= 10
    return sum
def f4(a, b, c):
    sum = abs(a+b+c)
    return sum%10
def main():
    s1,s2,a,b,c = [int(e) for e in input().split()]
    if (s1 == 0 and s2 == 0) :
        print(f1(a,b,c))
    elif (s1 == 0 and s2 == 1) :
        print(f2(a,b,c))
    elif (s1 == 1 and s2 == 0) :
        print(f3(a,b,c))
    elif (s1 == 1 and s2 == 1) :
        print(f4(a,b,c))
    else :
        print("Error")

exec(input().strip()) # DON'T remove this line

#print(f3(-1,-1,-8))