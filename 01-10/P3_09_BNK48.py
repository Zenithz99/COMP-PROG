inp = "-1"
p_vote = {} # p : {b : score}
b_voted = {} # b : [p]
b_score = {} # b : score
b_max_cnt = {} # b : cnt_kami
bnk_list = []
out = True
while out :
    inp = input()
    if (inp not in "123") :
        inp = inp.split()
        peo = inp[0]
        bnk = inp[1]
        vote = int(inp[2])

        if peo not in p_vote :
            p_vote[peo] = {}
        if bnk not in p_vote[peo] :
            p_vote[peo][bnk] = vote
        else : 
            p_vote[peo][bnk] += vote

        if bnk not in b_voted :
            b_voted[bnk] = [peo]
        elif peo not in b_voted[bnk] : b_voted[bnk].append(peo) 
        
        if bnk not in b_score :
            b_score[bnk] = vote
        else : b_score[bnk] += vote

        if bnk not in b_max_cnt :
            b_max_cnt[bnk] = 0


    else :
        if inp == '1' :
            for b in b_score :
                bnk_list.append([b , b_score[b]])
        elif inp == '2' :
            for b in b_voted :
                bnk_list.append([b , len(b_voted[b])])
                #print(b , b_voted[b])
        elif inp == '3' :
            #print(p_vote)
            for peo in p_vote :
                Max = 0
                kami = None
                for b in p_vote[peo] :
                    if p_vote[peo][b] > Max :
                        Max = p_vote[peo][b]
                        kami = b
                    elif p_vote[peo][b] == Max and b < kami :
                        kami = b
                if kami == None : continue
                b_max_cnt[kami] += 1
            
            for b in b_max_cnt :
                bnk_list.append([b , b_max_cnt[b]])
        bnk_list.sort(key=lambda x : x[1] , reverse=True)
        top = []
        for i in range(3) :
            top.append(bnk_list[i][0])
        print(", ".join(top))
        #print(bnk_list)
        out = False