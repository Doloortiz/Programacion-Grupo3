import random
from modulo_validaciones import leer_entero, leer_en_rango

# matrizC es para las carpas (ocupación: 0=libre, 1=ocupada)
def matrizppal(filas, columnas):
    # Crea una matriz de ceros de tamaño filas x columnas
    matrizC = [[0]*columnas for i in range(filas)]
    return matrizC

# Matrizprecios (matrizP) es para los precios de las carpas
def matrizprecios(filas, columnas):
    # Precios enteros aleatorios fijos en el rango 1000..5000
    P_MIN, P_MAX = 1000, 5000
    matrizP = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila.append(random.randint(P_MIN, P_MAX))
        matrizP.append(fila)
    return matrizP

def pedir_posicion(mC):
    # Pide una posición válida dentro de la matriz mC 
    filas = len(mC)
    cols = len(mC[0])
    f = leer_en_rango(f"Ingrese la FILA (1..{filas}): ", 1, filas)
    c = leer_en_rango(f"Ingrese la COLUMNA (1..{cols}): ", 1, cols)
    return f, c

# Mostrar matrices prolijo
def mostrarMatrizC(mc,f,c):
    for i in range(0,f):
        fila_str='  ' #Espacios
        for j in range(0,c):
            fila_str += str(mc[i][j])+'  '
        print(fila_str)

def mostrarMatrizP(mp,f,c):
    print("Precios de las carpas:")
    for i in range(0,f):
        fila_str= '  ' 
        for j in range(0,c):
            fila_str += str(mp[i][j])+'  '
        print(fila_str)

def DisponibilidadCarpas(mC):
    # Cuenta carpas libres en toda la matriz
    disponibles = 0
    for fila in mC:
        for carpa in fila:
            if carpa == 0:  # libre
                disponibles += 1
    print(f"Disponibilidad total de carpas: {disponibles}")

def ReservarCarpa(mC):
    # Reserva una carpa si está libre
    print("RESERVAR UNA CARPA:")
    print("-"*75)
    e = 1
    while e == 1:
        f, c = pedir_posicion(mC)
        if mC[f-1][c-1] == 0:  # 0=libre, 1=ocupada
            mC[f-1][c-1] = 1
            print("Carpa reservada con éxito.")
            e=0
        else:
            reservar_otra = leer_entero("La carpa ya esta reservada ¿Desea reservar otra? (1=Sí, 2=No): ")
            while reservar_otra != 1 and reservar_otra != 2:
                print("Opción inválida. Intente nuevamente.") 
                reservar_otra = leer_entero("¿Desea reservar otra? (1=Sí, 2=No): ")
            if reservar_otra == 1:
                e = 1
            else:
                e = 0

def CancelarCarpa(mC):
    # Verifica si hay alguna reserva antes de pedir posición
    print("CANCELAR UNA CARPA:")
    print("-"*75)
    hay_reserva=False
    for fila in mC:
        for carpa in fila:
            if carpa==1:
                hay_reserva=True
    if hay_reserva==False:
        print("No hay reservas para cancelar.")
        return
    else:
        e = 1
        while e == 1:
    # Cancela una reserva si está ocupada
            f, c = pedir_posicion(mC)
            if mC[f-1][c-1] == 1:
                mC[f-1][c-1] = 0
                print("Reserva cancelada.")
                return 
            else:
                cancelar_otra = leer_entero("La carpa no está ocupada ¿Desea desocupar otra? (1=Sí, 2=No): ")
                while cancelar_otra != 1 and cancelar_otra != 2:
                    print("Opción inválida. Intente nuevamente.") 
                    cancelar_otra = leer_entero("¿Desea desocupar otra? (1=Sí, 2=No): ")
                if cancelar_otra == 1:
                    e = 1
                else:
                    e = 0

def BuscarCarpa(mC, mP):
    # Muestra estado y precio de una carpa específica
    print("BUSCAR UNA CARPA:")
    print("-"*75)
    f, c = pedir_posicion(mC)
    if mC[f-1][c-1] == 1:
        print(f"La carpa en la fila {f}, columna {c} está ocupada")
    else:
        print(f"La carpa en la fila {f}, columna {c} está libre")
        print(f"El precio de la carpa es: ${mP[f-1][c-1]} pesos")

def estadisticas(mC, mP, fil):
    print("-"*75)
    # Resumen de carpas libres, ocupadas, ingresos y porcentaje de ocupación
    Carpas_libres = 0
    Carpas_Ocupadas = 0
    IngresosTotales = 0

    for i in range(len(mC)):
        for j in range(len(mC[0])):  # columnas correctas con len(mC[0])
            if mC[i][j] == 0:
                Carpas_libres += 1
            else:
                Carpas_Ocupadas += 1
                IngresosTotales += mP[i][j]

    print(f"Cantidad de carpas libres: {Carpas_libres}")
    print(f"Cantidad de carpas ocupadas: {Carpas_Ocupadas}")
    print(f"Ingresos totales: ${IngresosTotales}")
    
    # sacar estadistica
    totalCarpas = Carpas_libres + Carpas_Ocupadas
    porcentaje = (Carpas_Ocupadas / totalCarpas) * 100
    print(f"Porcentaje de ocupación: {porcentaje:.2f}%")
    print()
    # sumar matriz precios
    total=0
    for fil in mP:
        for elem in fil:
            total += elem
    print(f"Suma total del precio de las carpas: ${total}")
    promedio = lambda a, b, c : a //(b*c)
    resultado = promedio(total, len(mP), len(mP[0])) #mP[0] devuelve el numero de columnas
    print(f"Promedio de los precios de las carpas: ${resultado}")
    print()
    
    # División por sectores (filas): 
    print(f"El balneario se divide en {len(mP)} sectores.")
    sectores = []  
    for fil in mP:
        sectores.append(fil[:])   # Agrego cada fila a la lista
    for i in range(len(sectores)):
        sector = sectores[i]
        print(f"\nSector {i+1}:")
        print(f"\tPrecio total de las carpas: ${sum(sector)}")
        print(f"\tPrecio más bajo: ${min(sector)}")
        print(f"\tPrecio más alto: ${max(sector)}")
        print(f"\tPrecios ordenados: {sorted(sector)}")


def main():
    # Pide dimensiones del balneario (>=1)
    filas = leer_en_rango("Ingrese la cantidad de filas de carpas que conforman su balneario (>=1): ", 1, 10000)
    columnas = leer_en_rango("Ingrese la cantidad de columnas de carpas que conforman su balneario (>=1): ", 1, 10000)

    matrizC = matrizppal(filas, columnas)
    matrizP = matrizprecios(filas, columnas)

    # Menú principal
    e = 1
    while e == 1:
        print()
        print("-"*75)
        print()
        print("Seaside Resort Manager. El mejor sistema para los balnearios de Argentina.")
        print()
        print("-"*75) 
        print("MENU")
        print("1) Mostrar disponibilidad de carpas")
        print("2) Reservar carpa")
        print("3) Cancelar una reserva")
        print("4) Buscar una carpa")
        print("5) Ver precios de las carpas")
        print("6) Ver estadísticas")
        print("7) Finalizar carga")
        nro = leer_entero("Ingrese una opción (1-7): ")
        while nro < 1 or nro > 7:
            print("Opción inválida. Intente nuevamente.")
            nro = leer_entero("Ingrese una opción (1-7): ")
        print()

        if nro == 1:
            print("Matriz de carpas:")
            mostrarMatrizC(matrizC,filas,columnas)
            DisponibilidadCarpas(matrizC)
        elif nro == 2:
            ReservarCarpa(matrizC)
        elif nro == 3:
            CancelarCarpa(matrizC)
        elif nro == 4:
            BuscarCarpa(matrizC, matrizP)
        elif nro == 5:
            mostrarMatrizP(matrizP,filas,columnas)
        elif nro == 6:
            print("ESTADÍSTICAS:")
            estadisticas(matrizC, matrizP, filas)
        elif nro == 7:
            print("Gracias por usar nuestro sistema, hasta la próxima!")
            print()
            print("ESTADÍSTICAS FINALES:")
            estadisticas(matrizC, matrizP, filas)
            e = 0  # salir del bucle while

if __name__ == "__main__":
    main()
