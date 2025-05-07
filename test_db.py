import psycopg2

# Datos de conexión
DB_NAME = "liga_natacion"
DB_USER = "admin"
DB_PASSWORD = "admin"
DB_HOST = "localhost"
DB_PORT = "5432"

try:
    # Conectar a PostgreSQL
    conn = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )
    print("✅ Conexión exitosa a PostgreSQL en Docker")

    # Crear un cursor para ejecutar consultas
    cur = conn.cursor()

    # Ejecutar una consulta simple
    cur.execute("SELECT version();")
    postgres_version = cur.fetchone()
    print("📌 PostgreSQL Version:", postgres_version)

    # Cerrar cursor y conexión
    cur.close()
    conn.close()

except Exception as e:
    print("❌ Error conectando a PostgreSQL:", e)
