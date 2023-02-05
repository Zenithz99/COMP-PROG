dic = {0 : "soon" , 1 : "neung" , 2 : "song" , 3 : "sam" , 4 : "si" , 5 : "ha" , 6 : "hok" , 7 : "chet" , 8 : "paet" , 9 : "kao"}
def to_Thai( N ):
    out = ""
    if (N >= 1000) :
        f = N // 1000
        N %= 1000
        out += dic[f] + " "+ "pun" + " "
    if (N >= 100) :
        f = N // 100
        N %= 100
        out += dic[f] + " " + "roi" + " "
    if (N >= 10) :
        f = N // 10
        N %= 10
        if (f == 2) : out += "yi" + " " + "sip" + " "
        elif (f == 1) : out += "sip" + " "
        else : out += dic[f] + " " + "sip" + " "
    if (N == 0) :
        if (out == "") : out += dic[N]
    elif (N == 1 and out != "") : out += "et"
    else : out += dic[N] 
    return out

exec(input().strip())