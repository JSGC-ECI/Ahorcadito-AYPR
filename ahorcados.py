import random


def lista():
    """funcion que asigna una palabra al azar de la lista
    """
    lstt=["acaba","caballo","ballena","casa","hora",
          "ola","de","tal ","camilla","agria","algun",
          "barra","bingo","causa"]
    ran=random.choice(lstt)   
    return ran

def espacios(numpal):
    lst2=[]
    for i in range(0,numpal):
        lst2.append("-")
    return lst2


def comparar(pal,letra,num):
    guarda=[]
    for i in range(0,num):
        if letra==pal[i]:
            guarda.append[i]
    return guarda

def acierto(si,tablero,letra):
    for i in range(0,len(si)):
        tablero[si[i]]=letra
    
    return tablero


def acierto(espa,pala,let):
    lis=comparar(pala,let,len(pala))
    espa=espacios(len(pala))
    for i in range(0,len(pala)):
        if let in pala:
            espa[i]=lis[i]
    
        

def errores(let):
    palabra=lista()
    acum=0
    if let not in palabra:
        acum=acum+1
    return acum

        

def main():
    palabra=lista()
    long=len(palabra)
    intentos_maximos=len(palabra)+4
    intentos=0
    
    print("Vamos a jugar ahorcadito. Debe encontrar la palabra escondida.",
          "Son palabras de",long,"letras. Tiene",intentos,"oportunidades")
    
    esp=espacios(long)
    es= " ".join(esp)
    print(es)
    while intentos < intentos_maximos:
        lt=input("letra?")
        intentos=intentos+1
        acierto(esp,palabra,lt)
    
    

    
          



