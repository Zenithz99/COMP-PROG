n = int(input())
dic = {}
for i in range(n) :
    inp = input().split()
    dic[inp[0]] = inp[1]

inp = input().split()
while inp[0] != "q" :
    flag = True
    cur1 = []
    for p in inp:
        if p not in dic or dic[p] in cur1 :
            flag = False
            break
        cur1.append(dic[p])
                
    if (flag) :
        print("OK")
    else :
        print("Not OK")


    inp = input().split()