inp = input()
passkana = ["01","02","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","51","53","55","58"]
if len(inp) > 2 :
    print("Error")
else :
    if inp in passkana :
        print("OK")
    else :
        print("Error")