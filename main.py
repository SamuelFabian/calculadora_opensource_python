from funciones_calculadora import sumar_n_numeros
from funciones_calculadora import multiplicacion_n_numeros
from funciones_calculadora import division_2_numeros
from funciones_calculadora import resolver_para_y

import numpy as np
import matplotlib.pyplot as plt


while True:
    print(''' 
    Bienvenido a mi calculadora, por favor ingresa una opción
    ---------------------------------------------------------
          
    1.-Hacer una suma de N números.
    2.-Hacer una multiplicación de N números.
    3.-Hacer una división de dos números.
    4.-Resolver la posición en Y (Para la ecuación y = mx + b).
          
    0.-Salir del programa.
    ''')

    opcion = int(input('> '))
    if opcion == 0:
        break
    
    elif opcion == 1:
        resultado = sumar_n_numeros()
        print(f'El resultado de tu suma es {resultado}')

    elif opcion == 2:
        resultado = multiplicacion_n_numeros()
        print(f'El resultado es {resultado}')

    elif opcion == 3:
        resultado = division_2_numeros()
        print(f'El resultado es {resultado}')

    elif opcion == 4:
        resultado = resolver_para_y()
        print(f'El resultado es {resultado}')

        x = np.linspace(-10, 10)
        y = (resultado['pendiente'] * x) + resultado['ordenada_al_origen']

        fig, ax = plt.subplots()
        ax.plot(x, y, linewidth = 2.0)
        ax.plot(resultado['punto_en_x'], resultado['resultado'], 'yo')
        

        # Limita la gráfica hasta ciertos valores
        # ax.set(xlim = (0, 8), xticks=np.arange(1, 8), ylim = (0, 8), yticks=np.arange(1, 8) )
        ax.grid(True, linestyle = '-')
        plt.show()

    else:
        print('Ejecuta una opción válida :( ')


print('-------------------------------------')
print('Bye, gracias por usar mi calculadora')
