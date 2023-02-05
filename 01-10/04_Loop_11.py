inp = input()
cnt = 1
curr_char = inp[0]
out = ""
for i in range(1,len(inp)) :
  if inp[i] == inp[i-1] :
    cnt += 1
    curr_char = inp[i]
  else :
    out += "{} {} ".format(curr_char,cnt)
    cnt = 1
    curr_char = inp[i]
if not cnt == 0 :
  out += "{} {}".format(curr_char,cnt)
print(out)