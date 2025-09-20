import time

Mayu = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
Mini = "abcdefghijklmnopqrstuvwxyz"
Numeros = "0123456789"
cespeciales = "!#$%&/()=?¡¿+[];:.,"

alphabet = Mayu + Mini + Numeros + cespeciales

contra = input("Digite la contraseña de máximo 3 digitos: ")

while True:
    if len(contra) <= 3:
        break
    else:
        contra = input("Error, digite la contraseña de máximo 3 digitos: ")

inicio = time.time()

def fuerza_bruta():
    contador = 0

    if len(contra) == 1:
        for i in alphabet:
            if i == contra:
                fin = time.time()
                duracion = fin - inicio
                return ("Contraseña Encontrada...\n"
                        "Número de intentos: " + str(contador) + "\n"
                        "Tiempo Empleado: " + str(round(duracion, 2)) + " segundos")
            else:
                contador += 1

    elif len(contra) == 2:
        for i in alphabet:
            for j in alphabet:
                intento = i + j
                if intento == contra:
                    fin = time.time()
                    duracion = fin - inicio
                    return ("Contraseña Encontrada...\n"
                            "Número de intentos: " + str(contador) + "\n"
                            "Tiempo Empleado: " + str(round(duracion, 2)) + " segundos")
                else:
                    contador += 1

    elif len(contra) == 3:
        for i in alphabet:
            for j in alphabet:
                for k in alphabet:
                    intento = i + j + k
                    if intento == contra:
                        fin = time.time()
                        duracion = fin - inicio
                        return ("Contraseña Encontrada...\n"
                                "Número de intentos: " + str(contador) + "\n"
                                "Tiempo Empleado: " + str(round(duracion, 2)) + " segundos")
                    else:
                        contador += 1


print(fuerza_bruta())