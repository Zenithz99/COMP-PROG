result = input().strip()
target = int(input())
i = 0 # เตรียมตัวแปรที่คอยเก็บ index เริ่มต้นของเฟรม
total_score = 0 # เตรียมตัวแปรเก็บคะแนนรวม
n = len(result)
flag = False
for f in range(1,11) : # บังคับให้ท ำตั้งแต่เฟรม 1,2,...,10
 # ต้องให้ i เกบ็ ตำ แหน่งเริ่มต้นของเฟรม f ใน result
 s1 = s2 = s3 = ''
 if i < n : s1 = result[i]
 if i+1 < n : s2 = result[i+1]
 if i+2 < n : s3 = result[i+2]
 if s1 == 'X' and s2 == 'X' and s3 == 'X' :
   score_in_frame_f = 10 + 10 + 10
   i = i+1
 elif s1 == 'X' and s2 == 'X' and (s3 != 'X' and s3 != '/'):
   score_in_frame_f = 10 + 10 + int(s3)
   i = i+1
 elif s1 == 'X' and (s2 != 'X' and s2 != '/') and s3 == '/':
   score_in_frame_f = 10 + 10
   i = i+1
 elif s1 == 'X' and (s2 != 'X' and s2 != '/') and (s3 != 'X' and s3 != '/') :
   score_in_frame_f = 10 + int(s2) + int(s3)
   i = i+1
 elif (s1 != 'X' and s1 != '/') and s2 == '/' and s3 == 'X' :
   score_in_frame_f = 10 + 10
   i = i+2
 elif (s1 != 'X' and s1 != '/') and s2 =='/' and (s3 != 'X' and s3 != '/') :
   score_in_frame_f = 10 + int(s3)
   i = i+2
 else :
   score_in_frame_f = int(s1) + int(s2)
   i = i+2

 total_score += score_in_frame_f
 if f == target :
   print(score_in_frame_f)
   flag = True
   break
if flag == False :
    print(total_score)