n = int(input())
city_to_id = {}
id_to_city = {}
ids = []
for t in range(n) :
    inp = input().split()
    id = inp[0][:-1]
    ids.append(id)
    for i in range(1,len(inp)) :
        city = inp[i][:-1] if len(inp[i]) > 1 else inp[i]
        if city not in city_to_id :
            city_to_id[city] = [id]
        else : city_to_id[city].append(id)
        
        if id not in id_to_city :
            id_to_city[id] = [city]
        else : id_to_city[id].append(city)

in_id = input()
out = []
for id in ids:
    for ci in id_to_city[in_id]:
        if ci in id_to_city[id] and id != in_id and id not in out:
            out.append(id)
if len(out) == 0 : print("Not Found")
else :
    for id in out :
        print(id)


