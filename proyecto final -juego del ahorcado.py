

import random

# ---------- ESTRUCTURAS DE DATOS ----------

palabras = {
    "facil": ["sol", "luna", "casa", "gato", "perro"],
    "medio": ["python", "datos", "listas", "bucles"],
    "dificil": ["programacion", "estructura", "funciones"]
}

estado_juego = {
    "palabra_secreta": "",
    "letras_adivinadas": [],
    "intentos": 0
}

# ---------- FUNCIONES ----------

def mostrar_menu():
    print("\n🎮 MENÚ PRINCIPAL")
    print("1. Jugar")
    print("2. Salir")

def seleccionar_nivel():
    print("\n📊 SELECCIONE NIVEL")
    print("1. Fácil")
    print("2. Medio")
    print("3. Difícil")

    opcion = input("Opción: ")

    if opcion == "1":
        return "facil", 8
    elif opcion == "2":
        return "medio", 6
    elif opcion == "3":
        return "dificil", 4
    else:
        print("❌ Opción inválida")
        return None, None

def seleccionar_palabra(nivel):
    return random.choice(palabras[nivel])

def mostrar_progreso(palabra, letras):
    progreso = ""
    for letra in palabra:
        if letra in letras:
            progreso += letra
        else:
            progreso += "_"
    return progreso

def pedir_letra():
    letra = input("Ingrese una letra: ").lower()

    if len(letra) != 1:
        print("❌ Debe ingresar solo una letra")
        return None
    if not letra.isalpha():
        print("❌ Solo se permiten letras")
        return None

    return letra

def actualizar_estado(letra, estado):
    if letra in estado["letras_adivinadas"]:
        print("⚠ Ya ingresaste esa letra")
        return

    estado["letras_adivinadas"].append(letra)

    if letra not in estado["palabra_secreta"]:
        estado["intentos"] -= 1
        print("❌ Letra incorrecta")
    else:
        print("✅ Letra correcta")

def verificar_ganador(palabra_mostrada):
    return "_" not in palabra_mostrada

# ---------- JUEGO ----------

def jugar_ahorcado():
    print("🎮 BIENVENIDO AL JUEGO DEL AHORCADO")

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "2":
            print("👋 Gracias por jugar")
            break

        elif opcion == "1":
            nivel, intentos = seleccionar_nivel()
            if nivel is None:
                continue

            estado_juego["palabra_secreta"] = seleccionar_palabra(nivel)
            estado_juego["letras_adivinadas"] = []
            estado_juego["intentos"] = intentos

            # Ciclo del juego
            while estado_juego["intentos"] > 0:
                palabra_mostrada = mostrar_progreso(
                    estado_juego["palabra_secreta"],
                    estado_juego["letras_adivinadas"]
                )

                print("\nPalabra:", palabra_mostrada)
                print("Intentos restantes:", estado_juego["intentos"])
                print("Letras usadas:", estado_juego["letras_adivinadas"])

                if verificar_ganador(palabra_mostrada):
                    print("🎉 ¡FELICIDADES! HAS GANADO")
                    break

                letra = pedir_letra()
                if letra is None:
                    continue

                actualizar_estado(letra, estado_juego)

            else:
                print("💀 HAS PERDIDO")
                print("La palabra era:", estado_juego["palabra_secreta"])

# ---------- EJECUCIÓN ----------
jugar_ahorcado()
