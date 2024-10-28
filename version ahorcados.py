# Ahorcadito
import random
def palabra():
    lista = ["acaba","caballo","ballena","casa","hora","ola","de","tal ","camilla","agria","algun","barra","bingo","causa"]
    pal = random.choice(lista)
    num = len(pal)
    return pal, num
def espacios(numpal):
    espa = []
    for i in range(0,numpal):
        espa.append("_")
    return espa
def comparar(palabra, letra, num, guarda):
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
    return num + 6

def intgast(tv, err):
    if tv:
        return err
    else:
        return err +1
#def ganador(tab,num):
 #   for i in range(0,num):
  #      if "_" == tab[i]:
   #         return pass
    #return ganarmen()

def errores(error):
    if error==1:
        print("__")
    elif error==2:
        print("__")
        print("| |")
    elif error==3:
        print("__")
        print("| |")
        print("| O")
    elif error==4:
        print(" __\n| |\n| O\n| /\\")
        
    elif error==5:
        
        print(" __\n | | \n | O \n | /\ \n | /\ \n |   ")
def repetido(mal,letra,letras_ingresadas):
    if letra in letras_ingresadas:
        
        print("La letra ya se ingreso anteriormente. Pierde una oportunidad")
        mal=mal+1
        return False
    else:
        letras_ingresadas.append(letra)
        mal=mal+0
        return True
        
def ganarmen():
    print("GANADOR")
def turnos(mal, fal, posi, inten):
    if mal == fal:
        print("Fin errores")
    elif posi == inten:
        print("Maximo de intentos")
def main():
    lista=[]
    palabraa , numero = palabra()
    falt = espacios(numero)
    inten = intentos(numero)
    fal = 5
    print("Vamos a jugar ahorcadito. Debe encontrar la palabra escondida.","Son palabras de", numero ,"letras. Tiene", inten ,"oportunidades y", fal, "veces en las que puede fallar")
    mal = 0
    posi = 0
    while mal < fal and posi < inten:
        lt = input("letra?")
        rep=repetido(mal,lt,lista)
        posi = posi + 1
        confir, tablero = comparar(palabraa, lt, numero, falt)
        mal = intgast(confir, mal)
        print(tablero)
        print("Intentos", posi)
        print("Errores", mal)
        errores(mal)
        #ganador(tablero,numero)
    turnos(mal, fal, posi, inten)
    if intentos==posi:
        print("El jugador ha ganado")
    else:
        print("El jugador ha perdido")
        
main()
