inu = input()
inv = input()

u = inu[1:-1].split(", ")
v = inv[1:-1].split(", ")

u1 = float(u[0])
u2 = float(u[1])
u3 = float(u[2])
v1 = float(v[0])
v2 = float(v[1])
v3 = float(v[2])

lu = [u1,u2,u3]
lv = [v1,v2,v3]
lt = [u1+v1,u2+v2,u3+v3]

print(str(lu) + " + " + str(lv) + " = " + str(lt))