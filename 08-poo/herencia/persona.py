class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
    
    def  detalle_persona(self):
        print(f'Nombre: {self.nombre}\nEdad: {self.edad}')

    def __str__(self):
        return f'Nombre: {self.nombre}\nEdad: {self.edad}'

# Tomando como parametro en una clase a otra clase, 
# es que se heredan los atributos y comportamientos
class Cliente(Persona):
    pass

# La funcion SUPER toma los valores que se van a heredar, 
# a partir de eso agregamos lo que nos haga falta en la clase.
# Tambien hay otra forma que es la que no esta comentada y va sin el SUPER
class Empleado(Persona):
    def __init__(self,nombre,edad,sueldo):
        #super().__init__(nombre,edad)
        Persona.__init__(self, nombre, edad)
        self.sueldo = sueldo

    def detalle_empleado(self):
        #super().detalle_persona()
        Persona.detalle_persona(self)
        print(f'Sueldo: {self.sueldo}')

    def __str__(self):
        #return super().__str__() + f'\nSueldo: {self.sueldo}'
        return Persona.__str__(self) + f'\nSueldo: {self.sueldo}'