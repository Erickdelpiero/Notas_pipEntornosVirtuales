import Opencsv
import Graph

def PBarras():
  
  Name=input('Ingrese nombre del país a graficar: ')
  
  Country= Opencsv.read_csv('Data.csv')
  Pais=next((pais for pais in Country if pais['Country/Territory']==Name), None)
  
  # Claves que deseas incluir en el nuevo diccionario
  year = {'2022 Population': '2022', '2020 Population': '2020', 
          '2015 Population': '2015', '2010 Population': '2010', 
          '2000 Population': '2000', '1990 Population': '1990', 
          '1980 Population': '1980', '1970 Population': '1970'}
  
  # Generar un nuevo diccionario con solo las claves deseadas
  Years = {year[clave]: Pais[clave] for clave in year}
  labels=list(Years.keys())
  value=list(Years.values())
  values= [int(num_str) for num_str in value]
  
  Graph.barras(labels, values)

if __name__=='__main__':
  PBarras()