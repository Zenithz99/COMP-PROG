def read_matrix():
    m = []
    nrows = int(input())
    for k in range(nrows):
        x = input().split()
        r = []
        for e in x:
            r.append( float(e) )
        m.append(r)
    return m
def mult_c(c, A):
    for i in range(len(A)) :
        for j in range(len(A[i])) :
            A[i][j] *= c
    return A
def mult(A, B):
    ans = []
    n = len(A)
    m = len(A[0])
    p = len(B[0])
    for i in range(n) :
        ap = []
        for j in range(p) :
            add = 0
            for k in range(m) :
                add += A[i][k] * B[k][j]
            ap.append(add)
        ans.append(ap)
    return ans
exec(input().strip())