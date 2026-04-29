def validar_edad(edad):
    return edad >= 65
def validar_correo(correo):
    return "@" in correo and "." in correo
def validar_password(password):
    return len(password) >= 8
def validar_nombre(nombre):
    return len(nombre) > 5
def validar_genero(genero):
    return "Femenino" in genero