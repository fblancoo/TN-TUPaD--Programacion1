# Variables iniciales (no se piden por teclado)
energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
consecutivos_forzar = 0

agente = ""
while not agente.isalpha():
    agente = input("Nombre del agente: ")

# El juego continúa mientras haya energía y tiempo, no se hayan abierto todas,
# y no esté bloqueado por la alarma (alarma activa y tiempo <= 3).
while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3:
    # Regla de bloqueo por alarma
    if alarma and tiempo <= 3 and cerraduras_abiertas < 3:
        break

    print(f"\n--- ESTADO DEL AGENTE {agente.upper()} ---")
    print(
        f"Energía: {energia} | Tiempo: {tiempo} | Cerraduras: {cerraduras_abiertas}/3 | Alarma: {'ON' if alarma else 'OFF'}"
    )
    print("1. Forzar cerradura")
    print("2. Hackear panel")
    print("3. Descansar")

    opcion = ""
    while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 3:
        opcion = input("Elige acción (1-3): ")
    opcion = int(opcion)

    if opcion == 1:  # Forzar cerradura
        consecutivos_forzar += 1
        energia -= 20
        tiempo -= 2

        # Regla anti-spam: 3 veces seguidas
        if consecutivos_forzar == 3:
            alarma = True
            print(
                "¡Forzaste demasiadas veces seguidas! La cerradura se trabó y la alarma se activó."
            )
        else:
            if energia < 40:
                riesgo = ""
                while not riesgo.isdigit() or int(riesgo) < 1 or int(riesgo) > 3:
                    riesgo = input("¡Riesgo de alarma! Ingresa un número del 1 al 3: ")
                if int(riesgo) == 3:
                    alarma = True
                    print("¡Mala suerte, se activó la alarma!")

            if not alarma:
                cerraduras_abiertas += 1
                print("¡Cerradura forzada con éxito!")
            else:
                print("No puedes abrir la cerradura mientras la alarma está activa.")

    elif opcion == 2:  # Hackear panel
        consecutivos_forzar = 0  # Rompe la racha
        energia -= 10
        tiempo -= 3
        print("Hackeando el sistema...")

        # Bucle for para progreso
        for i in range(4):
            codigo_parcial += "A"
            print(f"Progreso: {codigo_parcial}")

        if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
            cerraduras_abiertas += 1
            codigo_parcial = ""  # Se reinicia para poder abrir otra si es necesario
            print(
                "¡Código completado! Se abrió una cerradura de la bóveda automáticamente."
            )

    elif opcion == 3:  # Descansar
        consecutivos_forzar = 0  # Rompe la racha
        tiempo -= 1
        energia += 15
        if energia > 100:
            energia = 100

        if alarma:
            energia -= 10  # Costo extra por alarma
            print("Descansaste, pero la alarma te aturde (-10 energía extra).")
        else:
            print("Descansaste y recuperaste energía.")

# Evaluaciones de Fin de Juego
print("\n=== FIN DEL JUEGO ===")
if cerraduras_abiertas == 3:
    print("¡VICTORIA! Lograste abrir la bóveda a tiempo.")
elif alarma and tiempo <= 3 and cerraduras_abiertas < 3:
    print(
        "DERROTA (Bloqueo). El sistema de la bóveda se bloqueó definitivamente por la alarma."
    )
else:
    print("DERROTA. Te quedaste sin energía o sin tiempo para continuar.")
