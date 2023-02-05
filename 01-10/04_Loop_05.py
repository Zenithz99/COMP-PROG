check = input()
inp = input()

inp = inp.replace("\""," ")
inp = inp.replace("("," ")
inp = inp.replace(")"," ")
inp = inp.replace(","," ")
inp = inp.replace("."," ")
inp = inp.replace("'"," ")

spl = inp.split()

cnt = 0
for word in spl :
  if check == word : cnt += 1
print(cnt)
