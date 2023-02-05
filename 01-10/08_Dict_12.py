n = int(input())
to_nickname = {}
to_surname = {}
for i in range(n) :
    surname , nickname = [x for x in input().strip().split()]
    to_nickname[surname] = nickname
    to_surname[nickname] = surname
m = int(input())
out_list = []
for i in range(m) :
    out = ""
    inp = input().strip()
    try :
        out = to_nickname[inp]
    except :
        pass
    try :
        out = to_surname[inp]
    except :
        pass
    if (out == "") : print("Not found")
    else : print(out)
