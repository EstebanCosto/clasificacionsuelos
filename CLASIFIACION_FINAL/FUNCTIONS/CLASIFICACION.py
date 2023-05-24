from FUNCTIONS.CARTAPLASTICIDAD import CartaPlasticidad
from FUNCTIONS.VAL_ENTRADA import *
#Importar las bibliotecas  
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# D10, D30 y D60
d10 = np.percentile(porcentaje_pasa, 10)
d30 = np.percentile(porcentaje_pasa, 30)
d60 = np.percentile(porcentaje_pasa, 60)

# Tamíz N° 4 y N° 200
Tamiz_200 = porcentaje_pasa[12]
Tamiz_4 = porcentaje_pasa[5]

def clasificacion_suelo():

    Limite_liquido1 = Limiteliquido[0]
    Indice_plasticidad1 = Indiceplasticidad[0]

    Cu = (d60/d10)
    Cc = ((d30**2)/(d60*d10))

    if Tamiz_200 < 50:

      if Tamiz_4 < 50:
        
        if Tamiz_200 < 5:

          if Cu >= 4 and 1 <= Cc <= 3: #Parámetros para un tipo de suelo GW  - Grava bien gradada
            print("La clasificación del suelo es: GW - Grava bien gradada")

          elif Cu < 4 and 1 > Cc > 3: #Parámetros para un tipo de suelo GP - Grava mal gradada
            print("La clasificación del suelo es: GP - Grava mal gradada")

        elif Tamiz_200 > 12:

          if Indice_plasticidad1[0] < 4: #Parámetro para un tipo de suelo GM - Grava limoso
            print("La clasificación del suelo es: GM - Grava limoso")

          elif Indice_plasticidad1[0] > 7: #Parámetro para un tipo de suelo GC- Grava arcillosa
            print("La clasificación del suelo es: GC- Grava arcillosa")

        else:

          if (Cu >= 4 and 1 <= Cc <= 3) and (Indice_plasticidad1[0] < 4): #Parámetros para un tipo de suelo GW-GM - Grava bien gradada con limo
            CartaPlasticidad(Limite_liquido1,Indice_plasticidad1)
            print("La clasificación del suelo es: GW-GM - Grava bien gradada con limo")

          elif (Cu >= 4 and 1 <= Cc <= 3) and (Indice_plasticidad1[0] > 7): #Parámetros para un tipo de suelo GW-GC - Grava bien gradada con arcilla
            CartaPlasticidad(Limite_liquido1,Indice_plasticidad1)
            print("La clasificación del suelo es: GW-GC - Grava bien gradada con arcilla")

          elif (Cu < 4 and 1 > Cc > 3) and (Indice_plasticidad1[0] < 4): #Parámetros para un tipo de suelo GP-GM - Grava mal gradada con limo
            CartaPlasticidad(Limite_liquido1,Indice_plasticidad1)
            print("La clasificación del suelo es: GP-GM - Grava mal gradada con limo")

          else: #Parámetros para un tipo de suelo GP-GC - Grava mal gradada con arcilla
            print("La clasificación del suelo es: GP-GC - Grava mal gradada con arcilla")

      elif Tamiz_4 >= 50:

        if Tamiz_200 < 5:

          if Cu >= 6 and 1 <= Cc <= 3: #Parámetros para un tipo de suelo SW - Arena bien gradada
            print("La clasificación del suelo es: SW - Arena bien gradada")

          elif Cu < 6 and 1 > Cc > 3: #Parámetros para un tipo de suelo SP - Arena mal gradada
            print("La clasificación del suelo es: SP - Arena mal gradada")

        elif Tamiz_200 > 12:

          if Indice_plasticidad1[0] < 4: #Parámetro para un tipo de suelo SM - Arena limoso
            CartaPlasticidad(Limite_liquido1,Indice_plasticidad1)
            print("La clasificación del suelo es: SM - Arena limoso")

          elif Indice_plasticidad1[0] > 7: #Parámetro para un tipo de suelo SC- Arena arcillosa
            CartaPlasticidad()
            print("La clasificación del suelo es: SC- Arena arcillosa")

        else:

          if (Cu >= 4 and 1 <= Cc <= 3) and (Indice_plasticidad1[0] < 4): #Parámetros para un tipo de suelo SW-SM - Arena bien gradada con limo
            CartaPlasticidad(Limite_liquido1,Indice_plasticidad1)
            print("La clasificación del suelo es: SW-SM - Arena bien gradada con limo")

          elif (Cu >= 4 and 1 <= Cc <= 3) and (Indice_plasticidad1[0] > 7): #Parámetros para un tipo de suelo SW-SC - Arena bien gradada con arcilla
            CartaPlasticidad(Limite_liquido1,Indice_plasticidad1)
            print("La clasificación del suelo es: SW-SC - Arena bien gradada con arcilla")

          elif (Cu < 4 and 1 > Cc > 3) and (Indice_plasticidad1[0] < 4): #Parámetros para un tipo de suelo SP-SM - Arena mal gradada con limo
            CartaPlasticidad(Limite_liquido1,Indice_plasticidad1)
            print("La clasificación del suelo es: SP-SM - Arena mal gradada con limo")

          else: #Parámetros para un tipo de suelo SP-SC - Arena mal gradada con arcilla
            CartaPlasticidad(Limite_liquido1,Indice_plasticidad1)
            print("La clasificación del suelo es: SP-SC - Arena mal gradada con arcilla")  
        
      
    elif Tamiz_200 > 50:

      if Limite_liquido1 < 50:

        if Indice_plasticidad1 > 7: #Parámetro para un tipo de suelo CL - Arcilla de baja platicidad
            CartaPlasticidad(Limite_liquido1,Indice_plasticidad1)
            print("La clasificación del suelo es: CL - Arcilla de baja platicidad")

        elif Indice_plasticidad1 < 4: #Parámetro para un tipo de suelo ML - Limo de baja platicidad
          CartaPlasticidad(Limite_liquido1,Indice_plasticidad1)
          print("La clasificación del suelo es: ML - Limo de baja platicidad")

      elif Limite_liquido1 >= 50:

        if Indice_plasticidad1 > 7: #Parámetro para un tipo de suelo CH - Arcilla de alta platicidad
          CartaPlasticidad(Limite_liquido1,Indice_plasticidad1)
          print("La clasificación del suelo es: CH - Arcilla de alta platicidad")

        elif Indice_plasticidad1[0] < 4: #Parámetro para un tipo de suelo MH - Limo de alta platicidad
          CartaPlasticidad(Limite_liquido1,Indice_plasticidad1)
          print("La clasificación del suelo es: MH - Limo de alta platicidad") 