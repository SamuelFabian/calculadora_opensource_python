def sumar_n_numeros():
    numeros_a_sumar = int(input('Cuántos números deseas sumar: '))
    lista_numeros = []

    for numero in range (0, numeros_a_sumar):
        numero_a_sumar = float(input( f'Ingresa el número {numero + 1} a sumar: '))
        lista_numeros.append(numero_a_sumar)

    return sum(lista_numeros)

