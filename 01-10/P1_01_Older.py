inp1 = input().split(" ")
inp2 = input().split(" ")
name1 = inp1[0]
name2 = inp2[0]
m1 = inp1[1]
m2 = inp2[1]
d1 = int(inp1[2][0:-1])
d2 = int(inp2[2][0:-1])
y1 = int(inp1[3])
y2 = int(inp2[3])

m_list = ["January","February","March","April","May","June","July","August","September","October","November","December"]

ri = 0
rj = 0
for i in range(0,12) :
    if m_list[i] == m1 : ri = i
    if m_list[i] == m2 : rj = i

if y2 > y1 :
  print(name1)
elif y2 < y1 :
  print(name2)
else :
  if rj > ri :
    print(name1)
  elif ri > rj :
    print(name2)
  else :
    if d2 > d1 :
      print(name1)
    elif d1 > d2 :
      print(name2)
    else :
      print(name1,name2)