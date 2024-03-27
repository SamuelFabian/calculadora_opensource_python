from funciones_calculadora import sumar_n_numeros


while True:
    print(''' 
    Bienvenido a mi calculadora, por favor ingresa una opción
    ---------------------------------------------------------
          
    1.-Hacer una suma de N números.
    2.-Hacer una multiplicación de N números.
    3.-Hacer una división de dos números.
          
    0.-Salir del programa.
    ''')

    opcion = int(input('> '))
    if opcion == 0:
        break
    elif opcion == 1:
        resultado = sumar_n_numeros()
        print(f'El resultado de tu suma es {resultado}')


print('-------------------------------------')
print('Bye, gracias por usar mi calculadora')
