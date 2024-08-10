'''
Enunciado: un restaurante ofrece un descuento del 10% para consumo de hasta s/. 100.00 y 
un descuento del 20 % para consumos mayores, para ambos casos se aplica un impuesto del 19%. 
Determinar el monto del descuento, el impuesto y el importe a pagar.

Análisis: para la solución de este problema, se requiere que el usuario ingrese el consumo y 
el sistema verifica y calcula el monto del descuento, el impuesto y el importe a pagar.

monto del descuento

impuesto

importe a pagar
'''

consumo = float(input("Ingrese el consumo del cliente: ")) # 200.000

def desc(consumo):
    if consumo <= 100.00:
        mo_desc = consumo * 0.10 
    elif consumo > 100.00:
        mo_desc = consumo * 0.20 # 40.000

    desc_total = consumo - mo_desc

    impuesto = desc_total * 0.19 #38.000

    imp_pagar = desc_total + impuesto

    print('*' * 10)
    print('-' * 10)
    print('FACTURA')
    print(f'Consumo total: ${consumo}\nDescuento: ${mo_desc}\nImpuesto: ${impuesto}\nImporte a pagar: ${imp_pagar}')
    print('-' * 10)
    print('*' * 10)

desc(consumo)