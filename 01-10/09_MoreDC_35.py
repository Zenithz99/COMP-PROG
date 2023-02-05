def check(key,inp) :
    if key == -1 : return True
    return inp == key

n = int(input())
datas = [] # name group gen class
for t in range(n) :
    inp = input().split()
    datas.append(inp)
inp = input().split()
keyname = -1
keygroup = -1
keygen = -1
keyclass = -1
for item in inp :
    if len(item) == 1 or item == "Dog":
        keygroup = item
    elif '0' <= item[0] <= '9' :
        keygen = item
    elif item.upper() == item :
        keyclass = item
    else :
        keyname = item
out = []
for data in datas :
    if check(keyname,data[0]) and check(keygroup,data[1]) and check(keygen,data[2]) and check(keyclass,data[3]) :
        out.append(data)

if len(out) == 0 :
    print("Not Found")
else :
    out.sort(key= lambda x : x[0])
    for data in out :
        print(data[0],data[1],data[2],data[3])
