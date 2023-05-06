
# Importar librerias
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def granunlometria( porcentaje_pasa =pd.Series([
        100,  # Ingrese el % pasa del tamiz 1"
        85,   # Ingrese el % pasa del tamiz 3/4"
        80,   # Ingrese el % pasa del tamiz 1/2"
        75,   # Ingrese el % pasa del tamiz 3/8"
        60,   # Ingrese el % pasa del tamiz 1/4"
        45,    # Ingrese el % pasa del tamiz Nº 4"
        40,    # Ingrese el % pasa del tamiz Nº 10"
        20,    # Ingrese el % pasa del tamiz Nº 20"
        10,    # Ingrese el % pasa del tamiz Nº 40"
        13,   # Ingrese el % pasa del tamiz Nº 60"
        16,   # Ingrese el % pasa del tamiz Nº 80"
        15,   # Ingrese el % pasa del tamiz Nº 100"
        11,   # Ingrese el % pasa del tamiz Nº 200"
        14    # Ingrese el % que quedo en la base."
    ])
):
    # Introduzca los porcentajes pasa de los tamices anteriormente especificados para realizar la curva granulométrica
    porcentaje_pasa =pd.Series([
        100,  # Ingrese el % pasa del tamiz 1"
        85,   # Ingrese el % pasa del tamiz 3/4"
        80,   # Ingrese el % pasa del tamiz 1/2"
        75,   # Ingrese el % pasa del tamiz 3/8"
        60,   # Ingrese el % pasa del tamiz 1/4"
        45,    # Ingrese el % pasa del tamiz Nº 4"
        40,    # Ingrese el % pasa del tamiz Nº 10"
        20,    # Ingrese el % pasa del tamiz Nº 20"
        10,    # Ingrese el % pasa del tamiz Nº 40"
        13,   # Ingrese el % pasa del tamiz Nº 60"
        16,   # Ingrese el % pasa del tamiz Nº 80"
        15,   # Ingrese el % pasa del tamiz Nº 100"
        11,   # Ingrese el % pasa del tamiz Nº 200"
        14    # Ingrese el % que quedo en la base."
    ])

    # En la curva granulometrica se grafica como esta gradado el suelo, para esto introduzca los porcentaje pasa de diferentes tamices.
    # Podrá evaluar el suelo en comparación a los limites para la granulometria.

    # Nombre de los tamicez a usar:

    Tamiz = pd.Series([
        '1"',
        '3/4"',
        '1/2"',
        '3/8"',
        '1/4"',
        'Nº 4',
        'Nº 10',
        'Nº 20',
        'Nº 40',
        'Nº 60',
        'Nº 80',
        'Nº 100',
        'Nº 200',
        'Base'
    ])

    # Aberturas de los tamices correspondientes.
    Abertura =pd.Series([
        25.4,  # Medida en mm del tamiz 1"
        19.1,  # Medida en mm del tamiz 3/4"
        12.7,  # Medida en mm del tamiz 1/2"
        9.52,  # Medida en mm del tamiz 3/8"
        6.35,  # Medida en mm del tamiz 1/4"
        4.75,  # Medida en mm del tamiz Nº 4
        1.9,   # Medida en mm del tamiz Nº 10
        0.84,  # Medida en mm del tamiz Nº 20
        0.42,  # Medida en mm del tamiz Nº 40
        0.25,  # Medida en mm del tamiz Nº 60
        0.177, # Medida en mm del tamiz Nº 80
        0.149, # Medida en mm del tamiz Nº 100
        0.074, # Medida en mm del tamiz Nº 200
        0      # Medida de la base de los tamices.
    ])

    Estructura = pd.DataFrame({
        'Tamiz':Tamiz,
        'Abertura' : Abertura,
        '% pasa' : porcentaje_pasa,
    })
    print(Estructura)


    # Con estos datos se grafican los limites superior e inferior de la curva granulométrica.
    tamiz = [37.5,25,19,9.5,4.75,2,0.85,0.425,0.25,0.15 ,0.075] 
    lista_tamiz = pd.Series(tamiz)
    limite_inferior = [100,84.82,55.96,36.92,24.27,16.01,10.67,7.04,4.64,3.06]
    limite_superior = [100,89.6,67.91,51.46,38.90,29.48,22.49,17.05,12.92,9.79]
    tamiz_limite = [25,19,9.5,4.75,2.36,1.18,0.6,0.3,0.15,0.0075]

    plt.grid()
    plt.plot(tamiz_limite, limite_inferior, 'r', label = "Límite Inferior" )
    plt.plot(tamiz_limite, limite_superior, 'g', label = "Límite Superior" )
    plt.scatter(Abertura, porcentaje_pasa)
    plt.plot(Abertura, porcentaje_pasa, 'b', label = "Curva Granulométrica" )
    plt.legend()
    plt.grid(color='k', ls = '-.', lw = 0.5)
    plt.grid(True, which="minor", linestyle='-')
    plt.xscale("log")
    plt.gca().invert_xaxis()
    plt.title("Curva granulométrica ",fontsize=10)
    plt.xlabel("Medida del tamiz (mm)",fontsize=10)
    plt.ylabel("% Pasa",fontsize=10)
    plt.show()
