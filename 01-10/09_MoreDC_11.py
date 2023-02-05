n = int(input())
for i in range(n) :
    inp = input()
    if (len(inp) > 0 and inp[0] == '.') :
        out = ""
        cnt = 0
        for j in range(len(inp)) :
            if (inp[j] == '.') : cnt += 1
            else : break
        out += ('.' * (cnt // 2) ) + inp[cnt:]
        print(out)
    else :
        print(inp)