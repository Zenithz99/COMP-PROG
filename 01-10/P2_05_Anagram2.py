A = input()
B = input()
dicA = {}
dicB = {}
for c in A.lower() :
    if c not in "abcdefghijklmnopqrstuvwxyz" : continue
    if c not in dicA :
        dicA[c] = 1
    else :
        dicA[c] += 1
for c in B.lower() :
    if c not in "abcdefghijklmnopqrstuvwxyz" : continue
    if c not in dicB :
        dicB[c] = 1
    else :
        dicB[c] += 1
remove_a = []
remove_b = []
for c in "abcdefghijklmnopqrstuvwxyz" :
    if c not in dicA and c not in dicB : continue
    elif c in dicA and c not in dicB :
        remove_a.append((c,dicA[c]))
    elif c not in dicA and c in dicB :
        remove_b.append((c,dicB[c]))
    else :
        if (dicA[c] > dicB[c]) :
            remove_a.append((c,dicA[c] - dicB[c]))
        elif (dicB[c] > dicA[c]) :
            remove_b.append((c,dicB[c] - dicA[c]))
print(A)
if len(remove_a) == 0 : print (" - None")
else :
    for rem in remove_a :
        put = rem[0] if (rem[1] < 2) else rem[0] + "'s"
        print(" - remove {} {}".format(rem[1],put))
print(B)
if len(remove_b) == 0 : print (" - None")
else : 
    for rem in remove_b :
        put = rem[0] if (rem[1] < 2) else rem[0] + "'s"
        print(" - remove {} {}".format(rem[1],put))
