import sqlite3

def conectar():
    return sqlite3.connect("usuarios.db")

def crear_bd():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS roles(
        id_rol INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre_rol TEXT NOT NULL
    )
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios(
        id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        correo TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        id_rol INTEGER,
        FOREIGN KEY(id_rol)
        REFERENCES roles(id_rol)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS actividades(
        id_actividad INTEGER PRIMARY KEY AUTOINCREMENT,
        descripcion TEXT,
        fecha TEXT,
        id_usuario INTEGER,
        FOREIGN KEY(id_usuario)
        REFERENCES usuarios(id_usuario)
    )
    """)

    cursor.execute("SELECT COUNT(*) FROM roles")

    if cursor.fetchone()[0] == 0:
        cursor.execute(
            "INSERT INTO roles(nombre_rol) VALUES('Administrador')"
        )
        cursor.execute(
            "INSERT INTO roles(nombre_rol) VALUES('Empleado')"
        )
        cursor.execute(
            "INSERT INTO roles(nombre_rol) VALUES('Cliente')"
        )

    conexion.commit()
    conexion.close()
