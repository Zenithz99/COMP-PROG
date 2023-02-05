def is_odd(n):
 # คืน (True/False) ว่า n เป็นจ านวนคี่หรือไม่
    return True if n%2 == 1 else False
def has_odds(x):
 # คืน (True/False) ว่า x เป็นลิสต์ที่มีข ้อมูลบางตัวเป็นจ านวนคี่
    for num in x :
        if is_odd(num) : return True
    return False
def all_odds(x):
 # คืน (True/False) ว่า x เป็นลิสต์ที่มีข ้อมูลทุกตัวเป็นจ านวนคี่
    for num in x :
        if not is_odd(num) : return False
    return True
def no_odds(x):
 # คืน (True/False) ว่า x เป็นลิสต์ที่มีไม่มีข ้อมูลที่เป็นจ านวนคี่เลย
    for num in x :
        if is_odd(num) : return False
    return True
def get_odds(x):
 # คืนลิสต์ที่มีจ านวนคี่ที่มีเก็บในลิสต์ x (ล าดับก่อนหลังให ้เป็นไปตามล าดับเดียวกับใน x)
 # เชน่ x = [1,2,3,5,0] จะได ้ผลคือ [1,3,5]
    odd_list = []
    for num in x :
        if is_odd(num) : odd_list.append(num)
    return odd_list
def zip_odds(a, b):
 # คืนลิสต์ที่สร้างจากการน าจ านวนคี่ใน a และ b มาสลับกันเก็บในลิสต์ผลลัพธ์ (เริ่มจากใน a ก่อน)
 # เชน่ a = [0,8,1,2,4,6,5,7,9,2,3] กับ b = [4,19,11,12,10,17] จะได ้คือ
 # [1,19,5,11,7,17,9,3]
    odd_a = get_odds(a)
    odd_b = get_odds(b)
    i = 0
    j = 0
    odd_out = []
    while (i < len(odd_a) or j < len(odd_b)) :
        if (i == len(odd_a)) : 
            odd_out.append(odd_b[j])
            j += 1
        elif (j == len(odd_b)) :
            odd_out.append(odd_a[i])
            i += 1
        else :
            if len(odd_out)%2 == 0 :
                odd_out.append(odd_a[i])
                i += 1
            else :
                odd_out.append(odd_b[j])
                j += 1
    return odd_out
exec(input().strip()) # ตอ้ งมคี าสั่งนี้ ตรงนี้ตอนสง่ ให้Grader ตรวจ