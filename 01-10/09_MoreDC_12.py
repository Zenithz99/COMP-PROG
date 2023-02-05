n = int(input())
m1 = {}
m2 = {}
for i in range(n) :
    inp = [int(e) for e in input().split()]
    new_m2 = {}
    for item in inp :
        if item not in m1 :
            m1[item] = 1
        else :
            m1[item] += 1
        
        if i == 0 :
            m2[item] = 1
        else :
            if item in m2 :
                new_m2[item] = 1
    if(i != 0) : m2 = new_m2
print(len(m1) , len(m2))