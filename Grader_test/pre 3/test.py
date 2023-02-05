def calculateSTH(current_list) :
    print("".join(current_list))


def func1(l , i , current_list) :
    if (i == len(l)) :
        calculateSTH(current_list)
        return
    for each_item in l[i] :
        func1(l , i+1 , current_list + [each_item])
    return

def calculateSTH2(array,l) :
    out = ""
    for i in range(len(l)) :
        out += l[i][array[i]]
    print(out)

def func2(l) :
    n = len(l)
    array = [0]*n
    working = True
    while(working) :
        array[n-1] += 1
        for j in range(n)[::-1] :
            if (array[j] == len(l[j])) :
                if (j-1 < 0) :
                    working = False
                    break
                array[j] = 0
                array[j-1] += 1
        if (not working) : break
        calculateSTH2(array,l)

l = [
    ['a' , 'b' , 'c'],
    ['d' , 'e'],
    ['f'],
    ['g' ,'h' ,'i'],
    ['j','k'],
    ['l','m','n','o']
]
#func1(l , 0 , [])
func2(l)