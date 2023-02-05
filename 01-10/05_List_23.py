n = int(input())
lists = []
for i in range(n) :
  x , y = [float(x) for x in input().split(" ")]
  diff_0 = (x**2 + y**2)**(1/2)
  lists.append([x,y,diff_0,i])
def sort_diff(x) :
  return x[2]
lists.sort(key = sort_diff)
print("#{}: ({}, {})".format(lists[2][3]+1,lists[2][0],lists[2][1]))