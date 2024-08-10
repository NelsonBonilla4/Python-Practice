'''
a = int(input("Ingrese un número: "))
b = int(input("Ingrese un segundo número: "))

c = a // b
r = a % b

print(f'El cociente es : {c}\nEl residuo es: {r}')
'''

vvp = float(input('Ingrese el valor de venta del producto: '))
imp = 0.18

igv = vvp * imp
pv = igv + vvp

print(f'El IGV del producto es de: {igv}\nEl precio de venta del producto es de: {pv}')