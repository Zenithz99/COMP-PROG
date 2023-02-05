def factor(N):
    tmp = N
    out = []
    for i in range(2,N+1) :
        if (N%i == 0) :
            cnt = 0
            while (N%i == 0) :
                cnt += 1
                N //= i
            out.append([i,cnt])
    N = tmp
    return out
exec(input().strip())