def gcd(a,b):
    while b != 0:
        a,b = b, a%b
    return a
def is_coprime(a, b, c):
    k1 = gcd(a,b)
    k2 = gcd(b,c)
    k3 = gcd(c,a)
    k = gcd(k1,k2)
    k = gcd(k,k3)
    return k <= 1
def is_pyta(a,b,c) :
    return c**2 == a**2 + b**2
def primitive_Pythagorean_triples(max_len):
    triple = []
    for c in range(1,max_len + 1) :
        for b in range(1,c+1) :
            for a in range(1,b+1) :
                if (is_coprime(a,b,c)) and (is_pyta(a,b,c)) : triple.append([a,b,c])
    triple.sort(key = lambda x : x[0])
    triple.sort(key = lambda x : x[2])
    return triple
exec(input().strip())