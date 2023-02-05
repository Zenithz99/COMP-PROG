lists = [int(i) for i in input().split(" ")]
lists.sort()
uniq = []
cnt = 0
for i in lists :
  if i not in uniq :
    cnt += 1
    uniq.append(i)
print(cnt)
print(uniq[:10])