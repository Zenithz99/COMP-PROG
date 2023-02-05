inp = input().strip().upper()
op = input()
wronginp = False
dic = {'A' : 0,'T' : 0,'G' : 0,'C' : 0}
for i in range(len(inp)) :
  if inp[i] not in "ATCG" :
    wronginp = True
    break
  dic[inp[i]] += 1
if wronginp :
  print("Invalid DNA")
else :
  if op == 'R' :
    newinp = ""
    for i in range(len(inp)) :
      if inp[i] == 'A' : newinp += 'T'
      elif inp[i] == 'T' : newinp += 'A'
      elif inp[i] == 'C' : newinp += 'G'
      elif inp[i] == 'G' : newinp += 'C'
    newinp = newinp[::-1]
    print(newinp)
  if op == 'F' :
    out = ""
    order = "ATGC"
    for i in range(4) :
      out += order[i] + "=" + str(dic[order[i]]) + ", "
    print(out[:-2].strip())
  if op == 'D' :
    finds = input()
    cnt = 0
    for i in range(len(inp)) :
      if inp[i:i+2] == finds : cnt += 1
    print(cnt)