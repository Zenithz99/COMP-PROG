def first_fit(L, e): # น ำ e ใสรำยกำรย่อยใ ่ น L ด ้วยวิธี first fit
    fit = False
    for idx,li in enumerate(L) :
        sum = 0
        for item in li :
            sum += item
            if (sum >= 100) : break
        if (sum + e <= 100) :
            L[idx].append(e)
            fit = True
        if (fit) : break
    if (not fit) :
        L.append([e])
def best_fit(L, e): # น ำ e ใสรำยกำรย่อยใ ่ น L ด ้วยวิธี best fit
    near = 0
    p = -1
    for idx,li in enumerate(L) :
        sum = 0
        for item in li :
            sum += item
            if (sum >= 100) : break
        if (sum + e <= 100) and (sum + e > near) :
            p = idx
            near = sum + e
    if (p == -1) :
        L.append([e])
    else :
        L[p].append(e)
def partition_FF(D): # คืนลิสต์ของลิสต์ที่ได ้จำกกำรแบ่งข ้อมูลใน D ด ้วย first fit
    out = []
    for item in D :
        first_fit(out,item)
    return out
def partition_BF(D): # คืนลิสต์ของลิสต์ที่ได ้จำกกำรแบ่งข ้อมูลใน D ด ้วย best fit
    out = []
    for item in D :
        best_fit(out,item)
    return out
exec(input().strip()) # ตอ้ งมคี ำสั่งนี้ ตรงนี้ตอนสง่ ให้Grader ตรวจ