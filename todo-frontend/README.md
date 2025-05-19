# To-Do List Frontend

Aplicación frontend para gestionar una lista de tareas, desarrollada con React y Material UI.

## Estructura del Proyecto

```
todo-frontend/
├── src/                    # Código fuente de la aplicación
│   ├── components/        # Componentes reutilizables
│   │   └── TodoList.jsx  # Componente principal de la lista de tareas
│   ├── App.jsx           # Componente raíz de la aplicación
│   ├── main.jsx         # Punto de entrada de la aplicación
│   └── index.css        # Estilos globales
├── public/               # Archivos públicos estáticos
├── index.html           # Archivo HTML principal
├── vite.config.js       # Configuración de Vite
├── package.json         # Dependencias y scripts
└── eslint.config.js     # Configuración de ESLint
```

## Tecnologías Utilizadas

- React: Biblioteca para construir interfaces de usuario
- Material UI: Framework de componentes de diseño
- Axios: Cliente HTTP para realizar peticiones al backend
- Vite: Herramienta de construcción y desarrollo

## Componentes Principales

### App.jsx

Componente raíz que proporciona el layout principal y contiene el TodoList.

### TodoList.jsx

Componente principal que maneja toda la lógica de la lista de tareas:

- Añadir nuevas tareas
- Editar tareas existentes
- Marcar tareas como completadas
- Eliminar tareas
- Interfaz responsive

## Scripts Disponibles

- `npm run dev`: Inicia el servidor de desarrollo
- `npm run build`: Construye la aplicación para producción
- `npm run lint`: Ejecuta el linter para verificar el código
- `npm run preview`: Previsualiza la versión de producción

## Conexión con el Backend

La aplicación se conecta a un servidor backend en `http://localhost:5000` que proporciona una API REST para:

- GET /todos: Obtener todas las tareas
- POST /todos: Crear una nueva tarea
- PUT /todos/:id: Actualizar una tarea
- DELETE /todos/:id: Eliminar una tarea
