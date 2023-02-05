n = int(input())
x = []
y = []
for i in range(n) :
    inp = input().split(" ")
    x.append(int(inp[0]))
    y.append(int(inp[1]))
command = input()
minn = 0
maxx = 0
if command == "Zig-Zag" :
    minn = x[0]
    maxx = y[0]
    for i in range(n) :
        if i % 2 == 0 :
            minn = min(minn,x[i])
            maxx = max(maxx,y[i])
        else :
            minn = min(minn,y[i])
            maxx = max(maxx,x[i])
elif command == "Zag-Zig" :
    minn = y[0]
    maxx = x[0]
    for i in range(n) :
        if i % 2 == 0 :
            minn = min(minn,y[i])
            maxx = max(maxx,x[i])
        else :
            minn = min(minn,x[i])
            maxx = max(maxx,y[i])
print(minn,maxx)