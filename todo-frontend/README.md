# To-Do List Frontend

Aplicación frontend moderna para gestionar una lista de tareas, desarrollada con React y Tailwind CSS.

## Características

- ✨ Interfaz moderna y minimalista
- 🌙 Modo oscuro por defecto
- 📱 Diseño completamente responsive
- ⚡ Transiciones suaves
- 🎨 Paleta de colores personalizada
- ♿ Accesibilidad mejorada

## Estructura del Proyecto

```
todo-frontend/
├── src/                    # Código fuente de la aplicación
│   ├── components/        # Componentes reutilizables
│   │   └── TodoList.jsx  # Componente principal de la lista de tareas
│   ├── App.jsx           # Componente raíz de la aplicación
│   ├── main.jsx         # Punto de entrada de la aplicación
│   └── index.css        # Estilos globales y configuración de Tailwind
├── public/               # Archivos públicos estáticos
├── index.html           # Archivo HTML principal
├── vite.config.js       # Configuración de Vite
├── tailwind.config.js   # Configuración de Tailwind CSS
├── postcss.config.js    # Configuración de PostCSS
├── package.json         # Dependencias y scripts
└── eslint.config.js     # Configuración de ESLint
```

## Tecnologías Utilizadas

- React: Biblioteca para construir interfaces de usuario
- Tailwind CSS: Framework de utilidades CSS para diseño moderno
- Axios: Cliente HTTP para realizar peticiones al backend
- Vite: Herramienta de construcción y desarrollo
- PostCSS: Procesador de CSS para Tailwind

## Componentes Principales

### App.jsx

Componente raíz que proporciona el layout principal y contiene el TodoList. Implementa un diseño minimalista con Tailwind CSS.

### TodoList.jsx

Componente principal que maneja toda la lógica de la lista de tareas:

- Añadir nuevas tareas con validación
- Editar tareas existentes mediante un modal
- Marcar tareas como completadas con animaciones
- Eliminar tareas con confirmación visual
- Interfaz responsive y accesible
- Diseño moderno con Tailwind CSS

## Estilos y Diseño

La aplicación utiliza Tailwind CSS para un diseño moderno y consistente:

- Modo oscuro por defecto con colores personalizados
- Transiciones suaves para interacciones
- Diseño responsive que se adapta a todos los dispositivos
- Componentes interactivos con estados hover y focus
- Scrollbar personalizado
- Sombras y efectos visuales sutiles

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

## Instalación y Desarrollo

1. Clonar el repositorio
2. Instalar dependencias:
   ```bash
   npm install
   ```
3. Iniciar el servidor de desarrollo:
   ```bash
   npm run dev
   ```
4. La aplicación estará disponible en `http://localhost:5173`

## Personalización

El diseño puede ser personalizado modificando el archivo `tailwind.config.js`:

- Colores personalizados
- Espaciado y tipografía
- Breakpoints para responsive design
- Plugins adicionales de Tailwind
