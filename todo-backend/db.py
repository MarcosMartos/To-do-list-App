"""
Módulo de configuración de la base de datos PostgreSQL
Este módulo proporciona la función necesaria para establecer
conexiones con la base de datos PostgreSQL.
"""

import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

def obtener_conexion():
    """
    Crea y retorna una nueva conexión a la base de datos PostgreSQL
    
    Returns:
        psycopg2.connection: Objeto de conexión a la base de datos
        
    Configuración:
        - host: Servidor de la base de datos (localhost)
        - database: Nombre de la base de datos (todo_app)
        - user: Usuario de PostgreSQL (postgres)
        - password: Contraseña del usuario
    """
    return psycopg2.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )

