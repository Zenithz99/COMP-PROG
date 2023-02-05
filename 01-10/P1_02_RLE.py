command = input()
if command == "str2RLE" :
  inp = input()
  out = ""
  cnt = 1
  curr_char = inp[0]
  for i in range(1,len(inp)) :
    if inp[i] == inp[i-1] :
      cnt += 1
    else :
      out += curr_char + " " + str(cnt) + " "
      cnt = 1
      curr_char = inp[i]
  out += curr_char + " " + str(cnt)
  print(out)
elif command == "RLE2str" :
  inp = input().split()
  out = ""
  for i in range(0,len(inp),2) :
    char = inp[i]
    cnt = int(inp[i+1])
    out += char * cnt
  print(out)
else :
  print("Error")