inp = input().strip()
if len(inp) >= 1 and inp[-1] == "x" or inp[-1] == "s" :
  inp += "es"
if len(inp) >= 2 and inp[-2:] == "ch":
  inp += "es"
elif len(inp) >= 2 and inp[-1] == "y" and inp[-2] not in ["a","e","i","o",'u'] :
  inp = inp[:-1]
  inp += "ies"
else :
  inp += "s"
print(inp)