def entretener_sobrino():
    while True:
        edad = int(input("¿Cuál es la edad de tu sobrino? "))

        if edad >= 0 and edad <= 2:
            actividad = "Jugar con juguetes suaves"
        elif edad >= 3 and edad <= 5:
            actividad = "Jugar con bloques"
        elif edad >= 6 and edad <= 12:
            actividad = "Jugar juegos de mesa"
        else:
            print("Edad no válida. Intenta de nuevo.")
            continue

        interes = input("¿Qué le gusta a tu sobrino? (música, arte, tecnología) ")

        if interes == "música":
            actividad += ", tocar instrumentos"
        elif interes == "arte":
            actividad += ", hacer manualidades"
        elif interes == "tecnología":
            actividad += ", jugar videojuegos"
        else:
            print("Interés no válido. Intenta de nuevo.")
            continue

        opcion = int(input("¿Qué actividad prefieres? (1) " + actividad + ", (2) Ir al parque "))

        if opcion == 1:
            print("Vamos a " + actividad)
        elif opcion == 2:
            print("Vamos al parque")
        else:
            print("Opción no válida. Intenta de nuevo.")
            continue

        # Usando el bucle for para gestionar la opción de continuar
        for _ in range(1):
            respuesta = input("¿Quieres seguir? (sí/no) ")
            if respuesta.lower() == "no":
                print("¡Hasta la próxima!")
                return  # Termina la función y el bucle
            elif respuesta.lower() == "sí":
                break
            else:
                print("Respuesta no válida. Debes responder 'sí' o 'no'.")
                continue

entretener_sobrino()