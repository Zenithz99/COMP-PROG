out = False
s1 , s2 = 0,0
dic = ['X','R','Y','G','W','B','P','K']
cur_color = 1
cnt_r = 0
while (not out) :
    inp = input()
    if (cur_color == 1) :
        cur_score = 0
        if (inp[1] == 'R') :
            cur_score += 1
            for idx , c in enumerate(dic) :
                if c == inp[2] :
                    cur_score += idx
                    break

        if inp[0] == '1' : s1 += cur_score
        else : s2 += cur_score

        if (cur_score >= 1) : cnt_r += 1
        if (cnt_r == 6) : cur_color += 1
    else :
        if (inp[1] == dic[cur_color]) :
            if inp[0] == '1' : s1 += cur_color
            else :  s2 += cur_color
            cur_color += 1
    if (cur_color == 8) : out = True
print(s1,s2)
if (s1 < s2) : print("Player 2 wins")
elif (s1 > s2) : print("Player 1 wins")
else : print("Tie")

