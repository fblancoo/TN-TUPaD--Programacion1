lunes1 = lunes2 = lunes3 = lunes4 = ""
martes1 = martes2 = martes3 = ""

operador = ""
while not operador.isalpha():
    operador = input("Nombre del operador: ")

while True:
    print(
        "\n1. Reservar turno\n2. Cancelar turno\n3. Ver agenda del día\n4. Ver resumen general\n5. Cerrar sistema"
    )
    opcion = input("Opción: ")

    if not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 5:
        print("Opción inválida. Ingrese un número del 1 al 5.")
        continue
    opcion = int(opcion)

    if opcion == 5:
        print("Cerrando sistema...")
        break

    elif opcion == 1:  # Reservar turno
        dia = input("Día (1=Lunes, 2=Martes): ")
        if dia not in ["1", "2"]:
            print("Día incorrecto.")
            continue

        paciente = ""
        while not paciente.isalpha():
            paciente = input("Nombre del paciente: ")

        if dia == "1":
            # Verificar repetidos
            if paciente in [lunes1, lunes2, lunes3, lunes4] and paciente != "":
                print("Error: Paciente ya registrado el Lunes.")
            # Asignar primer turno vacío
            elif lunes1 == "":
                lunes1 = paciente
            elif lunes2 == "":
                lunes2 = paciente
            elif lunes3 == "":
                lunes3 = paciente
            elif lunes4 == "":
                lunes4 = paciente
            else:
                print("No hay cupos libres para el Lunes.")
        elif dia == "2":
            if paciente in [martes1, martes2, martes3] and paciente != "":
                print("Error: Paciente ya registrado el Martes.")
            elif martes1 == "":
                martes1 = paciente
            elif martes2 == "":
                martes2 = paciente
            elif martes3 == "":
                martes3 = paciente
            else:
                print("No hay cupos libres para el Martes.")

    elif opcion == 2:  # Cancelar turno
        dia = input("Día (1=Lunes, 2=Martes): ")
        paciente = input("Nombre del paciente a cancelar: ")

        if dia == "1":
            if lunes1 == paciente:
                lunes1 = ""
            elif lunes2 == paciente:
                lunes2 = ""
            elif lunes3 == paciente:
                lunes3 = ""
            elif lunes4 == paciente:
                lunes4 = ""
            else:
                print("Paciente no encontrado.")
        elif dia == "2":
            if martes1 == paciente:
                martes1 = ""
            elif martes2 == paciente:
                martes2 = ""
            elif martes3 == paciente:
                martes3 = ""
            else:
                print("Paciente no encontrado.")

    elif opcion == 3:  # Ver agenda del día
        dia = input("Día (1=Lunes, 2=Martes): ")
        if dia == "1":
            print(f"Turno 1: {lunes1 if lunes1 != '' else '(libre)'}")
            print(f"Turno 2: {lunes2 if lunes2 != '' else '(libre)'}")
            print(f"Turno 3: {lunes3 if lunes3 != '' else '(libre)'}")
            print(f"Turno 4: {lunes4 if lunes4 != '' else '(libre)'}")
        elif dia == "2":
            print(f"Turno 1: {martes1 if martes1 != '' else '(libre)'}")
            print(f"Turno 2: {martes2 if martes2 != '' else '(libre)'}")
            print(f"Turno 3: {martes3 if martes3 != '' else '(libre)'}")

    elif opcion == 4:  # Resumen general
        ocupados_lunes = (
            (lunes1 != "") + (lunes2 != "") + (lunes3 != "") + (lunes4 != "")
        )
        ocupados_martes = (martes1 != "") + (martes2 != "") + (martes3 != "")

        print(f"Lunes: {ocupados_lunes} ocupados, {4 - ocupados_lunes} disponibles.")
        print(f"Martes: {ocupados_martes} ocupados, {3 - ocupados_martes} disponibles.")

        if ocupados_lunes > ocupados_martes:
            print("El día con más turnos es el Lunes.")
        elif ocupados_martes > ocupados_lunes:
            print("El día con más turnos es el Martes.")
        else:
            print("Ambos días tienen la misma cantidad de turnos.")
