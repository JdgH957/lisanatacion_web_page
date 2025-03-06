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

## Ejecución de la aplicación
Para iniciar la aplicación, ejecutar el siguiente comando:
```sh
uvicorn app.main:app --reload
```

