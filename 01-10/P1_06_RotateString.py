command = input().strip()
n = int(input())
lists = []
check_size = -1
check = True
for i in range(n) :
    tmp = input().strip()
    lists.append(tmp)
    if check_size == -1 : check_size = len(tmp)
    elif check_size != -1 and len(tmp) != check_size : check = False

new = []
if check :
  m = check_size
  if command == "90" :
    
    j = 0
    while j < m:
      i = n-1
      out = ""
      while i>=0 :
        out += lists[i][j]
        i -= 1
      print(out)
      j += 1
      
  elif command == "flip" :
  
    for i in range(n) :
      j = m-1
      out = ""
      while j >= 0 :
        out += lists[i][j]
        j -= 1
      print(out)
      
  elif command == "180" :
    
    i = n-1
    while i >= 0 :
      j = m-1
      out = ""
      while j >= 0 :
        out += lists[i][j]
        j -= 1
      print(out)
      i -= 1
else :
  print("Invalid size")