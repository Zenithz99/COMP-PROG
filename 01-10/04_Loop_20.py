minZig = None
maxZig = None
minZag = None
maxZag = None
i = 0
while True :
    inp = input().split(" ")
    if (inp[0] == "Zig-Zag") :
        print(minZig,maxZig)
        break
    elif (inp[0] == "Zag-Zig"):
        print(minZag,maxZag)
        break
    
    n1 = int(inp[0])
    n2 = int(inp[1])
    if minZig == None : minZig = n1
    else : 
        if i%2 == 0 :
            minZig = min(minZig,n1)
        else :
            minZig = min(minZig,n2)
    if maxZig == None : maxZig = n2
    else : 
        if i%2 == 0 :
            maxZig = max(maxZig,n2)
        else :
            maxZig = max(maxZig,n1)
    if maxZag == None : maxZag = n1
    else : 
        if i%2 == 0 :
            maxZag = max(maxZag,n1)
        else :
            maxZag = max(maxZag,n2)
    if minZag == None : minZag = n2
    else : 
        if i%2 == 0 :
            minZag = min(minZag,n2)
        else :
            minZag = min(minZag,n1)

    i += 1
    
