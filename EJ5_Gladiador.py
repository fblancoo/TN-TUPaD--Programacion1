print("--- BIENVENIDO A LA ARENA ---")

gladiador = ""
while not gladiador.isalpha():
    gladiador = input("Nombre del Gladiador: ")
    if not gladiador.isalpha():
        print("Error: Solo se permiten letras.")

# Variables iniciales
vida_jugador = 100
vida_enemigo = 100
pociones = 3
dano_pesado = 15
dano_enemigo = 12
turno_jugador = True

print("=== INICIO DEL COMBATE ===")

# Ciclo principal
while vida_jugador > 0 and vida_enemigo > 0:
    if turno_jugador:
        print(
            f"\n{gladiador} (HP: {vida_jugador}) vs Enemigo (HP: {vida_enemigo}) | Pociones: {pociones}"
        )
        print("Elige acción:\n1. Ataque Pesado\n2. Ráfaga Veloz\n3. Curar")

        opcion = ""
        while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 3:
            opcion = input("Opción: ")
            if not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 3:
                print("Error: Ingrese un número válido.")
        opcion = int(opcion)

        if opcion == 1:  # Ataque Pesado
            dano_final = float(dano_pesado)
            if vida_enemigo < 20:
                dano_final = float(dano_pesado * 1.5)
                print("¡Golpe Crítico!")

            vida_enemigo -= int(dano_final)
            print(f"¡Atacaste al enemigo por {dano_final} puntos de daño!")

        elif opcion == 2:  # Ráfaga Veloz
            print(">> ¡Inicias una ráfaga de golpes!")
            for _ in range(3):
                vida_enemigo -= 5
                print("> Golpe conectado por 5 de daño")

        elif opcion == 3:  # Curar
            if pociones > 0:
                vida_jugador += 30
                pociones -= 1
                print("¡Te curaste por 30 puntos de vida!")
            else:
                print("¡No quedan pociones!")

        turno_jugador = False  # Cede el turno

    # Turno del Enemigo (automático después de la acción del jugador)
    if not turno_jugador and vida_enemigo > 0:
        vida_jugador -= dano_enemigo
        print(f">> ¡El enemigo contraataca por {dano_enemigo} puntos de daño!")
        turno_jugador = True


print("\n=== FIN DEL JUEGO ===")
if vida_jugador > 0:
    print(f"¡VICTORIA! {gladiador} ha ganado la batalla.")
else:
    print("DERROTA. Has caído en combate.")
