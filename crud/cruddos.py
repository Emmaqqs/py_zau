from pymongo import MongoClient
from bson import ObjectId



# Crear conexión con MongoDB local
cliente = MongoClient("mongodb://admin:mongopassword@localhost:27017/?authSource=admin")

# Seleccionar la base de datos
db = cliente["libreria"]

# Seleccionar la colección
coleccion = db["libros"]



def crear_libro():
    print("\n--- AGREGAR LIBRO ---")

    titulo = input("Título: ")
    autor = input("Autor: ")
    anio = int(input("Año: "))
    precio = float(input("Precio: "))

   
    libro = {
        "titulo": titulo,
        "autor": autor,
        "anio": anio,
        "precio": precio
    }


    resultado = coleccion.insert_one(libro)

    print("Libro agregado con ID:", resultado.inserted_id)



def listar_libros():
    print("\n--- LISTA DE LIBROS ---")

    libros = coleccion.find()

    contador = 0

  
    for libro in libros:
        print("ID:", libro["_id"])
        print("Título:", libro["titulo"])
        print("Autor:", libro["autor"])
        print("Año:", libro["anio"])
        print("Precio:", libro["precio"])
        print("-" * 30)
        contador = contador + 1

    if contador == 0:
        print("No hay libros registrados.")


def buscar_libro():
    print("\n--- BUSCAR LIBRO ---")

    id_libro = input("Ingrese el ID: ")

   
    if len(id_libro) != 24:
        print("Libro no encontrado.")
        return

   
    libro = coleccion.find_one({"_id": ObjectId(id_libro)})

    if libro:
        print("ID:", libro["_id"])
        print("Título:", libro["titulo"])
        print("Autor:", libro["autor"])
        print("Año:", libro["anio"])
        print("Precio:", libro["precio"])
    else:
        print("Libro no encontrado.")


def actualizar_libro():
    print("\n--- ACTUALIZAR LIBRO ---")

    id_libro = input("Ingrese el ID del libro: ")

  
    if len(id_libro) != 24:
        print("Libro no encontrado.")
        return


    libro = coleccion.find_one({"_id": ObjectId(id_libro)})

    if not libro:
        print("Libro no encontrado.")
        return

    nuevo_titulo = input("Nuevo título: ")
    nuevo_autor = input("Nuevo autor: ")
    nuevo_anio = int(input("Nuevo año: "))
    nuevo_precio = float(input("Nuevo precio: "))

    coleccion.update_one(
        {"_id": ObjectId(id_libro)},
        {
            "$set": {
                "titulo": nuevo_titulo,
                "autor": nuevo_autor,
                "anio": nuevo_anio,
                "precio": nuevo_precio
            }
        }
    )

    print("Libro actualizado.")


def eliminar_libro():
    print("\n--- ELIMINAR LIBRO ---")

    id_libro = input("Ingrese el ID del libro: ")


    if len(id_libro) != 24:
        print("Libro no encontrado.")
        return


    resultado = coleccion.delete_one({"_id": ObjectId(id_libro)})

  
    if resultado.deleted_count > 0:
        print("Libro eliminado.")
    else:
        print("Libro no encontrado.")



def menu():
    opcion = ""

    while opcion != "6":
        print("\n==============================")
        print(" CRUD DE LIBROS CON MONGODB")
        print("==============================")
        print("1. Crear libro")
        print("2. Listar libros")
        print("3. Buscar libro por ID")
        print("4. Actualizar libro")
        print("5. Eliminar libro")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            crear_libro()

        elif opcion == "2":
            listar_libros()

        elif opcion == "3":
            buscar_libro()

        elif opcion == "4":
            actualizar_libro()

        elif opcion == "5":
            eliminar_libro()

        elif opcion == "6":
            print("Fin del programa.")

        else:
            print("Opción incorrecta.")

menu()