import random
from colorama import Fore, Style

madera = 2
piedra = 4
hierro = 6
diamante = 8
netherita = 12
vida_maxima_enemigo = 12
vida_maxima_persona = 10
turnos = 0

persona = {
    "vida" : vida_maxima_persona,
    "danio" : 2,
    "xp" : 0,
    "nivel": 0,
    "arma": madera
}
zombie = {"nombre": "zombie", "vida" : vida_maxima_enemigo, "danio" : 2, "aparicion": 0}
esqueleto = {"nombre": "esqueleto", "vida": vida_maxima_enemigo, "danio": 2, "aparicion": 0}
arania = {"nombre": "araña", "vida": vida_maxima_enemigo, "danio": 2, "aparicion": 0}
enderman = {"nombre": "enderman", "vida": vida_maxima_enemigo, "danio": 2, "aparicion": 0}
crepeer = {"nombre": "crepeer", "vida": vida_maxima_enemigo, "danio": 2, "aparicion": 0}
enemigos = [zombie, esqueleto, arania, enderman, crepeer]
eleccion_enemigo = random.randint(0, len(enemigos)-1)

def seleccion_enemigo():
    for i in enemigos:
        if (enemigos.index(i) == eleccion_enemigo):
            enemigo_seleccionado = i["nombre"]
            vida_enemiga = i["vida"]
            danio_enemigo = i["danio"]
            return enemigo_seleccionado, vida_enemiga, danio_enemigo

informacion_enemiga = seleccion_enemigo()
informacion_enemiga = list(informacion_enemiga)

def subir_nivel():
    if (persona["xp"] == 10 and persona["nivel"] == 0):
        persona["arma"] = piedra
        persona["nivel"] += 1
        print(Fore.YELLOW + "Has subido de nivel y se mejoro tu arma. Dejaste de tener un arma de madera a una de piedra"+ Fore.WHITE)
        persona["xp"] = 0
        return True
    elif (persona["xp"] == 20 and persona["nivel"] == 1):
        persona["arma"] = hierro
        persona["nivel"] += 1
        print(Fore.YELLOW + "Has subido de nivel y se mejoro tu arma. Dejaste de tener un arma de piedra a una de hierro"+ Fore.WHITE)
        return True
    elif (persona["xp"] == 30 and persona["nivel"] == 2):
        persona["arma"] = diamante
        persona["nivel"] += 1
        print(Fore.YELLOW + "Has subido de nivel y se mejoro tu arma. Dejaste de tener un arma de hierro a una de " + Fore.CYAN + "diamante"+  Fore.WHITE)
        return True
    elif (persona["xp"] == 40 and persona["nivel"] == 3):
        persona["arma"] = netherita
        persona["nivel"] += 1
        print(Fore.YELLOW + "Has subido de nivel y se mejoro tu arma. Dejaste de tener un arma de diamante a una de " + Fore.MAGENTA + "netherita"+ Fore.WHITE)
        return True
    else: return False

def atacar():
    ataque_jugador = persona["arma"] * persona["danio"]
    informacion_enemiga[1] = informacion_enemiga[1] - ataque_jugador
    print("Has atacado a tu enemigo")
    if (informacion_enemiga[1] <= 0):
        persona["xp"] += 2
        if (subir_nivel() == False):
            print(Fore.YELLOW + "Derrotaste a un enemigo y aumento tu experiencia. Tu expericiencia actual es", persona["xp"], Fore.WHITE)
    return informacion_enemiga[1]

def curarse():
    if (persona["vida"] == vida_maxima_persona):
        return print("Ya tenes la vida completa.")
    seleccion_medicamento = input("Que medicamento queres usar? \n" + Fore.CYAN + "[1] Medicamento chico \n" + Fore.BLUE +"[2] Medicamento mediano \n" + Fore.MAGENTA +"[3] Medicamento grande \n" + Fore.WHITE)
    if (seleccion_medicamento == "1"):
        persona["vida"] += 2
    elif (seleccion_medicamento == "2"):
        persona["vida"] += 4
    elif (seleccion_medicamento == "3"):
        persona["vida"] += 6
    else:
        return print("error")
    return print(Fore.GREEN + "Tu salud ha aumentado." + Fore.WHITE)

def mostrar_vida_persona():
    if (persona["vida"] == 5):
        print("PH PERSONA:", Fore.YELLOW ,persona["vida"], Fore.WHITE)
    elif (persona["vida"] < 5):
        print("PH PERSONA:", Fore.RED ,persona["vida"], Fore.WHITE)
    else: print("PH PERSONA:", persona["vida"], Fore.WHITE)

def ataque_enemigo_principal():
    persona["vida"] = persona["vida"] - informacion_enemiga[2]
    print("Tu enemigo te ha hecho un ataque basico.")
    if (persona["vida"] <= 0):
        return print("Has perdido :(")

def ataque_enemigo_secundario():
    ataque_fuerte_enemigo = informacion_enemiga[2] * 2
    persona["vida"] = persona["vida"] - ataque_fuerte_enemigo
    print("Tu enemigo te ha hecho un ataque potenciado.")
    if (persona["vida"] <= 0):
        return print("Has perdido :(")
    
def curarse_enemigo():
    if (informacion_enemiga[1] > 7):
        return print("Tu enemigo intento curarse, pero ha fallado.")
    else: informacion_enemiga[1] += 5
    return print(Fore.GREEN + "La salud de tu enemigo aumento en 5 puntos." + Fore.WHITE)

def mostrar_vida_enemigo():
    if (informacion_enemiga[1] == 6):
        print("PH "+ informacion_enemiga[0].upper() +":", Fore.YELLOW ,informacion_enemiga[1], Fore.WHITE)
    elif (informacion_enemiga[1] < 6):
        print("PH "+ informacion_enemiga[0].upper() +":", Fore.RED ,informacion_enemiga[1], Fore.WHITE)
    else: print("PH "+ informacion_enemiga[0].upper() +":", informacion_enemiga[1])

def turno_enemigo():
    ataque_enemigo = random.randint(1,3)
    if (ataque_enemigo == 1):
        ataque_enemigo_principal()
    elif (ataque_enemigo == 2):
        ataque_enemigo_secundario()
    elif (ataque_enemigo == 3):
        curarse_enemigo()
        



print(Style.BRIGHT + Fore.BLUE + "Minecraft RPG" + Fore.WHITE + Style.NORMAL)
encuentro = input("Queres encontrarte con un enemigo? \n" "Si \n" "No \n")
while encuentro.lower() == "si":
    if (turnos == 0):
        if (informacion_enemiga[0] == "araña"):
            print("Te encontraste con una " + str(informacion_enemiga[0]) + " atacala antes de que te derrote")
        else:print("Te encontraste con un " + str(informacion_enemiga[0]) + " atacalo antes de que te derrote")
        mostrar_vida_enemigo()
        mostrar_vida_persona()
    print("Turno", turnos)
    respuesta = input("[1] Atacar \n" "[2] Curarse \n" "[3] Huir \n" "[4] Cerrar el juego \n")
    if (respuesta == "1"):
        atacar()
        if (informacion_enemiga[1] <= 0):
            for i in enemigos:
                if (i["nombre"] == informacion_enemiga[0]):
                    i["aparicion"] += 1
                    if (i["aparicion"] % 3 == 0):
                        print(Fore.RED + "Cuidado, este enemigo a aumentado su vida" + Fore.WHITE)
                        vida_maxima_enemigo += 3
            encuentro = input("Queres encontrarte con un enemigo? \n" "Si \nNo \n")
            if (encuentro.lower() == "no"):
                break;
            elif (encuentro.lower() == "si"):
                eleccion_enemigo = random.randint(0, len(enemigos)-1)
                informacion_enemiga = seleccion_enemigo()
                informacion_enemiga = list(informacion_enemiga)
                turnos = 0
                persona["vida"] = vida_maxima_persona
                continue;
            elif (persona["vida"] <= 0):
                break;
        turno_enemigo()
        if (persona["vida"] <= 0):
            break;
    elif (respuesta == "2"):
        curarse()
        turno_enemigo()
        if (informacion_enemiga[1] <= 0 or persona["vida"] <= 0):
            break;
    elif (respuesta == "3"):
        print("Escapaste")
        continue;
    elif (respuesta == "4"):
        cerrar_juego = input("Si queres salir del juego escribi si, perderas el progreso que tengas hasta el momento.\nSi \nNo\n")
        if (cerrar_juego == "si"):
            break;
        elif (cerrar_juego == "no"):
            encuentro = input("Queres encontrarte con un enemigo? \n" "Si \n" "No \n")
            if (encuentro.lower() == "no"):
                break;
    mostrar_vida_enemigo()
    mostrar_vida_persona()
    print("==========")
    turnos += 1

# Hacer:
# Sistema de xp: cuando el personaje llegue a x cantidad de xp aumenten su vida.