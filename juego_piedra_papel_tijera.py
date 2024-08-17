nombre1 = input("Nombre del jugador 1: ")
nombre2 = input("Nombre del jugador 2: ")

jugador1 = input(f'{nombre1}, ¿Qué eliges? ¿piedra, papel o tijera?: ').lower()
jugador2 = input(f'{nombre2}, ¿Qué eliges? ¿piedra, papel o tijera?: ').lower()

condicion1 = jugador1 == "piedra" and jugador2 == "tijera"
condicion2 = jugador1 == "tijera" and jugador2 == "papel"
condicion3 = jugador1 == "papel" and jugador2 == "piedra"

if jugador1 == jugador2:
    print("Empate")
elif condicion1 or condicion2 or condicion3:
    print("Ha ganado:", nombre1, "!")
else: 
    print("Ha ganado:", nombre2, "!")