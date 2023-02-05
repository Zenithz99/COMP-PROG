def rule2(p) :
    lower = upper = number = symbol = False
    for i in range(len(p)) :
        if '0' <= p[i] <= '9' :
            number = True
        elif 'A' <= p[i] <= 'Z' :
            upper = True
        elif 'a' <= p[i] <= 'z' :
            lower = True
        else :
            symbol = True
    return lower,upper,number,symbol
def rule3_6(p) :
    rule3 = rule4 = rule5 = rule6 = False
    if len(p) >= 4 :
        for i in range(len(p)-3) :
            if p[i] == p[i+1] == p[i+2] == p[i+3] :
                rule3 = True
            cal = p[i:i+4].lower()
            if cal in "abcdefghijklmnopqrstuvwxyzabc" or cal in "abcdefghijklmnopqrstuvwxyzabc" [::-1]:
                rule5 = True
            if cal in "0123456789012" or cal in "0123456789012" [::-1]:
                rule4 = True
            if cal in "!@#$%^&*()_+!@#" or cal in "qwertyuiopqwe" or cal in "asdfghjklasd" or cal in "zxcvbnmzxc" :
                rule6 = True
            if cal in "!@#$%^&*()_+!@#"[::-1] or cal in "qwertyuiopqwe"[::-1] or cal in "asdfghjklasd"[::-1] or cal in "zxcvbnmzxc"[::-1] :
                rule6 = True
    return rule3,rule4,rule5,rule6
            
password = input().strip()

lower,upper,number,symbol = rule2(password)
rule3,rule4,rule5,rule6 = rule3_6(password)
error = []
if len(password) < 8 :
    error.append("Less than 8 characters")
if not lower :
    error.append("No lowercase letters")
if not upper :
    error.append("No uppercase letters")
if not number :
    error.append("No numbers")
if not symbol :
    error.append("No symbols")
if rule3 :
    error.append("Character repetition")
if rule4 :
    error.append("Number sequence")
if rule5 :
    error.append("Letter sequence")
if rule6 :
    error.append("Keyboard pattern")

if len(error) == 0 :
    print("OK")
else :
    for e in error :
        print(e)

