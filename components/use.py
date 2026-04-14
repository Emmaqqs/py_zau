from calculadora import Calculadora
def procesar(op):
    match op:
        case 1:
            return print(Calculadora.restar(10,5))
        case 2:
            return print(Calculadora.sumar(10,5))
        case 3:
            return print(Calculadora.multiplicar(10,5))
        case 4:
            return print(Calculadora.dividir(10,5))
print(procesar (4))