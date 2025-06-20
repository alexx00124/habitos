# Habitos - App de gestión de hábitos estilo Habitica

**Habitos** es una aplicación web liviana construida con HTML, CSS y Python usando **PyScript** y **MongoDB** como base de datos. Está diseñada para ayudarte a crear y marcar hábitos, tareas diarias y pendientes de manera sencilla.

## Estructura del proyecto

habitos/
│
├── static/
│ ├── app.py
│ ├── database.py
│ └── styles/
│  ├── styles.css
│  └── img/
│    └── login_register.jfif
│
├── templates/
│ ├── habitos.html
│ ├── login.html
│ └── register.html
│
├── pyscript.config.toml (opcional)
└── README.md

## Funcionalidades

- Registro e inicio de sesión de usuario (Frontend)
- Carga de imagen de perfil (Frontend)
- Añadir tareas a tres categorías:
  - Hábitos
  - Tareas diarias
  - Pendientes
- Marcar tareas como completadas (en desarrollo)
- Estilo personalizado inspirado en Habitica

## Tecnologías utilizadas

- Python (usando [PyScript](https://pyscript.net))
- MongoDB (como base de datos no relacional)
- HTML5 + CSS3 (Frontend)
- Imágenes y estilos personalizados

## Para la activacion del entorno virtual

- source venv/bin/activate (si lo haces en gitbash o /macOS)
- venv\Scripts\activate (para windows es diferente)

## Instala las dependencias
**Con el entorno virtual activo**, instala los paquetes necesarios:

- pip install -r requirements.txt

## Ejecuta la aplicación

- python server.py

la aplicacion se debe abrir en el puerto **http://localhost:5000** 
