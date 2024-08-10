consumo = float(input("Ingrese el consumo del cliente: ")) # 250.0

def desc(consumo):
    if consumo > 0:
        if consumo <= 100.00:
            mo_desc = consumo * 0.10 
        elif consumo > 100.00 and consumo <= 200.00:
            mo_desc = consumo * 0.20
        elif consumo > 200.00:
            mo_desc = consumo * 0.30 #75.0
         
        desc_total = consumo - mo_desc # 175.0

        impuesto = desc_total * 0.19 # 33.25

        imp_pagar = desc_total + impuesto #208.25

        print('*' * 10)
        print('-' * 10)
        print('FACTURA')
        print(f'Consumo total: ${consumo}\nDescuento: ${mo_desc}\nImpuesto: ${impuesto}\nImporte a pagar: ${imp_pagar}')
        print('-' * 10)
        print('*' * 10)

    else:
        print(f'ERROR {consumo} no es un valor valido para la factura. Ingrese correctamente los datos nuevamente')

desc(consumo)