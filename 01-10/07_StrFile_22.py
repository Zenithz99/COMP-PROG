dic1 = {}
dic2 = {}
inp1 = input()
inp2 = input()
for i in range(len(inp1)) :
    if inp1[i] == ' ' : continue
    if inp1[i].lower() not in dic1 : dic1[inp1[i].lower()] = 1
    else : dic1[inp1[i].lower()] += 1 
for i in range(len(inp2)) :
    if inp2[i] == ' ' : continue
    if inp2[i].lower() not in dic2 : dic2[inp2[i].lower()] = 1
    else : dic2[inp2[i].lower()] += 1 
if (dic1 == dic2): print("YES")
else : print("NO")