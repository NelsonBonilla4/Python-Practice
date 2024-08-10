from persona import Persona as per

# Segun nuestro modulo de persona gracias al __init__ que agregamos en nuestra clase
# Se reducen las lineas de codigo en cuanto a los objetos que creamos con la clase
# Es una mejor manera de hacerlo y que simplifica lineas de codigo.
persona1 = per('Nelson', 17)

'''
persona1.nombre = 'Nelson'
persona1.age = 17

persona2 = per()
persona2.nombre = 'Neruson'
persona2.age = 18
'''

persona1.show_dat()

persona1.name = 'Neruson' # Se cambia el nombre a Neruson en el objeto
print(persona1) # Gracias al metodo __str__ ahora se va a mostrar el objeto como lo hayamos retornado en el metodo


#persona2.show_dat()