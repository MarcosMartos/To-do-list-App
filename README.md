# To-Do List Application

Aplicación completa de gestión de tareas desarrollada con React (Frontend) y Flask (Backend).

## 📋 Descripción

Sistema de gestión de tareas moderno y responsive que permite a los usuarios crear, editar, marcar como completadas y eliminar tareas. La aplicación está construida con una arquitectura cliente-servidor, utilizando tecnologías modernas tanto en el frontend como en el backend.

## 🚀 Características Principales

### Frontend

- ✨ Interfaz moderna con Tailwind CSS
- 🌙 Modo oscuro por defecto
- 📱 Diseño completamente responsive
- ⚡ Transiciones suaves
- 🎨 Paleta de colores personalizada
- ♿ Accesibilidad mejorada

### Backend

- 🚀 API RESTful completa
- 🔒 Base de datos PostgreSQL
- 🔄 Soporte CORS
- 📝 CRUD completo
- 🔍 Documentación detallada
- ⚡ Configuración mediante variables de entorno

## 🏗️ Arquitectura del Proyecto

```
todo-list/
├── todo-frontend/          # Aplicación React
│   ├── src/               # Código fuente
│   │   ├── components/    # Componentes React
│   │   ├── App.jsx       # Componente principal
│   │   └── index.css     # Estilos globales
│   ├── public/           # Archivos estáticos
│   └── package.json      # Dependencias
│
└── todo-backend/          # API Flask
    ├── app.py            # Aplicación principal
    ├── db.py             # Configuración DB
    ├── create-database.py # Script de inicialización
    └── requirements.txt   # Dependencias Python
```

## 🛠️ Tecnologías Utilizadas

### Frontend

- React: Biblioteca para interfaces de usuario
- Tailwind CSS: Framework de utilidades CSS
- Axios: Cliente HTTP
- Vite: Herramienta de construcción
- PostCSS: Procesador de CSS

### Backend

- Flask: Framework web Python
- PostgreSQL: Base de datos
- psycopg2: Adaptador PostgreSQL
- Flask-CORS: Soporte CORS
- python-dotenv: Variables de entorno

## 📋 Requisitos Previos

### Frontend

- Node.js 16 o superior
- npm 7 o superior

### Backend

- Python 3.8 o superior
- PostgreSQL 12 o superior
- pip (gestor de paquetes Python)

## 🚀 Instalación y Configuración

### 1. Clonar el Repositorio

```bash
git clone <url-del-repositorio>
cd todo-list
```

### 2. Configurar el Backend

```bash
cd todo-backend

# Crear entorno virtual
python -m venv venv

# Activar entorno virtual
# Windows:
.\venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt

# Crear archivo .env
echo "DB_HOST=localhost
DB_NAME=todo_app
DB_USER=postgres
DB_PASSWORD=tu_contraseña" > .env

# Inicializar base de datos
python create-database.py

# Iniciar servidor backend
python app.py
```

### 3. Configurar el Frontend

```bash
cd todo-frontend

# Instalar dependencias
npm install

# Iniciar servidor de desarrollo
npm run dev
```

## 🌐 Acceso a la Aplicación

- Frontend: http://localhost:5173
- Backend API: http://localhost:5000

## 📚 Documentación de la API

### Endpoints Disponibles

#### GET /todos

- Obtiene todas las tareas
- Respuesta: Lista de tareas en JSON

#### POST /todos

- Crea una nueva tarea
- Body: `{ "title": "Nueva tarea" }`

#### PUT /todos/:id

- Actualiza una tarea
- Body: `{ "completed": true }`

#### DELETE /todos/:id

- Elimina una tarea

Para más detalles, consultar la [documentación del backend](todo-backend/README.md).

## 💻 Desarrollo

### Frontend

```bash
cd todo-frontend
npm run dev     # Desarrollo
npm run build   # Producción
npm run lint    # Linting
```

### Backend

```bash
cd todo-backend
python app.py   # Desarrollo
```

## 🚀 Despliegue

### Frontend

1. Construir la aplicación:
   ```bash
   cd todo-frontend
   npm run build
   ```
2. Servir los archivos estáticos con un servidor web (Nginx/Apache)

### Backend

1. Configurar servidor WSGI (Gunicorn)
2. Configurar proxy inverso (Nginx/Apache)
3. Implementar HTTPS
4. Configurar variables de entorno de producción

## 🔒 Seguridad

- Credenciales de base de datos en variables de entorno
- CORS configurado para el frontend
- Consultas SQL parametrizadas
- Recomendado: Implementar autenticación para producción

## 🤝 Contribución

1. Fork el repositorio
2. Crear rama feature (`git checkout -b feature/AmazingFeature`)
3. Commit cambios (`git commit -m 'Add AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abrir Pull Request

## 📝 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 👥 Autores

- Tu Nombre - [@tu-usuario](https://github.com/tu-usuario)

## 🙏 Agradecimientos

- [React](https://reactjs.org/)
- [Flask](https://flask.palletsprojects.com/)
- [Tailwind CSS](https://tailwindcss.com/)
- [PostgreSQL](https://www.postgresql.org/)
