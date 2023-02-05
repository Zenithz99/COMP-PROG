inp = input()
check_num = ['0','1','2','3','4','5','6','7','8','9']
is_in = [False for i in range(10)]
n = len(inp)
for i in range(n) :
  char = inp[i]
  if char in check_num :
    idx = int(char)
    is_in[idx] = True

out = ""
cnt_false = 0
for i in range(10) :
    if not is_in[i] : 
        out += "{},".format(i)
        cnt_false += 1
out = out[:-1]
print(out) if cnt_false != 0 else print("None")