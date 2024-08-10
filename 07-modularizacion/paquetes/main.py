import my_paquete.arith as a

def main():
    suma = a.sumar(4,4,4,5,8,10)
    resta = a.restar(20, 4)
    potencia = a.potencia(4,4)

    print(f'suma: {suma}\nresta: {resta}\npotencia: {potencia}')

if __name__ == '__main__':
    main()