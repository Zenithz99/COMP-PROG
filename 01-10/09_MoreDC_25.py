def row_number(t, e): # return row number of t containing e (top row is row #0)
    for i in range(len(t)) :
        if e in t[i] : return i
    return -1
            
def flatten(t): # return a list of ints converted from list of lists of ints t
    out = []
    for i in range(len(t)) :
        for j in range(len(t[i])) :
            if (t[i][j] == 0) : continue
            else : out.append(t[i][j])
    return out
def inversions(x): # return the number of inversions of list x
    cnt = 0
    for i in range(len(x))[::-1] :
        for j in range(len(x))[0:i] :
            if (x[j] > x[i]) : cnt += 1
    return cnt
def solvable(t): # return True if tiling t (list of lists of ints) is solvable
 # otherwise return False  
    n_row = len(t)
    li = flatten(t)
    n_inv = inversions(li)
    n_0_row = row_number(t,0)
    out = False
    if (n_row%2 == 0 ) :
        if (n_inv%2 == 1 and n_0_row%2 == 0) : out = True
        elif (n_inv%2 == 0 and n_0_row%2 == 1) : out = True
    else :
        if (n_inv%2 == 0) : out = True
    return out


exec(input().strip()) # do not remove this line
