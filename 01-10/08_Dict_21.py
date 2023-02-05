dic = {}
inp = input().lower()
for c in inp :
    if not ('a' <= c <= 'z' or 'A' <= c <= 'Z') : continue
    if (c not in dic.keys()) : dic[c] = 1
    else : dic[c] += 1
out = []
for key,val in dic.items() :
    out.append([key,val])
out.sort(key=lambda item: item[0])
out.sort(key=lambda item: item[1],reverse=True)
for key,val in out :
    print("{} -> {}".format(key,val))