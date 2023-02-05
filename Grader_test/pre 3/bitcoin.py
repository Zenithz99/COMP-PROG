line = int(input())
data = []
for i in range(line) :
    inp = [float(e) for e in input().split(",")]
    data += inp
fast = [-1] * len(data)
slow = [-1] * len(data)
sum = 0.0
buy = -1
sell = -1
dir = 0 # 0 : fast > slow , 1 : fast < slow
out = []
for i in range(len(data)) :
    sum += data[i]
    if (i == 6) :
        fast[i] = (1/7 * sum)
    if (i == 13) :
        slow[i] = (1/14 * sum)
    
    
    if (i > 6) :
        a1 = 2 / (1 + 7)
        fast[i] = a1 * data[i] + fast[i-1] * (1-a1)
    if (i > 13) :
        a2 = 2 / (1 + 14)
        slow[i] = a2 * data[i] + slow[i-1] * (1-a2)
    
    if (i == 13) :
        if (fast[i] < slow[i]) :
            dir = 1
        else :
            dir = 0
    else :
        if (fast[i] > slow[i] and dir == 1) :
            out.append(['BUY' , data[i]])
            dir = 0
            print(i , fast[i] , slow[i])
        elif (fast[i] < slow[i] and dir == 0) :
            out.append(['SELL' , data[i]])
            dir = 1
            print(i , fast[i] , slow[i])
if (len(out) == 0) :
    print("No results")
else :
    for data in out :
        print("{} at {:.2f}".format(data[0] , data[1]))
