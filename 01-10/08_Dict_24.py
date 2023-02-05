def create_dic() :
    dic = {}
    start = 1
    multi = 1
    dic[" "] = '0'
    for char in "abcdefghijklmnopqrstuvwxyz" :
        if char in "adgjmptw" :
            start += 1
            multi = 1
        dic[char] = str(start) * multi
        multi += 1
    #print(dic)
    return dic
def reverse_dic(dic) :
    new_dic = {}
    for key,val in dic.items() :
        new_dic[val] = key
    return new_dic

to_keys = create_dic()
to_text = reverse_dic(to_keys)
def text2keys( text ):
    text = text.lower()
    out = ""
    for char in text :
        if 'a' <= char <= 'z' or char == ' ' :
            out += str(to_keys[char]) + " "
    return out.strip()
def keys2text( keys ):
    out = ""
    inp = keys.split()
    #print(to_text)
    for key in inp :
        out += to_text[key]
    return out
# ตอ้ งมคี ำสั่งข ้ำงล่ำงนี้ ตอนสง่ ให้Grader ตรวจ

exec(input().strip())