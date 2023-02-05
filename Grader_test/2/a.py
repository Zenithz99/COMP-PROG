def createdic(dic) :
    for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" :
        if (c in "AEILNORSTU") :
            dic[c] = 1
        elif (c in "DG") :
            dic[c] = 2
        elif (c in "BCMP") :
            dic[c] = 3
        elif (c in "FHVWY") :
            dic[c] = 4
        elif (c in "K") :
            dic[c] = 5
        elif (c in "JX") :
            dic[c] = 8
        elif (c in "QZ") :
            dic[c] = 10

def cal_score(word,dic) :
    score = 0
    for c in word :
        score += dic[c]
    return score
words = input().split()
dic = {}
createdic(dic)
list_word = []
for word in words :
    cur_score = cal_score(word,dic)
    list_word.append([word,cur_score])
    
list_word.sort(key=lambda x : x[0])    
list_word.sort(key=lambda x : x[1] , reverse=True)

for ans in list_word :
    print("{} {}".format(ans[0] , ans[1]))
