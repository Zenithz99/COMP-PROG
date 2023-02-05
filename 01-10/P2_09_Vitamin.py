n = int(input())
li = []
for i in range(n) :
    inp = input()
    li.append(inp.split())

command = input().split()
if (command[0] == "show") :
    for i in range(n) :
        out = ""
        for j in range(len(li[0])) :
            out += li[i][j] + " "
        print(out.strip())
elif (command[0] == "get") :
    fin = command[1]
    found = False
    for i in range(n) :
        if (li[i][0] == fin) :
            out = ""
            for j in li[i] :
                out += j + " "
            print(out.strip())
            found = True
    if (not found) : print("{} not found".format(fin))
elif (command[0] == "avg") :
    idx = int(command[1])
    sum = 0
    for i in range(n) :
        val = float(li[i][idx])
        sum += val
    print(round(sum / n , 4))
elif (command[0] == "max") :
    idx = int(command[1])
    Max = 0
    out = []
    for i in range(n) :
        val = float(li[i][idx])
        if (val > Max) :
            out = []
            out.append(li[i][0])
            Max = val
        elif (val == Max) :
            out.append(li[i][0])
    out.sort()
    print("{} {}".format(out[0],Max))
elif (command[0] == "sort") :
    idx = int(command[1])
    li.sort(key=lambda x : x[0])
    li.sort(key=lambda x : x[idx])
    out = ""
    for item in li :
        out += item[0] + " "
    print(out)