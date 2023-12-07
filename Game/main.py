# Importamos la biblioteca random para generar elecciones aleatorias
import random

# Función para obtener la elección del usuario
def obtener_eleccion_usuario():
    eleccion = input("Elige piedra, papel o tijera: ").lower()
    while eleccion not in ["piedra", "papel", "tijera"]:
        eleccion = input("Entrada inválida. Elige piedra, papel o tijera: ").lower()
    return eleccion

# Función para obtener la elección del computador
def obtener_eleccion_computadora():
    elecciones = ["piedra", "papel", "tijera"]
    return random.choice(elecciones)

# Función para determinar el ganador
def determinar_ganador(usuario, computadora):
    if usuario == computadora:
        return "Empate"
    elif(usuario == "piedra" and computadora == "tijera") or \
        (usuario == "papel" and computadora == "piedra") or \
        (usuario == "tijera" and computadora == "papel"):
        return "Ganaste"
    else:
        return "Perdió"

# Función principal para jugar el juego
def jugar():
    eleccion_usuario = obtener_eleccion_usuario()
    eleccion_computadora = obtener_eleccion_computadora()

    print(f"\nTu elección: {eleccion_usuario}")
    print(f"Elección de la computadora: {eleccion_computadora}")

    resultado = determinar_ganador(eleccion_usuario, eleccion_computadora)
    print(f"Resultado: {resultado}\n")

# Ejecutamos el juego
jugar()
