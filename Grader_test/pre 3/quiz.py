n = int(input())
played = {} # played[song] = [rating , score ,rating]
for i in range(n) :
    inp = input().split(" | ")
    if (inp[0] == "Play") :
        song_name = inp[1]
        song_lvl = int(inp[2])
        score = int(inp[3])
        rating = int( 25 * (song_lvl + 1) * (score / 10**7))
        played[song_name] = [song_lvl , score , rating]
    if (inp[0] == "Rating") :
        if (len(inp) == 1) :
            out = [[played[e][2] , e] for e in played]
            out.sort(key=lambda x : x[0],reverse=True)
            out = out[:5]
            sum = 0
            for i in range(len(out)) : sum += out[i][0]
            print(sum)
        else :
            tar = inp[1]
            if (tar not in played) :
                print("0")
            else :
                print(played[tar][2])
    if (inp[0] == "Detail") :
        tar = inp[1]
        if (tar not in played) :
            print("{} : No play history".format(tar))
        else :
            print("{} | {} | {} | {}".format(tar , played[tar][0] , played[tar][1] , played[tar][2]))