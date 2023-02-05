out = []
# 1
n = int(input())
tmp = True # True add back , False add front
for i in range(n) :
  num = int(input())
  if (tmp) :
    out.append(num)
    tmp = False
  else :
    out.insert(0,num)
    tmp = True

#2
input2 = input()
if len(input2) != 0 :
    inp2 = [int(x) for x in input2.split()]
    for i in range(len(inp2)) :
        num = inp2[i]
        if (tmp) :
            out.append(num)
            tmp = False
        else :
            out.insert(0,num)
            tmp = True

#3
num = int(input())
while num != -1 :
  if (tmp) :
    out.append(num)
    tmp = False
  else :
    out.insert(0,num)
    tmp = True
  num = int(input())
print(out)