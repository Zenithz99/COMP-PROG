n = int(input())
icecream = {}
for i in range(n) :
    key,val = [x for x in input().strip().split()]
    icecream[key] = int(val)
m = int(input())
top_sell_item = ""
top_sell_amount = 0
total_amount = 0
item_sell = {}
for i in range(m) :
    inp = input().split()
    item,amount = inp[0],int(inp[1])
    try :
        profit = float(icecream[inp[0]] * amount)
        if (item not in item_sell.keys()) : item_sell[item] = profit
        else : item_sell[item] += profit
        total_amount += profit
        top_sell_amount = max(top_sell_amount,item_sell[item])
    except :
        continue
if(item_sell == {}) : print("No ice cream sales")
else :
    list_sell_item = []
    for key,val in item_sell.items() :
        if (val == top_sell_amount) : list_sell_item.append(key)
    list_sell_item.sort()
    for item in list_sell_item : top_sell_item += item + ", "
    print("Total ice cream sales: {}".format(total_amount))
    print("Top sales: {}".format(top_sell_item[:-2]))
