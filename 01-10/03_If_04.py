inp = input()
if len(inp) != 10 :
    print("Not a mobile number")
else :
    front = inp[0] + inp[1]
    if front == "06" or front == "08" or front == "09" :
        print("Mobile number")
    else :
        print("Not a mobile number")