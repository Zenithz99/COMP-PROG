def check(coun ,checker , dic_enem) :
    if checker in dic_enem and coun in dic_enem[checker] :
        return False
    elif coun in dic_enem and checker in dic_enem[coun] :
        return False
    return True


def add_enem(curr , targ , dic_enem , dic_ally) :
    if curr not in dic_enem :
        dic_enem[curr] = []
    if targ not in dic_enem :
        dic_enem[targ] = []
    ally_cur = dic_ally[curr] if curr in dic_ally else [curr]
    ally_targ = dic_ally[targ] if targ in dic_ally else [targ]
    for coun in ally_cur :
        if coun not in dic_enem :
            dic_enem[coun] = []
        dic_enem[coun] += ally_targ
    for coun in ally_targ :
        if coun not in dic_enem :
            dic_enem[coun] = []
        dic_enem[coun] += ally_cur

comm = input().split()
dic_ally = {}
dic_enem = {}
while comm[0] != "End" :
    if comm[0] == "Ally" :
        for coun in comm[1:] :
            ally = comm[1:]
            dic_ally[coun] = ally
    if comm[0] == "Enemy" :
        add_enem(comm[1] , comm[2] , dic_enem, dic_ally)
    if comm[0] == "Table" :
        table = comm[1:]
        flag = True
        for i in range(len(table)) :
            check1 = table[i-1] if i-1 >= 0 else table[-1]
            check2 = table[i+1] if i+1 < len(table) else table[0]
            if not (check(table[i] , check1 , dic_enem) and check(table[i] ,check2 , dic_enem)) :
                flag = False
                break
        if (flag) :
            print("Okay")
        else :
            print("No")
    comm = input().split()