inp = input()
if len(inp) >= 10 :
  front = float(inp) / 10**9
  if (front / 10 < 1) : 
    out = round(front,1)
    print("{}B".format(out))
  else :
    out = round(front,0)
    print("{}B".format(int(out)))
elif len(inp) >= 7 :
  front = float(inp) / 10**6 
  if (front / 10 < 1) : 
    out = round(front,1)
    print("{}M".format(out))
  else :
    out = round(front,0)
    print("{}M".format(int(out)))
elif len(inp) >= 4 :
  front = float(inp) / 10**3 
  if (front / 10 < 1) : 
    out = round(front,1)
    print("{}K".format(out))
  else :
    out = round(front,0)
    print("{}K".format(int(out)))
else :
  print(inp)