"""
API REST para la aplicación To-Do List
Este módulo implementa los endpoints necesarios para gestionar las tareas:
- GET /todos: Obtiene todas las tareas
- POST /todos: Crea una nueva tarea
- PUT /todos/<id>: Actualiza una tarea existente
- DELETE /todos/<id>: Elimina una tarea
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
from db import obtener_conexion

# Inicialización de la aplicación Flask
app = Flask(__name__)
# Habilitamos CORS para permitir peticiones desde el frontend
CORS(app)

@app.route("/")
def home():
    """Ruta principal que muestra un mensaje de bienvenida"""
    return "Bienvenido a la API To-Do. Usá /todos para interactuar."

@app.route("/todos", methods=["GET"])
def get_todos():
    """
    Obtiene todas las tareas de la base de datos
    Returns:
        list: Lista de tareas con su id, título y estado de completado
    """
    conn = obtener_conexion()
    cur = conn.cursor()
    cur.execute("SELECT id, title, completed FROM todos")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify([{"id": r[0], "title": r[1], "completed": r[2]} for r in rows])

@app.route("/todos", methods=["POST"])
def add_todo():
    """
    Agrega una nueva tarea a la base de datos
    Request body:
        title (str): Título de la tarea
    Returns:
        dict: Tarea creada con su id, título y estado inicial (no completada)
    """
    data = request.get_json()
    conn = obtener_conexion()
    cur = conn.cursor()
    cur.execute("INSERT INTO todos (title) VALUES (%s) RETURNING id", (data["title"],))
    todo_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({"id": todo_id, "title": data["title"], "completed": False})

@app.route("/todos/<int:id>", methods=["PUT"])
def update_todo(id):
    """
    Actualiza el estado de una tarea existente
    Args:
        id (int): ID de la tarea a actualizar
    Request body:
        completed (bool): Nuevo estado de completado
    Returns:
        str: Respuesta vacía con código 204
    """
    data = request.get_json()
    conn = obtener_conexion()
    cur = conn.cursor()
    cur.execute("UPDATE todos SET completed = %s WHERE id = %s", (data["completed"], id))
    conn.commit()
    cur.close()
    conn.close()
    return "", 204

@app.route("/todos/<int:id>", methods=["DELETE"])
def delete_todo(id):
    """
    Elimina una tarea de la base de datos
    Args:
        id (int): ID de la tarea a eliminar
    Returns:
        str: Respuesta vacía con código 204
    """
    conn = obtener_conexion()
    cur = conn.cursor()
    cur.execute("DELETE FROM todos WHERE id = %s", (id,))
    conn.commit()
    cur.close()
    conn.close()
    return "", 204

if __name__ == "__main__":
    # Iniciamos el servidor en modo debug para desarrollo
    app.run(debug=True)
