def main():
    filas=int(input("Ingrese la cantidad de filas de carpas que conforman su balneario: "))
    columnas=int(input("Ingrese la cantidad de columnas de carpas que conforman su balneario: "))
    matriz=matrizppal(filas,columnas)
    
    # Mostrar la matriz de forma ordenada
    print("Estado inicial del balneario:")
    for fila in matriz:
        print(fila)

def matrizppal(filas,columnas):
    matriz=[]
    for i in range(filas):
        fila=[]
        for j in range(columnas):
            fila.append(0)
        matriz.append(fila)
    return matriz

if __name__=="__main__":
    main()


