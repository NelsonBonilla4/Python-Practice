'''
input: tiempo en segundos
output: tiempo en horas, minutos y segundos (00:00:00)
'''

# Función para convertir los segundos en horas, minutos y segundos
def segundos_a_hms(t):
    m = 0
    while t > 60:
        t = t - 60
        m += 1
    
    h = 0 
    while m > 60:
        m = m - 60
        h += 1
        
    d = 0
    while h > 24:
        h = h - 24
        d += 1
    s = t
    print(f'Los segundos ingresados son equivalentes a {d} días, {h} horas, {m} minutos y {s} segundos')

segundos_a_hms(int(input('Ingrese los segundos: ')))