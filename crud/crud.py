from pymongo import MongoClient
from bson.objectid import ObjectId
import sys

MONGO_URI = "mongodb://admin:mongopassword@localhost:27017/?authSource=admin"

def conectar_mongodb():
    """Intenta conectar a MongoDB local y devuelve la colección"""
    try:
        cliente = MongoClient(MONGO_URI)
        # Verificar conexión
        cliente.admin.command('ping')
        print("✅ Conectado a MongoDB local correctamente\n")
        db = cliente["libreria"]       # Base de datos
        coleccion = db["libros"]       # Colección
        return coleccion
    except Exception as e:
        print(f"❌ Error de conexión a MongoDB: {e}")
        print("Asegúrate de que el servicio MongoDB esté corriendo")
        sys.exit(1)

# ------------------------------------------------------------
# 2. FUNCIÓN AUXILIAR PARA MOSTRAR UN LIBRO
# ------------------------------------------------------------
def mostrar_libro(libro):
    print(f"ID: {str(libro['_id'])}")
    print(f"Título: {libro['titulo']}")
    print(f"Autor: {libro['autor']}")
    print(f"Año: {libro['anio']}")
    print(f"Precio: ${libro['precio']:.2f}")
    print(f"Editorial: {libro['editorial']}")
    print(f"ISBN: {libro['isbn']}")
    print("-" * 35)

# ------------------------------------------------------------
# 3. OPERACIONES CRUD
# ------------------------------------------------------------
def crear_libro(coleccion):
    print("\n--- NUEVO LIBRO ---")
    titulo = input("Título: ").strip()
    if not titulo:
        print("❌ El título es obligatorio")
        return
    autor = input("Autor: ").strip()
    if not autor:
        print("❌ El autor es obligatorio")
        return
    editorial = input("Editorial: ").strip()
    if not editorial:
        print("❌ La editorial es obligatoria")
        return
    isbn = input("ISBN: ").strip()
    if not isbn:
        print("❌ El ISBN es obligatorio")
        return
    
    try:
        anio = int(input("Año: "))
        precio = float(input("Precio: "))
    except ValueError:
        print("❌ Año debe ser número entero y precio número decimal")
        return
    
    libro = {
        "titulo": titulo,
        "autor": autor,
        "editorial": editorial,
        "isbn": isbn,
        "anio": anio,
        "precio": precio
    }
    resultado = coleccion.insert_one(libro)
    print(f"✅ Libro insertado con ID: {resultado.inserted_id}")

def listar_libros(coleccion):
    print("\n--- LISTA DE LIBROS ---")
    libros = coleccion.find()
    cont = 0
    for libro in libros:
        mostrar_libro(libro)
        cont += 1
    if cont == 0:
        print("📭 No hay libros en la base de datos.")

def buscar_libro_por_id(coleccion):
    id_str = input("Ingrese el ID del libro: ").strip()
    if not ObjectId.is_valid(id_str):
        print("❌ ID inválido (debe ser un ObjectId de 24 caracteres hex)")
        return
    try:
        libro = coleccion.find_one({"_id": ObjectId(id_str)})
        if libro:
            mostrar_libro(libro)
        else:
            print("❌ Libro no encontrado.")
    except Exception as e:
        print(f"❌ Error: {e}")

def actualizar_libro(coleccion):
    id_str = input("ID del libro a actualizar: ").strip()
    if not ObjectId.is_valid(id_str):
        print("❌ ID inválido")
        return
    
    try:
        libro = coleccion.find_one({"_id": ObjectId(id_str)})
        if not libro:
            print("❌ Libro no encontrado.")
            return
        
        print("Deje en blanco para mantener el valor actual.")
        titulo = input(f"Nuevo título [{libro['titulo']}]: ").strip()
        autor = input(f"Nuevo autor [{libro['autor']}]: ").strip()
        editorial = input(f"Nueva editorial [{libro['editorial']}]: ").strip()
        isbn = input(f"Nuevo ISBN [{libro['isbn']}]: ").strip()
        
        anio = libro['anio']
        anio_str = input(f"Nuevo año [{libro['anio']}]: ").strip()
        if anio_str:
            try:
                anio = int(anio_str)
            except:
                print("Año inválido, se mantiene el anterior")
        
        precio = libro['precio']
        precio_str = input(f"Nuevo precio [{libro['precio']}]: ").strip()
        if precio_str:
            try:
                precio = float(precio_str)
            except:
                print("Precio inválido, se mantiene el anterior")
        
        actualizacion = {"$set": {}}
        if titulo:
            actualizacion["$set"]["titulo"] = titulo
        if autor:
            actualizacion["$set"]["autor"] = autor
        if editorial:
            actualizacion["$set"]["editorial"] = editorial
        if isbn:
            actualizacion["$set"]["isbn"] = isbn
        if anio_str and anio != libro['anio']:
            actualizacion["$set"]["anio"] = anio
        if precio_str and precio != libro['precio']:
            actualizacion["$set"]["precio"] = precio
        
        if actualizacion["$set"]:
            coleccion.update_one({"_id": ObjectId(id_str)}, actualizacion)
            print("✅ Libro actualizado.")
        else:
            print("⚠️ No se realizaron cambios.")
    except Exception as e:
        print(f"❌ Error al actualizar: {e}")

def eliminar_libro(coleccion):
    id_str = input("ID del libro a eliminar: ").strip()
    if not ObjectId.is_valid(id_str):
        print("❌ ID inválido")
        return
    try:
        resultado = coleccion.delete_one({"_id": ObjectId(id_str)})
        if resultado.deleted_count > 0:
            print("✅ Libro eliminado.")
        else:
            print("❌ Libro no encontrado.")
    except Exception as e:
        print(f"❌ Error: {e}")

# ------------------------------------------------------------
# 4. MENÚ PRINCIPAL
# ------------------------------------------------------------
def menu():
    coleccion = conectar_mongodb()
    
    while True:
        print("\n" + "="*35)
        print("📚 CRUD DE LIBROS CON MONGODB")
        print("="*35)
        print("1. Crear libro")
        print("2. Listar todos los libros")
        print("3. Buscar libro por ID")
        print("4. Actualizar libro")
        print("5. Eliminar libro")
        print("6. Salir")
        
        opcion = input("Elige una opción: ").strip()
        
        if opcion == "1":
            crear_libro(coleccion)
        elif opcion == "2":
            listar_libros(coleccion)
        elif opcion == "3":
            buscar_libro_por_id(coleccion)
        elif opcion == "4":
            actualizar_libro(coleccion)
        elif opcion == "5":
            eliminar_libro(coleccion)
        elif opcion == "6":
            print("👋 ¡Hasta luego!")
            break
        else:
            print("❌ Opción inválida. Intenta de nuevo.")

if __name__ == "__main__":
    menu()
