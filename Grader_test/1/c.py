inp = input().strip()
curr = 0
next = ""
found = 0
if inp[0] != '-' : inp = '+' + inp
for i in range(len(inp)) :
    if inp[i] in '+-' and found == 1 :
        op = next[0]
        num = int(next[1:])
        if op == '+' : curr += num
        elif op == '-' : curr -= num
        next = ""
    next += inp[i]
    found = 1
if next != "" :
    op = next[0]
    num = int(next[1:])
    if op == '+' : curr += num
    elif op == '-' : curr -= num
print(curr)