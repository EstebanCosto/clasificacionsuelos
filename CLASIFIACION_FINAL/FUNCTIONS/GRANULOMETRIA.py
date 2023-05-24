from FUNCTIONS.VAL_ENTRADA import *
# Importar librerias
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def curva_granulometrica():
    # Crear un DataFrame con los datos de entrada
    Estructura = pd.DataFrame({
        'Tamiz': nombres_tamices,
        'Abertura': aberturas_tamices,
        '% pasa': porcentaje_pasa
    })

    print(Estructura)
    # Ordenar los datos por las aberturas de los tamices
    Estructura = Estructura.sort_values(by='Abertura', ascending=True)

    # Crear las listas de límites inferior, superior y de tamaño de tamiz
    tamiz = [37.5,25,19,9.5,4.75,2,0.85,0.425,0.25,0.15,0.075]
    limite_inferior = [100,84.82,55.96,36.92,24.27,16.01,10.67,7.04,4.64,3.06]
    limite_superior = [100,89.6,67.91,51.46,38.90,29.48,22.49,17.05,12.92,9.79]
    tamiz_limite = [25,19,9.5,4.75,2.36,1.18,0.6,0.3,0.15,0.0075]

    # Graficar los límites inferior y superior, y la curva granulométrica
    plt.grid()
    plt.plot(tamiz_limite, limite_inferior, 'r', label = "Límite Inferior" )
    plt.plot(tamiz_limite, limite_superior, 'g', label = "Límite Superior" )
    plt.scatter(Estructura['Abertura'], Estructura['% pasa'])
    plt.plot(Estructura['Abertura'], Estructura['% pasa'], 'b', label = "Curva Granulométrica" )
    plt.legend()
    plt.grid(color='k', ls = '-.', lw = 0.5)
    plt.grid(True, which="minor", linestyle='-')
    plt.xscale("log")
    plt.gca().invert_xaxis()
    plt.title("Curva granulométrica ",fontsize=14,fontweight="bold")
    plt.xlabel("Tamaño de tamiz (mm)")
    plt.ylabel("% que pasa")
    plt.show()