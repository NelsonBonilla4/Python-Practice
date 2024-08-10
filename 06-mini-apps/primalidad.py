# Funcion para hallar si es primo
def es_primo(n):
    contador = 0

    for i in range(1, n+1):
        if i == 1 or i == n:
            continue

        elif n % i == 0:
            contador += 1

    if contador == 0:
        return True
    else:
        return False

# Funcion principal para imprimir la información del numero
def main():
    n = int(input("Por favor ingrese el numero a comprobar: "))
    is_prime = es_primo(n)
    if is_prime:
        print(f"El numero {n} es primo")
    else:
        print(f"El numero {n} no es primo")

if __name__ == '__main__':
    main()

