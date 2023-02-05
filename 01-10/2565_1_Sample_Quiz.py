lists = [int(e) for e in input().split()]
k = int(input())
before = lists[0]
cntbefore = 1
total = 0
for i in range(1,len(lists)) :
    if lists[i] == before :
        cntbefore += 1
    else :
        if cntbefore < k :
            total += before * cntbefore
        before = lists[i]
        cntbefore = 1
if (cntbefore < k) :
    total += before * cntbefore
print(total)
