def chartoint(a) :
    if a == "A" : 
        return 5
    if a == "B" : 
        return 4
    if a == "C" : 
        return 3
    if a == "D" : 
        return 2
    if a == "F" : 
        return 1
    return 0

def findwhomax(a,b,id1,id2,out) :
    if a > b :
        out.append(id1)
    if b > a :
        out.append(id2)
        
def choose(stu1, stu2):
 # stu1 และ stu2 เป็นลิสต์[ ID, GPAX, compprog, cal1, cal2 ]
 # ID เป็นสตริงเก็บเลขประจ ำตัว
 # GPAX เป็น float
 # comprog, cal1, cal2 เป็นสตริงเก็บเกรดของสำมวิชำ (เกรดเป็นแบบไม่มีประจุ A,B,C,D,F)
 # ฟังกช์ ันนี้คนื
 # - ถ้ำไม่ผ่ำนเกณฑ์ข้อ 1 ทั้งคู่ คืนลิสต์ว่ำง
 # - ถ้ำผ่ำนเกณฑ์ข้อ 1 คนเดียว คืนลิสต์ที่เก็บเลขประจ ำตัวของคนที่ผ่ำนเกณฑ์ข้อ 1
 # - ถ้ำผ่ำนเกณฑ์ข้อ 1 ทั้งคู่ คืนลิสต์ที่เก็บเลขประจ ำตัวของนิสติ ที่มีข้อ 2 ที่ดีกว่ำ
 # - ถ้ำผ่ำนเกณฑ์ข้อ 1 ทั้งคู่ และมีข้อ 2 เท่ำกัน คืนลิสต์ที่เก็บเลขประจ ำตัวของนิสติ คนแรก ตำมด้วยของคนที่สอง
    out = []
    id1 = stu1[0]
    id2 = stu2[0]
    gpax1 = float(stu1[1])
    gpax2 = float(stu2[1])
    com1 = stu1[2]
    com2 = stu2[2]
    cal11 = stu1[3]
    cal12 = stu2[3]
    cal21 = stu1[4]
    cal22 = stu2[4]


    pass1 = False
    pass2 = False
    if chartoint(com1) == 5 and chartoint(cal11) >= 3 and chartoint(cal21) >= 3:
        pass1 = True
    if chartoint(com2) == 5 and chartoint(cal12) >= 3 and chartoint(cal22) >= 3:
        pass2 = True
    
    if pass1 and pass2 :
        if (gpax1 == gpax2) : 
            if (chartoint(cal11) == chartoint(cal12)) :
                if (chartoint(cal21) == chartoint(cal22)) :
                    out.append(id1)
                    out.append(id2)
                else :
                    findwhomax(chartoint(cal21),chartoint(cal22),id1,id2,out)
            else :
                findwhomax(chartoint(cal11),chartoint(cal12),id1,id2,out)
        else :
            findwhomax(gpax1,gpax2,id1,id2,out)
    else :
        if pass1 :
            out.append(id1)
        if pass2 : 
            out.append(id2)
    return out
exec(input()) # DON'T remove this line