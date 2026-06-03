from pymongo import MongoClient
from bson import ObjectId



# Crear conexión con MongoDB local
cliente = MongoClient("mongodb://admin:mongopassword@localhost:27017/?authSource=admin")

# Seleccionar la base de datos
db = cliente["prendasdos"]

# Seleccionar la colección
coleccion = db["prendas"]



def crear_prenda():
    print("\n--- AGREGAR prenda ---")

    producto = input("Producto: ")
    marca = input("Marca: ")
    talla = input("Talla: ")
    precio = float(input("Precio: "))

   
    prenda = {
        "producto": producto,
        "marca": marca,
        "talla": talla,
        "precio": precio
    }


    resultado = coleccion.insert_one(prenda)

    print("prenda agregado con ID:", resultado.inserted_id)



def listar_prendas():
    print("\n--- LISTA DE prendas ---")

    prendas = coleccion.find()

    contador = 0

  
    for prenda in prendas:
        print("ID:", prenda["_id"])
        print("Título:", prenda["producto"])
        print("marca:", prenda["marca"])
        print("Año:", prenda["talla"])
        print("Precio:", prenda["precio"])
        print("-" * 30)
        contador = contador + 1

    if contador == 0:
        print("No hay prendas registrados.")


def buscar_prenda():
    print("\n--- BUSCAR prenda ---")

    id_prenda = input("Ingrese el ID: ")

   
    if len(id_prenda) != 24:
        print("prenda no encontrado.")
        return

   
    prenda = coleccion.find_one({"_id": ObjectId(id_prenda)})

    if prenda:
        print("ID:", prenda["_id"])
        print("Título:", prenda["producto"])
        print("marca:", prenda["marca"])
        print("Año:", prenda["talla"])
        print("Precio:", prenda["precio"])
    else:
        print("prenda no encontrado.")


def actualizar_prenda():
    print("\n--- ACTUALIZAR prenda ---")

    id_prenda = input("Ingrese el ID del prenda: ")

  
    if len(id_prenda) != 24:
        print("prenda no encontrado.")
        return


    prenda = coleccion.find_one({"_id": ObjectId(id_prenda)})

    if not prenda:
        print("prenda no encontrado.")
        return

    nuevo_producto = input("Nuevo título: ")
    nuevo_marca = input("Nuevo marca: ")
    nuevo_talla = int(input("Nuevo año: "))
    nuevo_precio = float(input("Nuevo precio: "))

    coleccion.update_one(
        {"_id": ObjectId(id_prenda)},
        {
            "$set": {
                "producto": nuevo_producto,
                "marca": nuevo_marca,
                "talla": nuevo_talla,
                "precio": nuevo_precio
            }
        }
    )

    print("prenda actualizado.")


def eliminar_prenda():
    print("\n--- ELIMINAR prenda ---")

    id_prenda = input("Ingrese el ID del prenda: ")


    if len(id_prenda) != 24:
        print("prenda no encontrado.")
        return


    resultado = coleccion.delete_one({"_id": ObjectId(id_prenda)})

  
    if resultado.deleted_count > 0:
        print("prenda eliminado.")
    else:
        print("prenda no encontrado.")



def menu():
    opcion = ""

    while opcion != "6":
        print("\n==============================")
        print(" CRUD DE prendas CON MONGODB")
        print("==============================")
        print("1. Crear prenda")
        print("2. Listar prendas")
        print("3. Buscar prenda por ID")
        print("4. Actualizar prenda")
        print("5. Eliminar prenda")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            crear_prenda()

        elif opcion == "2":
            listar_prendas()

        elif opcion == "3":
            buscar_prenda()

        elif opcion == "4":
            actualizar_prenda()

        elif opcion == "5":
            eliminar_prenda()

        elif opcion == "6":
            print("Fin del programa.")

        else:
            print("Opción incorrecta.")

menu()