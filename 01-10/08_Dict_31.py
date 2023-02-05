def total(pocket):
    sum = 0
    for key,val in pocket.items() :
        sum += int(val) * int(key)
    return sum
def take(pocket, money_in):
    for key,val in money_in.items() :
        if (key not in pocket.keys()) :
            pocket[key] = val
        else :
            pocket[key] += val
    return pocket
def remove(pocket, money_out) :
    for key,val in money_out.items() :
        pocket[key] -= val
def pay(pocket, amt):
    list_coin = []
    dic_pay = {}
    dic_before_pay = pocket
    for key,val in pocket.items() :
        list_coin.append([key,val])
    list_coin.sort(key=lambda item:item[0],reverse=True)
    for key,val in list_coin :
        if amt >= key:
            can_pay = min(amt // key,val)
            dic_pay[key] = can_pay
            amt -= can_pay*key
        if amt == 0 : break
    if (amt != 0) :
        return {}
    else :
        remove(pocket,dic_pay)
        return dic_pay
            

exec(input().strip()) 