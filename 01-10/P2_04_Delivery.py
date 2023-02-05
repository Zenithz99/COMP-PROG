dic = {"E" : 1,"Q" : 3,"N" : 7,"F" : 14}
def find_max_d(m,y) :
    max_d = 30 if (m in ["4","6","9","11"]) else 31
    y_c = int(y)-543
    if (m == "2") :
        max_d = 29 if (y_c%400 == 0 or (y_c%4==0 and y_c%100!=0)) else 28
    return max_d
def find_error(d,m,y,ex) :
    if (y < "2558") : return "Invalid year"
    if not (1 <= int(m) <= 12) : return "Invalid month"
    max_d = find_max_d(m,y)
    if not (1 <= int(d) <= max_d) : return "Invalid date"
    if ex not in "EQNF" : return "Invalid delivery type"
    return ""
def add_date(d,m,y,ex) :
    new_d = int(d) + dic[ex]
    new_m = int(m)
    new_y = int(y)
    max_d = find_max_d(m,y)
    if (new_d > max_d) :
        new_d %= max_d
        new_m += 1
        if (new_m > 12) :
            new_m %= 12
            new_y += 1
    return new_d,new_m,new_y
inp = input()
list_out = []
while inp != "END" :
    queue_num,express,d,m,y = inp.strip().split()
    error = find_error(d,m,y,express)
    if (error == "") :
        dd,dm,dy = add_date(d,m,y,express)
        list_out.append((dy,dm,dd,queue_num))
    else :
        print("Error: {} --> {}".format(inp,error))
    inp = input()
list_out.sort()
for tup in list_out :
    y,m,d,q = tup
    print("{}: delivered on {}/{}/{}".format(q,d,m,y))
    