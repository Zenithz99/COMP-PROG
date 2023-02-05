import math
PI = math.pi
E = math.e
n = float(input())

a = (2*PI)**(1/2) * n**(n + 1/2) * E**(-n + (1/(12*n+1)))
b = (2*PI)**(1/2) * n**(n + 1/2) * E**(-n + (1/(12*n)))

print(a)
print(b)