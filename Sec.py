#Imports
import random

#Clases123
class foreground:
        DEFAULT = '\033[37m'
        RED = '\033[31m'
        GREEN = '\033[32m'
        ORANGE = '\033[33m'
        BLUE = '\033[34m'
        PURPLE = '\033[35m'
        CYAN = '\033[36m'
        LIGHT_RED = '\033[91m'
        LIGHT_GREEN = '\033[92m'
        YELLOW = '\033[93m'
        LIGHT_BLUE = '\033[94m'
        PINK = '\033[95m'
        LIGHT_CYAN = '\033[96m'

#Funciones

#Función 1.
def crear_identif(mod):   
    iden = mod
    global adn
    adn = ["A", "T", "G", "C"]
    l_iden = list(iden)
    while iden == mod:
        for i in range(random.randint(1,3)):
            l_iden[random.randint(0, len(l_iden) - 1)] = adn[random.randint(0,3)]
        iden = "".join(l_iden)
    return iden

#Función 2.
def crear_muestra(iden):
    muestra = iden
    l_muestra = list(muestra)
    global pos
    pos = []
    while len(pos) < 5:
        for i in range(random.randint(5 - len(pos), 10 - len(pos))):
            aux_muestra = l_muestra.copy()
            cont = 0
            a = random.randint(0, len(l_muestra) - 1)
            for i in range(len(pos)):
                if pos[i] != a: 
                    cont += 1
            if cont != len(pos):
                continue
            l_muestra[a] = adn[random.randint(0,3)]
            for i in range(len(l_muestra)):
                if l_muestra[i] != aux_muestra[i]:
                    pos.append(i)
                    break
        if len(pos) == len(l_muestra):
            break
    muestra = "".join(l_muestra)    
    return muestra

#Función 3.
def recrear_identif(ident):
    nuevo_ident = ""
    a_cont = 0
    t_cont = 0
    g_cont = 0
    c_cont = 0
    matriz_muestra = []
    sumas = []
    for i in range(20):
        matriz_muestra.append(crear_muestra(ident))
    if len(pos) == len(ident):
        if len(pos) == 1:
            print("El tamaño de la cadena es menor a 5.",
            "\nSe realizó " + str(len(pos)) + " cambio.") 
        else:
            print("El tamaño de la cadena es menor a 5.",
            "\nSe realizaron " + str(len(pos)) + " cambios.") 
    for i in range(len(ident)):
        for j in range(len(matriz_muestra)):
            if matriz_muestra[j][i] == adn[0]:
                a_cont += 1
            elif matriz_muestra[j][i] == adn[1]:
                t_cont += 1
            elif matriz_muestra[j][i] == adn[2]:
                g_cont += 1
            elif matriz_muestra[j][i] == adn[3]:
                c_cont += 1
        sumas.append(a_cont)
        sumas.append(t_cont)
        sumas.append(g_cont)
        sumas.append(c_cont)
        for k in range(len(sumas)):
            if max(sumas) == sumas[k]:
                nuevo_ident += adn[k]
                break
        sumas.clear()
        a_cont = 0
        t_cont = 0
        g_cont = 0
        c_cont = 0
    print("\nIdentificador recreado:", nuevo_ident)

#Función 4.
def recrear_identif_mod(ident, mod):
    nuevo_ident = ""
    a_cont = 0
    t_cont = 0
    g_cont = 0
    c_cont = 0
    matriz_muestra = []
    sumas = []
    l_maxnuc = []
    for i in range(20):
        matriz_muestra.append(crear_muestra(ident)) 
    for i in range(len(ident)):
        for j in range(len(matriz_muestra)):
            if matriz_muestra[j][i] == adn[0]:
                a_cont += 1
            elif matriz_muestra[j][i] == adn[1]:
                t_cont += 1
            elif matriz_muestra[j][i] == adn[2]:
                g_cont += 1
            elif matriz_muestra[j][i] == adn[3]:
                c_cont += 1
        sumas.append(a_cont)
        sumas.append(t_cont)
        sumas.append(g_cont)
        sumas.append(c_cont)
        for k in range(len(sumas)):
            if max(sumas) == sumas[k]:
                l_maxnuc.append(adn[k])
        for l in range(len(l_maxnuc)):
            if l_maxnuc[l] == mod[i]:
                nuevo_ident += l_maxnuc[l]
                break
        if i == len(nuevo_ident):
            nuevo_ident += l_maxnuc[random.randint(0, len(l_maxnuc) - 1)]
        l_maxnuc.clear()
        sumas.clear()
        a_cont = 0
        t_cont = 0
        g_cont = 0
        c_cont = 0
    print("\nIdentificador recreado:", nuevo_ident,
    "\n(modelo utilizado como referencia)\n")

#Función 6.
def imprimir_pares(mod):
    pares = ""
    for i in range(len(mod)):
        if mod[i] == adn[0]:
            pares += adn[1]
        elif mod[i] == adn[1]:
            pares += adn[0]
        elif mod[i] == adn[2]:
            pares += adn[3]
        elif mod[i] == adn[3]:
            pares += adn[2]
    print("Hélice complementaria del modelo:", pares)

#Función 7.
def indicar_parent(muestra, ident):
    cont = 0
    for i in range(len(muestra)):
        if muestra[i] != ident[i]:
            cont += 1
    try:
        porc = str(100 -(cont*100)/len(muestra))
        if len(porc) > 4:
            porc = porc[0:5]
        print("\nEl porcentaje de parentesco entre la muestra y el identificador es", porc + "%\n")
    except ZeroDivisionError:
        print("\nLa muestra no contiene ningún elemento.\n")

#Función 8.
def indicar_especie(muestra, dic):
    l_keys = list(dic.keys())
    l_cont = []
    for i in range(len(l_keys)):
        cont = 0
        min = len(muestra)
        if min > len(dic[l_keys[i]]):
            min = len(dic[l_keys[i]])
        for j in range(min):
            if muestra[j] == dic[l_keys[i]][j]:
                 cont += 1             
        l_cont.append(cont)
    try:
        for i in range(len(l_cont)):
            if l_cont[i] == max(l_cont):
                porc = str((l_cont[i]*100)/len(muestra))
                if len(porc) > 4:
                    porc = porc[0:5]
                print(foreground.PURPLE +str(l_keys[i]), "es la especie con más similitudes a la muestra."+ foreground.DEFAULT 
                + foreground.LIGHT_BLUE +"\nSu ADN coincide en un " + porc + "%"+ foreground.DEFAULT)
                if len(muestra) != len(dic[l_keys[i]]):
                    print(foreground.ORANGE +"(Observación: la hélice comparada con "+
                    str(l_keys[i]) + " no posee el mismo número de nucleótidos)"+ foreground.DEFAULT, "\n")                
    except ZeroDivisionError:
        print("La muestra no contiene ningún elemento.")

#Main
adn = ["A", "T", "G", "C"]

#Punto 5
eleccion = 0
while eleccion != "1" and eleccion != "2":
    eleccion = (input("Ingrese 1 para crear un modelo de n caracteres aleatorios.\nIngrese 2 para escribir un modelo manualmente.\nElección: "))
modelo = ""
if eleccion == "1":
    n = "a"
    while n.isdigit() == False or n == "0":
        n = (input("Ingrese número de caracteres del modelo (sólo números naturales): "))
    for i in range(int(n)):
        modelo += adn[random.randint(0,3)] 
else:
        while len(modelo) == 0:
            modelo = input("Escriba su modelo (sólo caracteres A, T, G ó C): ")
            for i in range(len(modelo)):
                if modelo[i] != adn[0] and modelo[i] != adn[1] and modelo[i] != adn[2] and modelo[i] != adn[3]:
                    print("¡Sólo utilizar caracteres A, T, G ó C!")
                    modelo = ""
                    break
print("Su modelo:", modelo, "\n")

#Punto 1
identificador = crear_identif(modelo)
print("Identificador:", identificador)

#Punto 2
muestra = crear_muestra(identificador)
print("\nMuestra:", muestra)

#Punto 3
recrear_identif(identificador)

#Punto 4
recrear_identif_mod(identificador, modelo)

#Punto 6
imprimir_pares(modelo)

#Punto 7
indicar_parent(muestra, identificador)

#Punto 8
especies = {"Perro": "GGCAAAAGCCACGTTATTCG",
            "Gato": "ATGGGGGTACCGGTTACCCA",
            "Narval": "TACATGCGAGGGTGAAGTGC", 
            "Rana": "CCGTGGCCACACGCGGTACGCGATG"}
indicar_especie(muestra, especies)