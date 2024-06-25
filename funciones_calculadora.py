import numpy as np

def sumar_n_numeros():
    numeros_a_sumar = int(input('Cuántos números deseas sumar: '))
    lista_numeros = []

    for numero in range (0, numeros_a_sumar):
        numero_a_sumar = float(input( f'Ingresa el número {numero + 1} a sumar: '))
        lista_numeros.append(numero_a_sumar)

    return sum(lista_numeros)


def multiplicacion_n_numeros():
    resultado = 1
    numeros_a_multiplicar = int(input('Cuántos números deseas multiplicar: '))
    for numero in range (0, numeros_a_multiplicar):
        numeros_a_multiplicar = float(input(f'Ingresa el {numero + 1} a multiplicar: '))
        resultado *= numeros_a_multiplicar

    return resultado


def division_2_numeros():
    numerador = float(input('Ingresa el numerador: '))
    denominador = float(input('Ingresa el denominador: '))
    if denominador == 0:
        print('No puedes dividir entre 0')
        return None
    
    return numerador / denominador

# y = mx + b
def resolver_para_y():
    pendiente = float(input('Por favor ingrese la pendiente: '))
    ordenada_al_origen = float(input('Por favor ingrese la ordenada al origen: '))
    punto_en_x = int(input('Ingrese un punto en x: '))

    resultado = (pendiente * punto_en_x) + ordenada_al_origen
    return {'resultado':resultado, 'pendiente':pendiente, 'ordenada_al_origen':ordenada_al_origen, 'punto_en_x':punto_en_x}

def ingresar_valores_en_matriz(filas, columnas):
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            valor = float(input(f'Ingresa el valor para [{i + 1}, {j+1}]: '))
            fila.append(valor)
        matriz.append(fila)

    return np.array(matriz)

def obtener_matriz():
    filas = int(input('Ingresa el número de filas: '))
    columnas = int(input('Ingresa el número de columnas: '))
    print('Ingresa los valores de la primera matriz')
    matriz1 = ingresar_valores_en_matriz(filas, columnas)
    print('Ingresa los valores de la segunda matriz')
    matriz2 = ingresar_valores_en_matriz(filas, columnas)
    return matriz1, matriz2

def sumar_matrices():
    matriz1, matriz2 = obtener_matriz()
    resultado = matriz1 + matriz2
    
    return resultado

def restar_matrices():
    matriz1, matriz2 = obtener_matriz()
    resultado = matriz1 - matriz2

    return resultado

def multiplicar_matrices():
    matriz1, matriz2 = obtener_matriz()
    resultado = np.dot(matriz1, matriz2)

    return resultado

