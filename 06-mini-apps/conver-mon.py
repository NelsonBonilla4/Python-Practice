def conversor(valor_dolar, pais):
    mon_loc = float(input(f'Ingrese la cantidad de {pais} '))
    if pais == 'peso colombiano':
        mon_conv = mon_loc / valor_dolar
        return mon_conv
    elif pais == 'peso mexicano':
        mon_conv = mon_loc / valor_dolar
        return mon_conv
    elif pais == 'bolivares':
        mon_conv = mon_loc / valor_dolar
        return mon_conv

def monedas_paises():
    zzz = input('Elija la opción de su moneda para la conversión:\n1.Peso Colombiano\n2.Peso Mexicano\n3.Bolivares\nElija una de las tres opciones. ')
    if zzz == '1':
        mon = 'peso colombiano'
        return mon
    elif zzz == '2':
        mon = 'peso mexicano'
        return mon
    elif zzz == '3':
        mon = 'bolivares'
        return mon
    
def main():
    pais = monedas_paises()
    valor_dolar = float(input("Ingrese el valor actual del dolar en el pais de la moneda en cuestion: "))

    valor_mon = conversor(valor_dolar,pais)

    print(f'El {pais} está actualmente en ${valor_dolar} dolares, por lo tanto su conversión es de ${round(valor_mon,2)} dolares.')

if __name__ == '__main__':
    main()