def cal(num) :
    m = num % 1
    if m == 0 :
        return int(num)
    else :
        return num
n = int(input())
acc = {}
for i in range(n) :
    inp = input().split()
    acc[inp[1]] = [inp[0] , float(inp[2])]
inp = input().split()
while (inp[0] != "exit") :
    accname = inp[0]
    accnum = inp[1]
    dir = inp[2]
    if dir == "deposit" :
        val = float(inp[3])
        if (accnum not in acc) :
            acc[accnum] = [accname , val]
        elif (acc[accnum][0] != accname) :
            print("Transaction Failed")
            inp = input().split()
            continue    
        else :
            acc[accnum][1] += val
        print("{} ({}) {}".format(acc[accnum][0] , accnum , cal(acc[accnum][1])))
    elif dir == "withdraw" :
        val = float(inp[3]) 
        if (accnum not in acc or acc[accnum][0] != accname or acc[accnum][1] < val) :
            print("Transaction Failed")
            inp = input().split()
            continue
        acc[accnum][1] -= val
        print("{} ({}) {}".format(acc[accnum][0] , accnum , cal(acc[accnum][1])))
    elif dir == "transfer" :
        target = inp[3]
        val = float(inp[4])
        if (accnum not in acc or acc[accnum][0] != accname or acc[accnum][1] < val or target not in acc) :
            print("Transaction Failed")
            inp = input().split()
            continue
        acc[accnum][1] -= val
        acc[target][1] += val
        print("{} ({}) {}".format(acc[accnum][0] , accnum , cal(acc[accnum][1])))
        print("{} ({}) {}".format(acc[target][0] , target , cal(acc[target][1])))
        

    inp = input().split()