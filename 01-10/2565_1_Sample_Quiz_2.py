def change(word,check) :
    if (len(word) == len(check)) :
        for i in range(len(check)) :
            if (check[i] == '?') : continue
            if (check[i].lower() != word[i].lower()) : return False
        return True
    else :
        return False
locate = input()
file = open(locate , 'r')
check = input()
inp = input()

w = file.readline().strip()
while (w != "") :
    word = ""
    printout = ""
    for i in range(len(w)) :
        if w[i] == '/' :
            if (change(word,check)) :
                printout += inp + '/'
                #print("ggez")
            else : printout += word + '/'
            word = ""
        else :
            word += w[i]
        #print(word)
    if (word != "" and w[-1] == '/' and change(word,check)) :
        printout += inp
    else :
        printout += word
    print(printout)
    w = file.readline().strip()

file.close()