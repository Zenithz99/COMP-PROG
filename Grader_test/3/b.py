n,m,k = [int(e) for e in input().split()]
ban_fac = {}
for i in range(n) :
    inp = input().split()
    ban_fac[inp[0]] = inp[1]

kaek_fac = {}
for i in range(m) :
    inp = input().split()
    kaek = inp[0]
    if kaek not in kaek_fac :
        kaek_fac[kaek] = []
    for friend in inp[1:] :
        if ban_fac[friend] not in kaek_fac[kaek] :
            kaek_fac[kaek].append(ban_fac[friend])

for i in range(k) :
    inp = input().split()
    cur = kaek_fac[inp[0]]
    for p in inp[1:] :
        vis = kaek_fac[p]
        newcur = []
        for fac in vis :
            if fac in cur :
                newcur.append(fac)
        cur = newcur
    if len(cur) == 0 :
        print("None")
    else :
        print(" ".join(sorted(cur)))