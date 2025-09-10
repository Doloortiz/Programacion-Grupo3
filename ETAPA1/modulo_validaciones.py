#este modulo contiene todas las funciones de validacion para el codigo principal
def leer_entero(mensaje):
    #lee un entero valido (solo dígitos)
    e=1
    while e==1:
        n=input(mensaje)
        if n.isdigit():
            e=0
            return int(n)
        else:
            print("Ingrese solo numeros enteros")

def leer_en_rango(mensaje, minimo, maximo):
    #esto es para que se validen los valores dentro del rango de las matrices
    e=1
    while e==1:
        n=input(mensaje)
        if n.isdigit():
            n=int(n)
            if n>=minimo and n<=maximo:
                e=0
                return n
            else:
                print("Ingrese un numero dentro del rango")
        else:
            print("Ingrese solo numeros enteros")
