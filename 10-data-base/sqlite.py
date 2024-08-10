# Importar
import sqlite3

# Conexion
conexion = sqlite3.connect('tests.db')

# Crear cursor
cursor = conexion.cursor()

# Crear tabla
cursor.execute("CREATE TABLE IF NOT EXISTS gamers("+
"id INTEGER PRIMARY KEY AUTOINCREMENT, "+
"nombre varchar(255), "+
"apellido varchar(255), "+
"descripcion text, "+
")")

# Guardar cambios
conexion.commit()

# Cerrar la conexion
conexion.close()