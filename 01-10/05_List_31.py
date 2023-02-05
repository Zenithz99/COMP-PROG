lists = [x for x in input().split(" ")]
command = input().strip()
for i in range(len(command)) :
  tmp_list = []
  if command[i] == "C" :
    mid = len(lists) // 2
    tmp_list = lists[mid:] + lists[:mid]
    lists = tmp_list
  elif command[i] == "S" :
    mid = len(lists) // 2
    for i in range(mid) :
      tmp_list.append(lists[i])
      tmp_list.append(lists[i+mid])
    lists = tmp_list
out = ""
for i in range(len(lists)) : out += lists[i] + " "
print(out[:-1])