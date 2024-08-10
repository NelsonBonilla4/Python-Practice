import random

def juego(vidas):
    numero_rand = random.randint(1, 100)
    numero_elegido = None

    while numero_rand != numero_elegido:
        numero_elegido = int(input('Ingrese un numero entre 1 y 100: '))

        if numero_elegido < numero_rand:
            print('Elige un numero mas grande.')
            vidas -= 1

        elif numero_elegido > numero_rand:
            print('Elige un numero mas pequeño')
            vidas -= 1

        if vidas == 0:
            print('GAME OVER')
            break

        print(f'Te quedan {vidas} vidas restantes')
    
    print(f'Has ganado, felicidades. El numero era {numero_rand}')

def main():
    while True:
        n_dificultad = input('''
            -------ADIVINA EL NUMERO--------
            Elija la dificultad que desea:
                1. Fácil (10 vidas)
                2. Intermedio (7 vidas)
                3. Difícil (5 vidas)
                4. Salir
            Escriba el numero de la dificultad que desea para jugar: ''')
        
        if n_dificultad == '1':
            vidas = 10
            
        elif n_dificultad == '2':
            vidas = 7
            
        elif n_dificultad == '3':
            vidas = 5
            
        elif n_dificultad == '4':
            print('Cerrando el juego....')
            break
        else:
            print('Ingrese una opción válida')

        juego(vidas)


if __name__ == "__main__":
    main()
