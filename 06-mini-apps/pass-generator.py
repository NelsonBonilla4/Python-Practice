import random

# Función para generar una contraseña aleatoria
def generator(longo=0):
    if longo > 0:
        vocales_min = ['a','e','i','o','u']
        vocales_may = ['A','E','I','O','U']
        letras_min = ['b','c','d','h','j','k','l','m','n','p','q','r','s','t','w','y','v','x','z']
        letras_may = ['B','C','D','H','J','K','l','M','N','P','Q','R','S','T','W','Y','V','X','Z']
        carac_espec = ['!','#','$','%','&','¡','@','€']
        numeros = ['0','1','2','3','4','5','6','7','8','9']
        
        pws_base = vocales_may + vocales_min + letras_min + letras_may + carac_espec + numeros
        pws = []

        contador = 0
        while contador < longo:
            ps = random.choice(pws_base)
            pws.append(ps)
            contador += 1
        
        # Sirve para unir los elementos de una lista como si fueran un string
        pws = "".join(pws)
        return pws

    else:
        print("Por favor ingrese un valor válido....")

def main():
    pws = generator(int(input('Defina la extensión de su contraseña: ')))
    print(f'Su contraseña generada es: {pws}')

if __name__ == '__main__':
    main()
