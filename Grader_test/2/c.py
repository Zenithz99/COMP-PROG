def cal(word , dic) :
    result = ""
    i = 0
    while i < len(word) :
        flag = True
        for check in dic :
            if word[i].lower() == check[0] :
                long = len(check)
                color = word[i : i + long]
                if color.lower() == check :
                    flag = False
                    result += "<{}>{}</>".format(check , color)
                    i += long
                    break
        if (flag) :
            result += word[i]
            i += 1
    return result
locate_color = input()
locate_input = input()

file = open(locate_color , 'r')
dic_color = {}
for line in file.readlines() :
    line = line.strip().split()
    for color in line :
        dic_color[color.lower()] = 1
file.close()

file = open(locate_input , 'r')
for line in file.readlines() :
    out = ""
    line = line.strip()
    cur_word = ""
    for c in line :
        if c.lower() not in "abcdefghijklmnopqrstuvwxyz" :
            out += cal(cur_word,dic_color) + c
            cur_word = ""
        else :
            cur_word += c
    if cur_word != "" :
        out += cal(cur_word,dic_color)
    print(out)