"""
Script de inicialización de la base de datos
Este script crea la estructura inicial de la base de datos,
específicamente la tabla 'todos' que almacenará las tareas.

Estructura de la tabla 'todos':
- id: Identificador único autoincremental (SERIAL PRIMARY KEY)
- title: Texto de la tarea (TEXT NOT NULL)
- completed: Estado de completado (BOOLEAN DEFAULT FALSE)
"""

import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()


# Configuración de la conexión a la base de datos
conn = psycopg2.connect(
    host=os.getenv("DB_HOST"),
    database=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    port=os.getenv("DB_PORT")
)

# Creamos un cursor para ejecutar comandos SQL
cur = conn.cursor()

# Definición de la tabla 'todos'
# - SERIAL PRIMARY KEY: Genera IDs únicos automáticamente
# - TEXT NOT NULL: El título es obligatorio
# - BOOLEAN DEFAULT FALSE: Las tareas inician como no completadas
cur.execute("""
    CREATE TABLE IF NOT EXISTS todos (
        id SERIAL PRIMARY KEY,
        title TEXT NOT NULL,
        completed BOOLEAN DEFAULT FALSE
    );
""")

# Confirmamos los cambios en la base de datos
conn.commit()

# Cerramos el cursor y la conexión
cur.close()
conn.close()

print("Tabla 'todos' creada correctamente.")
