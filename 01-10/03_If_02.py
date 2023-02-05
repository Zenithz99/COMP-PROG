def chartoint(a) :
    if a == "A" : 
        return 5
    if a == "B" : 
        return 4
    if a == "C" : 
        return 3
    if a == "D" : 
        return 2
    if a == "E" : 
        return 1
    return 0

def findwhomax(a,b,id1,id2) :
    if a > b :
        print(id1)
    if b > a :
        print(id2)

n1 = input()
n2 = input()
l1 = n1.split(" ")
l2 = n2.split(" ")

id1 = l1[0]
id2 = l2[0]
pass1 = False
pass2 = False
cal11 = chartoint(l1[3])
cal12 = chartoint(l2[3])
cal21 = chartoint(l1[4])
cal22 = chartoint(l2[4])

if l1[2] == "A" and  cal11 >= 3 and cal21 >= 3:
    pass1 = True
if l2[2] == "A" and  cal12 >= 3 and cal22 >= 3:
    pass2 = True

if pass1 and pass2 :
    gpax1 = float(l1[1])
    gpax2 = float(l2[1])
    if gpax1 == gpax2 :
        if cal12 == cal11 :
            if cal22 == cal21 :
                print("Both")
            else :
                findwhomax(cal21,cal22,id1,id2)
        else :
            findwhomax(cal11,cal12,id1,id2)
    else :
        findwhomax(gpax1,gpax2,id1,id2)
else :
    if pass1 :
        print(id1)
    if pass2 :
        print(id2)
    if not pass1 and not pass2 :
        print("None")