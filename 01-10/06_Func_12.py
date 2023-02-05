def is_prime(n):
 # ทดสอบว่า n เป็นจ านวนเฉพาะหรือไม่
  if n <= 1:
    return False
  for k in range(2,int(n**0.5)+1):
    if n%k == 0:
      return False
  return True
def next_prime(N):
 # คืนจ านวนเฉพาะตัวที่มีค่าน้อยสุดที่มากกว่า N
  check = N + 1
  while not is_prime(check) : check += 1
  return check
def next_twin_prime(N):
 # คืนจ านวนเฉพาะสองค่าที่เป็น twin prime ที่มีค่าน้อยสุดที่มากกว่า N
 # twin prime คือจ านวนเฉพาะที่มีค่าต่างกัน 2 เชน่ 11 กับ 13 หรือ 41 กับ 43
  check = N+1
  while not (is_prime(check) and is_prime(check+2)) : check += 1
  return check , check+2


exec(input().strip()) # ตอ้ งมคี าสั่งนี้ ตรงนี้ตอนสง่ ให้Grader ตรวจ