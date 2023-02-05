n = int(input())
to_num = {}
to_name = {}
for i in range(n) :
    inp = input().strip().split()
    name,num = inp[0]+" "+inp[1] ,inp[2]
    to_name[num] = name
    to_num[name] = num
m = int(input())
for i in range(m) :
    inp = input().strip()
    out = ""
    if inp in to_name.keys() : out = to_name[inp]
    elif inp in to_num.keys() : out = to_num[inp]
    else : out = "Not found"
    print("{} --> {}".format(inp,out))