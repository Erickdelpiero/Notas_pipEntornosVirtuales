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

    for pais in Country:
        N = pais['Country/Territory']
        WPP = float(pais['World Population Percentage'])
        continente = pais['Continent']
        
        if y in regiones.keys() and continente == regiones[y]:
            Name.append(N)
            WPPorcentaje.append(WPP)
        elif y == 0:
            Name.append(N)
            WPPorcentaje.append(WPP)
    
    Graph.torta(Name, WPPorcentaje)
    # print(pais)


if __name__=='__main__':
    PTorta()