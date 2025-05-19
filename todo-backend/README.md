# To-Do List Backend

API REST para la aplicación To-Do List, desarrollada con Flask y PostgreSQL.

## Características

- 🚀 API RESTful completa
- 🔒 Conexión segura a base de datos PostgreSQL
- 🔄 Soporte CORS para integración con frontend
- 📝 CRUD completo para gestión de tareas
- 🔍 Documentación detallada de endpoints
- ⚡ Configuración mediante variables de entorno

## Estructura del Proyecto

```
todo-backend/
├── app.py              # Aplicación principal y endpoints
├── db.py              # Configuración de la base de datos
├── create-database.py # Script de inicialización de la BD
├── models.py          # Modelos de datos (reservado)
├── requirements.txt   # Dependencias del proyecto
├── .env              # Variables de entorno (no incluido en git)
└── venv/             # Entorno virtual de Python
```

## Tecnologías Utilizadas

- Flask: Framework web ligero para Python
- PostgreSQL: Sistema de gestión de base de datos
- psycopg2: Adaptador PostgreSQL para Python
- Flask-CORS: Soporte para CORS en Flask
- python-dotenv: Gestión de variables de entorno

## Requisitos Previos

- Python 3.8 o superior
- PostgreSQL 12 o superior
- pip (gestor de paquetes de Python)

## Configuración del Entorno

1. Crear un entorno virtual:

   ```bash
   python -m venv venv
   ```

2. Activar el entorno virtual:

   - Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - Linux/Mac:
     ```bash
     source venv/bin/activate
     ```

3. Instalar dependencias:

   ```bash
   pip install -r requirements.txt
   ```

4. Crear archivo `.env` con las variables de entorno:

   ```env
   DB_HOST=localhost
   DB_NAME=todo_app
   DB_USER=postgres
   DB_PASSWORD=tu_contraseña
   ```

5. Inicializar la base de datos:
   ```bash
   python create-database.py
   ```

## Endpoints de la API

### GET /

- Descripción: Ruta principal que muestra un mensaje de bienvenida
- Respuesta: Mensaje de bienvenida en texto plano

### GET /todos

- Descripción: Obtiene todas las tareas
- Respuesta: Lista de tareas en formato JSON
- Ejemplo:
  ```json
  [
    {
      "id": 1,
      "title": "Completar proyecto",
      "completed": false
    }
  ]
  ```

### POST /todos

- Descripción: Crea una nueva tarea
- Body:
  ```json
  {
    "title": "Nueva tarea"
  }
  ```
- Respuesta: Tarea creada en formato JSON
- Ejemplo:
  ```json
  {
    "id": 1,
    "title": "Nueva tarea",
    "completed": false
  }
  ```

### PUT /todos/:id

- Descripción: Actualiza una tarea existente
- Parámetros:
  - id: ID de la tarea
- Body:
  ```json
  {
    "completed": true
  }
  ```
- Respuesta: Código 204 (No Content)

### DELETE /todos/:id

- Descripción: Elimina una tarea
- Parámetros:
  - id: ID de la tarea
- Respuesta: Código 204 (No Content)

## Estructura de la Base de Datos

### Tabla: todos

- `id`: SERIAL PRIMARY KEY
  - Identificador único autoincremental
- `title`: TEXT NOT NULL
  - Título de la tarea
- `completed`: BOOLEAN DEFAULT FALSE
  - Estado de completado de la tarea

## Desarrollo

1. Iniciar el servidor de desarrollo:
   ```bash
   python app.py
   ```
2. El servidor estará disponible en `http://localhost:5000`

## Producción

Para entornos de producción, se recomienda:

1. Usar un servidor WSGI como Gunicorn
2. Configurar un proxy inverso (Nginx/Apache)
3. Implementar HTTPS
4. Configurar variables de entorno seguras
5. Implementar logging y monitoreo

## Seguridad

- Las credenciales de la base de datos se manejan mediante variables de entorno
- Se implementa CORS para controlar el acceso desde el frontend
- Las consultas SQL utilizan parámetros para prevenir inyección SQL
- Se recomienda implementar autenticación para entornos de producción

## Contribución

1. Fork el repositorio
2. Crear una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abrir un Pull Request
