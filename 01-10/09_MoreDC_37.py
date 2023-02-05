n = int(input())
max_class = {}
for t in range(n) :
    inp = input().split()
    max_class[inp[0]] = int(inp[1])

m = int(input())
datas = []
for t in range(m) :
    inp = input().split()
    inp[1] = float(inp[1])
    datas.append(inp)
id_class = []
datas.sort(key=lambda x : x[1],reverse=True)
for data in datas :
    for i in range(2,len(data)) :
        if max_class[data[i]] != 0 :
            id_class.append([data[0],data[i]])
            max_class[data[i]] -= 1
            break
id_class.sort(key=lambda x : x[0])
for id,clas in id_class :
    print(id,clas)