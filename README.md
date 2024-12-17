# Task Management App - Streamlit

Este proyecto es una aplicación de gestión de tareas desarrollada con **Streamlit** y **SQLAlchemy** para gestionar las tareas pendientes de manera sencilla. Permite agregar, actualizar, eliminar y listar tareas, con soporte para persistencia en una base de datos SQL.

## Funcionalidades

1. **Agregar Tarea**: Permite agregar nuevas tareas con título, descripción y prioridad.
2. **Actualizar Tarea**: Permite actualizar el título, descripción y prioridad de una tarea existente.
3. **Eliminar Tarea**: Permite eliminar tareas existentes de la base de datos.
4. **Listar Tareas**: Muestra todas las tareas registradas en la base de datos.

## Requisitos

Para ejecutar este proyecto, necesitarás tener las siguientes herramientas instaladas en tu sistema:

- **Python** (preferiblemente versión 3.8 o superior)
- **Streamlit**: Para la interfaz web.
- **SQLAlchemy**: Para la gestión de la base de datos.
- **SQLite** (o cualquier base de datos compatible con SQLAlchemy)

## Instalación

Sigue estos pasos para configurar el proyecto:

### 1. Clonar el repositorio

Primero, clona este repositorio en tu máquina local:

```bash
git clone https://github.com/tu_usuario/task-management-app.git
cd task-management-app
```

### 2. Crear un entorno virtual (opcional pero recomendado)

Es recomendable usar un entorno virtual para gestionar las dependencias del proyecto:

```bash
  python3 -m venv venv
  source venv/bin/activate  # En Linux/macOS
  venv\Scripts\activate     # En Windows
```

### Intalar dependencias:

Instala las dependencias neesarias:

```bash
pip install -r requeriments.txt
```

### Configurar la base de datos

El proyecto usa SQLAlchemy para interactuar con la base de datos. Asegúrate de tener SQLite (o la base de datos que prefieras) configurada para usarla con SQLAlchemy. La configuración de la base de datos se maneja dentro del archivo db.py.

### Ejecutar la aplicación

una vez que todo este configurado, puedes ejecutar la apliacacion con el siguiente comando:

```bash
streamlit run main.py
```

Esto iniciara el servidor de Streamlit y podras acceder a la apliacacion a traves de tu navegador en la direccion
https://localhost:8501

## Estructura del proyecto

```bash
task-management-app/
|
| - main.py
| - db.py
| - models.py
| - requeriments.txt
| - tasks.py
| - README.md
```

### Detalles de cada archivo:

 - **main.py**: Contiene la lógica principal de la aplicación, donde se agregan, actualizan, eliminan y listan las tareas.
- **db.py**: Configuración de la base de datos usando SQLAlchemy. Aquí se inicializa la conexión con la base de datos y se configura el manejo de las sesiones.
- **models.py**: Define el modelo de datos de las tareas (tabla Task) usando SQLAlchemy.
- **requirements.txt**: Lista de dependencias que se deben instalar para ejecutar la aplicación.


## Mejoras Futuras

- Implementar autenticación para que solo los usuarios autorizados puedan gestionar tareas.
- Agregar filtros de busqueda y ordenamiento para facilitar la visualizacion de tareas
- Mejorar la interfaz con mas funcionalidades y diseño
- Agregar un sistema de notificaciones para tareas urgentes o proximas a vencer


## Created by
[NicolasFue05][https://github.com/NicolasFue05]
