def RLE(t):
  out = []
  if len(t) == 0 : return out
  inp = t
  cnt = 1
  curr_char = inp[0]
  for i in range(1,len(inp)) :
    if inp[i] == inp[i-1] :
      cnt += 1
      curr_char = inp[i]
    else :
      out.append([curr_char,cnt])
      cnt = 1
      curr_char = inp[i]
  if not cnt == 0 :
    out.append([curr_char,cnt])
  return out
exec(input()) # DON'T remove this line