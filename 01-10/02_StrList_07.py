inp = input()
# 4,11,18,25 และ 32
str1 = inp[3] + inp[10] + inp[17] + inp[24] + inp[31]
#  8,13,18,23,28
str2 = inp[7] + inp[12] + inp[17] + inp[22] + inp[27]

num3 = int(str1) + int(str2) + 10000
num3 = str(num3)

num5 = int(num3[-2]) + int(num3[-3]) + int(num3[-4])
char5 = num5%10

char = ["A" , "B" , "C" , "D" , "E" , "F" , "G" , "H" , "I" , "J"]
print(num3[-4:-1] + char[char5])


