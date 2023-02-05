n = int(input())
pak_list = []
pak_person = {}
for i in range(n) :
    inp = input().strip()
    pak_list.append(inp)
    pak_person[inp] = []

n = int(input())
for i in range(n) :
    inp = input().strip().split()
    pak = inp[1]
    person = inp[0]
    pak_person[pak].append(person)
n = int(input())
person_vote = {}
for i in range(n) :
    inp = input().strip().split()
    person = inp[0]
    vote = inp[1]
    person_vote[person] = vote

for pak in pak_list :
    vote_list = {'Y' : [] , 'N' : [] , 'X' : []}
    print(pak)
    for person in pak_person[pak] :
        if person in person_vote :
            cur_vote = person_vote[person]
            if cur_vote == 'Y' :
                vote_list['Y'].append(person)
            elif cur_vote == 'N' :
                vote_list['N'].append(person)
            elif cur_vote == 'X' :
                vote_list['X'].append(person)
    maxlen = len(vote_list['Y'])
    max2 = False
    cur_max = 'Y'
    for c in "NX" :
        if len(vote_list[c]) > maxlen :
            maxlen = len(vote_list[c])
            cur_max = c
            max2 = False
        elif len(vote_list[c]) == maxlen :
            max2 = True
    #print(maxlen , cur_max , max2)
    if (max2) :
        print("Inconclusive")
    else :
        cobra = []
        for c in "YNX" :
            if c == cur_max : continue
            cobra = cobra + vote_list[c]
        if (len(cobra) == 0) :
            print("No cobra")
        else :
            cobra.sort()
            print(", ".join(cobra))
