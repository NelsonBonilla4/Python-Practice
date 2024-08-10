def palindromo(palabra):
    pal = palabra.replace(' ', '').lower()
    palabra_invertida = pal[::-1]

    if pal == palabra_invertida:
        return True
    else:
        return False

def main():
    palabra = input("Ingrese su palabra o frase para comprobarla: ")
    is_pal = palindromo(palabra)
    if is_pal:
        print(f'La palabra/frase {palabra} es palindromo')
    else:
        print(f'La palabra/frase {palabra} no es palindromo')

if __name__ == "__main__":
    main()
