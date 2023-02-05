def create_dic() :
    dic_num = {}
    dic_symbol = {}
    nums = "A23456789TJQK"
    symbols = "CDHS"
    for i in range(len(nums)) :
        dic_num[nums[i]] = i+1
    for i in range(len(symbols)) :
        dic_symbol[symbols[i]] = i+1
    return dic_num,dic_symbol

dic_num,dic_symbol = create_dic()
inp = input()
out = ""
for idx in range(3,len(inp),2) :
    num1 = dic_num[inp[idx-3]]
    sym1 = dic_symbol[inp[idx-2]]
    num2 = dic_num[inp[idx-1]]
    sym2 = dic_symbol[inp[idx]]
    if num1 == num2 and sym1 == sym2 :
        out += '0'
    elif num1 == num2 :
        out += str(sym1 - sym2) if sym1 < sym2 else "+" + str(sym1-sym2)
    else :
        out += str(num1 - num2) if num1 < num2 else "+" + str(num1-num2)
print(out)