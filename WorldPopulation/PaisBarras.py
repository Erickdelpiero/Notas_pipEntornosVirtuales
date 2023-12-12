import Opencsv
import Graph

def PBarras():
  
  # Solicita el nombre del país al usuario y lo normaliza
  # para que coincida con la capitalización de los datos
  Name = input('Ingrese nombre del país a graficar: ').capitalize()
  
  # Lee los datos del archivo CSV
  Country = Opencsv.read_csv('Data.csv')
  
  # Encuentra el país solicitado en los datos
  Pais = next((pais for pais in Country if pais['Country/Territory'] == Name), None)
  
  # Claves que deseas incluir en el nuevo diccionario
  year = {'2022 Population': '2022', '2020 Population': '2020', 
          '2015 Population': '2015', '2010 Population': '2010', 
          '2000 Population': '2000', '1990 Population': '1990', 
          '1980 Population': '1980', '1970 Population': '1970'}
  
  # Generar un nuevo diccionario con solo las claves deseadas
  # y convierte los valores de la población a enteros
  Years = {year[clave]: int(Pais[clave].replace(',', '')) for clave in year if clave in Pais}
  
  # Ordena los años de manera ascendente
  ordered_Years = dict(sorted(Years.items()))

  # Obtiene las etiquetas y valores para el gráfico
  labels = list(ordered_Years.keys())
  values = list(ordered_Years.values())
  
  # Crea el gráfico de barras con las etiquetas y valores,
  # establece el nombre del país como título y cambia el formato del eje Y a 'Millions'
  Graph.barras(labels, values, title=Name, ylabel='Población (Millones)')

if __name__=='__main__':
  PBarras()
