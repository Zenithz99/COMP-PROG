n = int(input())
dic_item = {}
dic_bidder = {}
bidder_list = []
for r in range(n) :
    inp = input().split()
    if (inp[0] not in "BW") : continue
    bidder = inp[1]
    item = inp[2]
    if (inp[0] == 'B') : price = int(inp[3])
    if bidder not in bidder_list :
        bidder_list.append(bidder)
        dic_bidder[bidder] = [0 , []]

    if inp[0] == 'B' :
        if item not in dic_item :
            dic_item[item] = []
        bidded = False
        for i in range(len(dic_item[item])) :
            bid = dic_item[item][i]
            if bid[0] == bidder :
                dic_item[item].pop(i)
                dic_item[item].append([bidder , price])
                bidded = True
                break
        if not bidded :
            dic_item[item].append([bidder , price])
    elif inp[0] == 'W' :
        for i in range(len(dic_item[item])) :
            if dic_item[item][i][0] == bidder :
                dic_item[item].pop(i)
                break

for item in dic_item :
    cur_max = 0
    winner = None
    for bid in dic_item[item] :
        if bid[1] > cur_max :
            cur_max = bid[1]
            winner = bid[0]
    
    if (winner == None) : continue
    dic_bidder[winner][0] += cur_max
    dic_bidder[winner][1].append(item)

bidder_list.sort()
for bidder in bidder_list :
    pay = dic_bidder[bidder][0]
    list_pay = sorted(dic_bidder[bidder][1])
    if (pay == 0) : print("{}: ${}".format(bidder,pay))
    else : print("{}: ${} -> {}".format(bidder,pay, " ".join(list_pay)))



