from figuras import Rectangulo, Circulo, probar_figura

def main():
    while True:
        print(' ' * 8)
        print(' ' * 8, 'AREA Y PERIMETRO DE FIGURAS GEOMETRICAS')
        print(' ' * 8, '1. - Rectangulo')
        print(' ' * 8, '2. - Circulo')
        print(' ' * 8, '3. - Salir')
        n = int(input('Ingrese una opcion: '))

        if n == 1:
            probar_figura(Rectangulo)

        elif n == 2:
            probar_figura(Circulo)

        elif n == 3:
            print('Cerrando el programa....')
            break

        else:
            print('Por favor escriba una de las opciones....')

if __name__ == '__main__':
    main()