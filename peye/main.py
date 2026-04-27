from validaciones import validar_edad, validar_correo, validar_password, validar_nombre, validar_genero
edad = int(input("Ingrese su edad: "))
correo = input("Ingrese su correo: ")
password = input("Ingrese su contraseña: ")
nombre = input("Ingrese su nombre: ")
genero = input("Ingrese su género F o M: ")
if not validar_edad(edad):
    print("Error: Debe ser mayor de 65 años")
elif not validar_correo(correo):
    print("Error: Correo no válido")
elif not validar_password(password):
    print("Error: Contraseña muy corta (mínimo 8 caracteres)")
elif not validar_nombre(nombre):
    print("Error: Nombre muy corto (mínimo 6 caracteres)")
elif not validar_genero(genero):
    print("Error: Género no válido")
else:
    print("Registro exitoso")
    print(f"Nombre: {nombre}")
    print(f"Edad: {edad}")
    print(f"Correo: {correo}")
    print(f"Género: {genero}")