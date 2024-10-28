# Ahorcadito
import random
def lecach():
    """Hace lectura de palabras a partir de un archivo
    (none) -> list
    """
    datos = []
    nom_arc = input("Digite nombre de archivo ")
    arch = open(nom_arc,"r")
    line = arch.readline().strip('\n')
    while line!= "":
        datos.append(line)
        line = arch.readline().strip('\n')
    arch.close()
    return datos
def palabra(lista):
    """ Escojer al azar una palabra de la lista y cuantas letras tiene
    (list) -> str, int
    """
    pal = random.choice(lista)
    num = len(pal)
    return pal, num
def espacios(numpal):
    """ Genera el tablero con los espacios suficientes de la palabrea
    (int) -> list
    """
    espa = []
    for i in range(0,numpal):
        espa.append("_")
    return espa
def comparar(palabra, letra, num, guarda):
    """ Verifica si la letra se encuentra en la palabra y la ubica en la posicion adecuada
    (str, str, int, list) -> bool, list
    """
    a = 0
    b = True
    for i in range(0,num):
        if letra == palabra[i]:
            guarda[i] = letra
            a = a + 1
    if a == 0:
        b = False
    return b, guarda 
def intentos(num):
    """ Determina cuantos intentois totales puede tener
    (int) -> int
    """
    return num + 6
def intgast(tv, err):
    """ Cuenta los intentos ya gastados
    () -> 
    """
    if tv:
        return err
    else:
        return err +1
def turnos(mal, fal, posi, inten, f):
    """ Mensajes de fin de juego
    (int, int, int, int) -> none 
    """
    if mal == fal:
        print("Fin errores")
    elif posi == inten:
        print("Maximo de intentos")
    elif f:
        print("Ganador")
def errores(error):
    """ Forma muñeco segun numero de errores
    (int) -> none 
    """
    if error == 1:
        print("__")
    elif error == 2:
        print("__")
        print("| |")
    elif error == 3:
        print("__")
        print("| |")
        print("| O")
    elif error == 4:
        print(" __\n| |\n| O\n| /\\")     
    elif error == 5:
        print(" __\n | | \n | O \n | /\ \n | /\ \n |   ")
def ganador(tab,num):
    """ Verifica si queda alguna letra por descubrir
    (lsit, int) -> bool 
    """
    for i in range(0,num):
        if "_" == tab[i]:
            return False
    return True
def letrep(let, l):
    """ Verifica si hay letras digitadas dos veces
    (list, str) ->
    """
    for i in range(0,len(let)):
        if let[i] == l:
            return True
    return False
def main():
    palabras = lecach()
    palabraa , numero = palabra(palabras)
    falt = espacios(numero)
    inten = intentos(numero)
    fal = 5
    print("Vamos a jugar ahorcadito. Debe encontrar la palabra escondida.","Son palabras de", numero ,"letras. Tiene", inten ,"oportunidades y", fal, "veces en las que puede fallar")
    mal = 0
    posi = 0
    letras = []
    fin = False
    print(falt)
    while mal < fal and posi < inten and fin == False:
        lt = input("letra?")
        posi = posi + 1
        confir, tablero = comparar(palabraa, lt, numero, falt)
        rep = letrep(letras, lt)
        fin = ganador(tablero,numero)
        if rep or confir == False:
            mal = mal + 1
        else:
            letras.append(lt)
        print(tablero)
        print("Intentos", posi)
        print("Errores", mal)
        ahor = errores(mal)
    turnos(mal, fal, posi, inten, fin)
    print("La palabra es", palabraa)     
main()

