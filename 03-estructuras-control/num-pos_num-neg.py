n = int(input('Ingrese el numero inicial negativo '))
nf = int(input('Ingrese el numero final positivo '))

c = list(range(n, nf+1))

cp = 0
cn = 0
cpl = []
cnl = []

for num in c:
    if num > 0:
        cp += 1
        cpl.append(num)
    else:
        cn += 1
        cnl.append(num)

print(f'Del rango {n} hasta {nf}, hay:\n{cp} numeros positivos, los cuales son: {cpl}\n{cn} numeros negativos, los cuales son: {cnl}')