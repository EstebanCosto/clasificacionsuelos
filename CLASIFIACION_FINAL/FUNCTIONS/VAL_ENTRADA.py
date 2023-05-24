import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# Datos de entrada para la curva granulométrica
# Insertar los valores indicados en los numerales para procentaje pasa
porcentaje_pasa=[
# Tamiz 1"
 10,
# Tamiz 3/4"
 9,
# Tamiz 1/2"
 9,
# Tamiz 3/8"
 8,
# Tamiz 1/4"
 8,
# Tamiz N° 4
 6,
# Tamiz N° 10
 5,
# Tamiz N° 20
 2,
# Tamiz N° 40
 1,
# Tamiz N° 60
 3,
# Tamiz N° 80
 1,
# Tamiz N° 100
 2,
# Tamiz N° 200
 100,
# Base
 100]
# NO MODIFICAR (Abertura del tamiz)
aberturas_tamices=[25.4,19.1,12.7,9.52,6.35,4.75,1.9,0.84,0.42,0.25,0.177,0.149,0.074,0]
# NO MODIFICAR (Nombre del tamiz)
nombres_tamices=['1"','3/4"','1/2"','3/8"','"1/4','Nº 4','Nº 10','Nº 20','Nº 40','Nº 60','Nº 80','Nº 100','Nº 200','Base']


# Datos Límite líquido e Índice de plasticidad
Limiteliquido = [80]
Indiceplasticidad = [10]
Cartaplasticidad = [80,10]
clasificacion_suelo = [80,10]
