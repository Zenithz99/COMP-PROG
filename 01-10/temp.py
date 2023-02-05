n = int(input())
coodinate_list = []
for i in range(n) :
    x = input()
    x_list = x.split()
    coodinate_list.append(x_list)
length_index_list = []
for a,b in enumerate(coodinate_list) :
    l = (float(b[0])**2+float(b[1])**2)**(1/2)
    length_index_list.append([l,a])

for i in range(len(length_index_list)) :
    a,b = length_index_list[i]
    coodinate_list[i].insert(0,length_index_list[i])

coodinate_list.sort()
for i in coodinate_list :
    out = ""
    for j in i :
        out += str(j) + " "
    print(out)
ans = coodinate_list[2]
ans2 = "(" + str(ans[1]) + "," + str(ans[2]) + ")"
ans3 = "#" + str(int(ans[0][1])+1) + ": "
print(ans3+ans2)