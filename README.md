# Proyecto lisanatacion_web_page

## Requisitos

Se recomienda utilizar **Visual Studio Code** como entorno de desarrollo.

### Instalación de herramientas necesarias
1. Instalar **Python 3.11.9**.
2. Instalar las siguientes extensiones de **Visual Studio Code**:
   - MagicPython
   - Pylance
   - Python
   - Python Debugger

## Configuración del entorno

1. Clonar el repositorio de GitHub de forma local.
2. Abrir **Visual Studio Code** y cargar la carpeta `lisanatacion_web_page`.
3. Abrir una terminal dentro de **VS Code**.
4. Crear un entorno virtual ejecutando el siguiente comando:
   ```sh
   python3 -m venv venv
   ```
5. Activar el entorno virtual:
   ```sh
   .\venv\Scripts\activate
   ```
6. Instalar las dependencias del proyecto:
   ```sh
   pip install -r requirements.txt
   ```
## Configuración de Base de datos
1. Para conectarte a PostgreSQL, instala psycopg2 y SQLAlchemy:
   ```sh
   pip install psycopg2-binary sqlalchemy pydantic[email]
   ```
2. Instalar docker desktop 
   ```sh    
   Elegir la opcion Use recommended settings
   ```
3. Verificar instalacion
   ```sh
   docker --version
   ```
4. Probar contenedor de prueba
   ```sh
   docker run hello-world 
   revisar respuesta en docker desktop
   ```
5. Levantar el Contenedor de PostgreSQL con Docker Compose
   ```sh
   Si ya tienes docker-compose.yml en el repo, solo ejecuta:
   docker compose up -d
   ```
6. Crear las Tablas en la Base de Datos
   ```sh
   python create_db.py
   SOLO SE CORRE LA PRIMERA VEZ NO REPETIR
   ```
7. Probar la Conexión a PostgreSQL
   ```sh
   python test_queries.py
   Si todo está bien, verás un mensaje con la lista de usuarios registrados.
   ```
8. instalar depenencia
   ```sh
   pip install python-jose[cryptography] passlib[bcrypt] python-multipart
   ```
9. modificar tablas 
   ```sh
   pip install alembic
   ```
10. como usar almebic
   -correr alembic init alembic va a crear en la raiz el doc de alembic.ini y la carpeta alembic 
   -alembic revision --autogenerate -m "agregar tablax o atributo x"
   -correr alembic upgrade head y visualizar los cambios en Dbeaver

## Ejecución de la aplicación
Para iniciar la aplicación, ejecutar el siguiente comando:
```sh
uvicorn app.main:app --reload
```

