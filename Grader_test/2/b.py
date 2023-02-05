def match(word, pattern, include_chars, exclude_chars):
    if (len(word) != len(pattern)) : return False
    dic = {}
    for i in range(len(word)) :
        if pattern[i] == "?" :
            if word[i] in exclude_chars : return False
            if (word[i] not in dic) :
                dic[word[i]] = 1
            else :
                dic[word[i]] += 1
        elif word[i] != pattern[i] : return False
    for c in include_chars :
        if (c not in dic) or (dic[c] == 0):
            return False
        dic[c] -= 1
    return True


exec(input()) # DON'T remove this line