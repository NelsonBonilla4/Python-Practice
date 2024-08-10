'''
Pequeñas funciones anónimas pueden ser creadas con la palabra reservada lambda. 
Esta función retorna la suma de sus dos argumentos: lambda a, b: a+b 
Las funciones Lambda pueden ser usadas en cualquier lugar donde sea requerido un objeto de tipo 
función. Están sintácticamente restringidas a una sola expresión. 
Semánticamente, son solo azúcar sintáctica para definiciones normales de funciones. 
Al igual que las funciones anidadas, las funciones lambda pueden hacer referencia a variables 
desde el ámbito que la contiene:
'''

def make_incrementor(n):
    return lambda x: x + n

f = make_incrementor(42)

print(f[0])
print(f[1])