filenames = input().split()
f1 = open(filenames[0],'r')
f2 = open(filenames[1],'r')
linef1 = f1.readline().strip()
linef2 = f2.readline().strip()
while not (linef1 == "" and linef2 == "") :
    choose1 = choose2 = False
    if linef1 == "":
        choose2 = True
    elif linef2 == "" :
        choose1 = True
    else :
        data1 = linef1.split()
        data2 = linef2.split()
        if data1[0][-2:] < data2[0][-2:] or (data1[0][-2:] == data2[0][-2:] and data1[0][:-2] < data2[0][:-2]):
            choose1 = True
        elif data2[0][-2:] < data1[0][-2:] or (data1[0][-2:] == data2[0][-2:] and data2[0][:-2] < data1[0][:-2]):
            choose2 = True
    if choose1 :
        if linef1 != "" : print(linef1)
        linef1 = f1.readline().strip()
    elif choose2 :
        if linef2 != "" : print(linef2) 
        linef2 = f2.readline().strip()


f1.close()
f2.close()
