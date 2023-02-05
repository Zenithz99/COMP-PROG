filename = input().strip()
f = open(filename,'r')

def createdict() :
    code = f.readline()
    dic = {}
    word = ""
    key = ""
    val = ""
    for c in code :
        if c == "["  :
            if key == "" : continue
            val = word
            dic[key] = val
            word = ""
        elif c == "]" :
            key = word
            word = ""
        else :
            word += c
    return dic
def swapdic(dic) :
    new_d = {}
    for key,val in dic.items() :
        new_d[val] = key
    return new_d

command = f.readline().strip()
if (command == "T2M" or command == "M2T") : 
    d = createdict()
    if (command == "M2T") : d = swapdic(d)
    line = f.readline().strip()
    while line != "" :
        words = line.strip().split() if (command == "M2T") else line.strip()
        out = ""
        flag = True
        for word in words :
            if word not in d :
                print("Invalid : {}".format(line))
                flag = False
                break
            out += d[word] + (" " if (command == "T2M") else "")
        if (flag) : print(out.strip())
        line = f.readline().strip()
else :
    print("Invalid code")