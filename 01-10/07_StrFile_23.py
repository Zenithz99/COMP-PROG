inp = input().split()
filename = inp[0]
year = inp[1][-2:]
f = open(filename,'r')
n = 0
maxx = -1
minn = 101
summ = 0

i = f.readline()
while (i != "") :
  v = i.split()
  if (v[0][:2] == year) :
    n += 1
    maxx = max(maxx,float(v[1]))
    minn = min(minn,float(v[1]))
    summ += float(v[1])
  i = f.readline()


if n == 0 :
  print("No data")
else :
  print("{} {} {}".format(minn,maxx,summ/n))
f.close()