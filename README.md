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
   python -m venv venv
   ```
5. Activar el entorno virtual:
   ```sh
   .\venv\Scripts\activate
   .\venv\Scripts\Activate '''alguno de esos dos'''

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

5. Levantar el Contenedor de PostgreSQL con Docker Compose
   ```sh
   Si ya tienes docker-compose.yml en el repo, solo ejecuta:
   docker compose up -d
   ```
6. Crear las Tablas en la Base de Datos
   ```sh
   python setDB.py
   RECOMENDABLE CORRER ESTE COMANDO CUANDO LA BASE DE DATOS DE ERRORES
   O SE DEBA ACTUALIZAR
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
   -EN LA CARPETA ALEMBIC/VERSIONS/ ESTARAN LOS CAMBIOS QUE SE VAN HACIENDO SI CREAS
   UNA NUEVA TABLA O UN ATRIBUTO ETC TIENES QUE HACER: alembic revision --autogenerate -m "NUEVO CAMBIO"
   -correr alembic upgrade head Y VISUALIZAR LOS CAMBIOS, ES IDEA SIEMPRE REVISAR QUE ESTEMOS EN LA BASE ACTUALIZADA


## Ejecución de la aplicación
Para iniciar la aplicación, ejecutar el siguiente comando:
```sh
uvicorn app.main:app --reload
```

