def reverse(d):
 # d เป็น dict ที่มี value ไม่ซ ้ำกนั
 # คืน dict ใหม่ที่เก็บ key,value ที่ค่ำเป็น value,key ของ d ที่ได ้รับ
    reverse_d = {}
    for key,val in d.items() :
        reverse_d[val] = key
    return reverse_d

def keys(d, v):
 # คืนลิสต์ที่เก็บค่ำของ keys ใน d (เรียงยังไงก็ได ้) ที่มีค่ำ value เท่ำกับ v
    out = []
    for key,val in d.items() :
        if (val == v) :
            out.append(key)
    return out
exec(input().strip()) 