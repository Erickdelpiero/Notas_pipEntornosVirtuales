# Erick Del Piero (https://github.com/Erickdelpiero)
# 20/07/2023

# Programa para visualizar gráficas estadíticas de la población mundial
import PaisBarras
import PaisTorta

print('Análisis de 1 país => 1  // Análisis de toda la población => 2')
a=int(input('Elija opción: '))
print('')

if a==1:
  PaisBarras.PBarras()
  
elif a==2:
  PaisTorta.PTorta()

else:
  print('Opción no válida, elija entre 1 y 2')