def convex_polygon_area(p):
    area = 0
    cal_p = p
    cal_p.append(p[0])
    for i in range(len(cal_p)) :
        if (i+1 < len(cal_p)) : area += cal_p[i][0] * cal_p[i+1][1]
        if (i-1 >= 0) : area -= cal_p[i][0] * cal_p[i-1][1]
    return abs(area*0.5)
def is_heterogram(s):
    inp = s.lower()
    used = ""
    for char in inp :
        if not ('a' <= char <= 'z' or 'A' <= char <= 'Z') : continue
        if char in used : return False
        else : used += char
    return True
def replace_ignorecase(s, a, b):
    out = ""
    j = 0
    currword = ""
    for i in range(len(s)) :
        currword += s[i]
        if s[i].lower() == a[j].lower() :
            j += 1
            if j == len(a) :
                out += b
                j = 0
                currword = ""
        else :
            out += currword
            currword = ""
            j = 0
    if currword != "" : out += currword
    return out

def top3(votes):
    list_top = []
    for key,val in votes.items() :
        list_top.append([key,val])
    list_top.sort(key=lambda item: item[0])
    list_top.sort(key=lambda item: item[1],reverse=True)
    out = []
    for i in range(3) :
        out.append(list_top[i][0])
    return out

# ตอ้ งมคี ำสั่งข ้ำงล่ำงนี้ ตอนสง่ ให้Grader ตรวจ
for k in range(2):
    exec(input().strip())
