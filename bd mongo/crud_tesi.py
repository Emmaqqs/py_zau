"""
CRUD TESI CON PYTHON + MONGODB DOCKER
"""

from pymongo import MongoClient
from bson import ObjectId
import sys

# ------------------------------------------------------------
# CONEXIÓN A MONGODB CON DOCKER
# ------------------------------------------------------------

MONGO_URI = "mongodb://admin:mongopassword@localhost:27017/"

def conectar_mongodb():
    try:
        cliente = MongoClient(MONGO_URI)

        # verificar conexión
        cliente.admin.command('ping')

        print("✅ Conectado a MongoDB Docker correctamente\n")

        db = cliente["tesi"]
        coleccion = db["alumnos"]

        return coleccion

    except Exception as e:
        print(f"❌ Error de conexión: {e}")
        sys.exit(1)

# ------------------------------------------------------------
# MOSTRAR ALUMNO
# ------------------------------------------------------------

def mostrar_alumno(alumno):
    print(f"\nID: {alumno['_id']}")
    print(f"Nombre: {alumno['nombre']}")
    print(f"Carrera: {alumno['carrera']}")
    print(f"Semestre: {alumno['semestre']}")
    print(f"Promedio: {alumno['promedio']}")

    print("Materias:")
    for materia in alumno["materias"]:
        print(f" - {materia}")

    print("-" * 40)

# ------------------------------------------------------------
# CREAR ALUMNO
# ------------------------------------------------------------

def crear_alumno(coleccion):

    print("\n--- NUEVO ALUMNO ---")

    nombre = input("Nombre: ").strip()
    carrera = input("Carrera: ").strip()

    try:
        semestre = int(input("Semestre: "))
        promedio = float(input("Promedio: "))
    except:
        print("❌ Datos inválidos")
        return

    materias = input(
        "Materias separadas por coma: "
    ).split(",")

    materias = [m.strip() for m in materias]

    alumno = {
        "nombre": nombre,
        "carrera": carrera,
        "semestre": semestre,
        "promedio": promedio,
        "materias": materias
    }

    resultado = coleccion.insert_one(alumno)

    print(f"✅ Alumno agregado con ID: {resultado.inserted_id}")

# ------------------------------------------------------------
# LISTAR ALUMNOS
# ------------------------------------------------------------

def listar_alumnos(coleccion):

    print("\n--- LISTA DE ALUMNOS ---")

    alumnos = coleccion.find()

    contador = 0

    for alumno in alumnos:
        mostrar_alumno(alumno)
        contador += 1

    if contador == 0:
        print("No hay alumnos registrados")

# ------------------------------------------------------------
# BUSCAR ALUMNO POR ID
# ------------------------------------------------------------

def buscar_alumno(coleccion):

    id_str = input("ID del alumno: ").strip()

    if not ObjectId.is_valid(id_str):
        print("❌ ID inválido")
        return

    alumno = coleccion.find_one({
        "_id": ObjectId(id_str)
    })

    if alumno:
        mostrar_alumno(alumno)
    else:
        print("❌ Alumno no encontrado")

# ------------------------------------------------------------
# ACTUALIZAR ALUMNO
# ------------------------------------------------------------

def actualizar_alumno(coleccion):

    id_str = input("ID del alumno: ").strip()

    if not ObjectId.is_valid(id_str):
        print("❌ ID inválido")
        return

    alumno = coleccion.find_one({
        "_id": ObjectId(id_str)
    })

    if not alumno:
        print("❌ Alumno no encontrado")
        return

    print("\nDeja vacío para mantener el valor actual")

    nombre = input(
        f"Nombre [{alumno['nombre']}]: "
    ).strip()

    carrera = input(
        f"Carrera [{alumno['carrera']}]: "
    ).strip()

    actualizacion = {"$set": {}}

    if nombre:
        actualizacion["$set"]["nombre"] = nombre

    if carrera:
        actualizacion["$set"]["carrera"] = carrera

    if actualizacion["$set"]:

        coleccion.update_one(
            {"_id": ObjectId(id_str)},
            actualizacion
        )

        print("✅ Alumno actualizado")

    else:
        print("⚠️ Sin cambios")

# ------------------------------------------------------------
# ELIMINAR ALUMNO
# ------------------------------------------------------------

def eliminar_alumno(coleccion):

    id_str = input("ID del alumno: ").strip()

    if not ObjectId.is_valid(id_str):
        print("❌ ID inválido")
        return

    resultado = coleccion.delete_one({
        "_id": ObjectId(id_str)
    })

    if resultado.deleted_count > 0:
        print("✅ Alumno eliminado")
    else:
        print("❌ Alumno no encontrado")

# ------------------------------------------------------------
# MENÚ PRINCIPAL
# ------------------------------------------------------------

def menu():

    coleccion = conectar_mongodb()

    while True:

        print("\n" + "=" * 40)
        print("🎓 CRUD TESI + MONGODB")
        print("=" * 40)

        print("1. Crear alumno")
        print("2. Listar alumnos")
        print("3. Buscar alumno")
        print("4. Actualizar alumno")
        print("5. Eliminar alumno")
        print("6. Salir")

        opcion = input("Opción: ").strip()

        if opcion == "1":
            crear_alumno(coleccion)

        elif opcion == "2":
            listar_alumnos(coleccion)

        elif opcion == "3":
            buscar_alumno(coleccion)

        elif opcion == "4":
            actualizar_alumno(coleccion)

        elif opcion == "5":
            eliminar_alumno(coleccion)

        elif opcion == "6":
            print("👋 Hasta luego")
            break

        else:
            print("❌ Opción inválida")

# ------------------------------------------------------------

if __name__ == "__main__":
    menu()