class A:
    def a0(self):
        print('Soy el metodo de la clase A')

class B:
    def b0(self):
        print('Soy el metodo de la clase B')

# Da prioridad al primero que se ponga
class C(A,B):
    def c0(self):
        print('Soy el metodo de la clase C')
    