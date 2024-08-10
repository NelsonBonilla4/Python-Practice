class Persona:
    '''
    name = None
    age = None
    '''

    # Esto crea la instancia de lo mismo de arriba y permite un codigo mas limpio
    # Ademas esto vienen siendo las propiedades de la clase
    # SE LE LLAMA CONSTRUCTOR por lo arriba  mencionado
    def __init__(self, name, age):
        self.name = name
        self.age = age 

    # Esta funcion entra a ser las operaciones internas de la clase
    def show_dat(self):
        print(f"Nombre: {self.name}\nEdad: {self.age}")

    # Este metodo sirve para cuando se imprima solo el objeto, vaya con cierta informacion
    # Y podamos conocer lo que ocurre internamente
    def __str__(self):
        return f'Nombre: {self.name}\nEdad: {self.age}'