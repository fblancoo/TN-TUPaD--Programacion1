usuario_correcto = "alumno"
clave_correcta = "python123"
intentos = 0
acceso = False

# Ciclo con máximo de 3 intentos
while intentos < 3:
    usuario = input(f"Intento {intentos + 1}/3 - Usuario: ")
    clave = input("Clave: ")

    if usuario == usuario_correcto and clave == clave_correcta:
        acceso = True
        print("Acceso concedido.")
        break
    else:
        intentos += 1
        print("Error: credenciales inválidas.")

if not acceso:
    print("Cuenta bloqueada.")
else:
    # Menú repetitivo
    while True:
        print("\n1) Estado  2) Cambiar clave  3) Mensaje  4) Salir")
        opcion = input("Opción: ")

        # Validación estricta con isdigit
        if not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 4:
            print("Error: ingrese un número válido entre 1 y 4.")
            continue

        opcion = int(opcion)

        if opcion == 1:
            print("Estado: Inscripto")
        elif opcion == 2:
            nueva_clave = input("Nueva clave: ")
            if len(nueva_clave) >= 6:
                confirmacion = input("Confirme nueva clave: ")
                if nueva_clave == confirmacion:
                    clave_correcta = nueva_clave
                    print("Clave cambiada exitosamente.")
                else:
                    print("Error: las claves no coinciden.")
            else:
                print("Error: mínimo 6 caracteres.")
        elif opcion == 3:
            print("¡La práctica constante es la clave para dominar la programación!")
        elif opcion == 4:
            print("Saliendo del sistema...")
            break
