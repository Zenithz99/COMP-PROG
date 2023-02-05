def convert(i) :
    if 'a' <= i <= 'z' :
        id = (ord(i) - ord('a') + 13) % 26
        return chr(id + ord('a'))
    elif 'A' <= i <= 'Z' :
        id = (ord(i) - ord('A') + 13) % 26
        return chr(id + ord('A'))
    else : return i
inp = input()
while inp != "end" :
    out = ""
    for i in range(len(inp)) :
        out += convert(inp[i])
    print(out)
    inp = input()