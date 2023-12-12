import Opencsv
import Graph

def PTorta():
    Country = Opencsv.read_csv('Data.csv')
    Name = []
    WPPorcentaje = []
    print('Si desea elegir una región específica, marque => 1, caso contrario cualquier tecla')
    x = int(input('Elija su opción: '))
    print('')
    
    if x == 1:
        print('Africa:1 // Asia:2 // Europe:3 // North America:4 // Oceania:5 // South America:6')
        y = int(input('Ingrese el número correspondiente a la región deseada: '))
    else:
        y = 0
    
    regiones = {
        1: 'Africa',
        2: 'Asia',
        3: 'Europe',
        4: 'North America',
        5: 'Oceania',
        6: 'South America'
    }

    # Diccionario para almacenar la población total de cada continente
    poblacion_continente = {continente: 0 for continente in regiones.values()}

    # Calcular la población total de cada continente
    for pais in Country:
        continente = pais['Continent']
        poblacion = float(pais['World Population Percentage'])
        if continente in poblacion_continente:
            poblacion_continente[continente] += poblacion

    # Variable para almacenar el porcentaje total de 'Otros' en el continente seleccionado
    otros_porcentaje = 0

    for pais in Country:
        N = pais['Country/Territory']
        poblacion = float(pais['World Population Percentage'])
        continente = pais['Continent']
        
        # Calcular el porcentaje de población del país en su continente
        if continente in poblacion_continente and poblacion_continente[continente] > 0:
            porcentaje_continente = (poblacion / poblacion_continente[continente]) * 100

            # Agrupar países con menos del 2% en 'Otros'
            if porcentaje_continente < 3:
                if y in regiones.keys() and continente == regiones[y]:
                    otros_porcentaje += porcentaje_continente
            elif y in regiones.keys() and continente == regiones[y]:
                Name.append(N)
                WPPorcentaje.append(porcentaje_continente)
            elif y == 0:
                Name.append(N)
                WPPorcentaje.append(porcentaje_continente)
    
    # Agregar 'Otros' si su porcentaje es significativo
    if otros_porcentaje > 0:
        Name.append('Otros')
        WPPorcentaje.append(otros_porcentaje)

    Graph.torta(Name, WPPorcentaje)

if __name__=='__main__':
    PTorta()
