
def multiplicar(a , r):
    for x in range(len(r)):
        r[x] = a*r[x]
    return r


a = 0.90
r = [1, 1, 1, 1]

r = multiplicar(a, r)
print(r)