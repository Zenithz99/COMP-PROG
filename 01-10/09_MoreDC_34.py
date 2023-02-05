def pattern1(nrows, ncols):
 # nrows  0, ncols  0
    out = []
    n = 1
    for i in range(nrows) :
        tmp = []
        for j in range(ncols) :
            tmp.append(n)
            n += 1
        out.append(tmp)
    return out
def pattern2(nrows, ncols):
 # nrows  0, ncols  0
    out = [[0] * ncols] * nrows
    n = 1
    for j in range(ncols) :
        for i in range(nrows) :
            out[i][j] = n
            n += 1
    return out
def pattern3( N ): # N  0
    out = [[0] * N] * N
    return out
#def pattern4( N ): # N  0

#def pattern5( N ): # N  0

#def pattern6( N ): # N  0

exec(input().strip())