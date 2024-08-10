def extraccion_numeros(n):
    f = []
    while n > 0:
        n -= 1
        f.append(n)
    print(f)
    t = sum(f)
    print(t)

extraccion_numeros(5)