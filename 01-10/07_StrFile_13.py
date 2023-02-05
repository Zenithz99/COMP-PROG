def valid(i) :
  return ("0" <= i <= "9") or ("a" <= i <= "z") or ("A" <= i <= "Z")  or i == " "
inp = input()
cal = ""
for i in range(len(inp)) :
  if valid(inp[i]) :
    cal += inp[i]
  else :
    cal += " "
listcal = cal.split(" ")
out = ""
first = True
for i in range(len(listcal)) :
  if len(listcal[i]) == 0 : continue
  if first :
    first = False
    out += listcal[i].lower()
  else :
    out += listcal[i][0].upper() + listcal[i][1:].lower()
print(out)