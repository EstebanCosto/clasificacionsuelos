# invocar las funciones
from functions.granulometria import curva_granulometrica
from functions.clasificacion import clasificacion_suelo

curva_granulometrica()
clasificacion_suelo(
# % Pasa Tamiz N°200
15,
# % Pasa Tamiz N°4
60,
# D10
40,
# D30
50,
# D60
60,
# Indice de plasticidad
40,
# Límite líquido
60)