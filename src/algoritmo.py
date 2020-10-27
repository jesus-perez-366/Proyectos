import random
import src.dibujo as do
from string import ascii_uppercase
ascii_uppercase += 'Ñ'
alphab=[i for i in ascii_uppercase]
alphab_not_use=[i for i in ascii_uppercase]
a=0
look=str
word=str
def word_list():
    do.incio()
    User_name=input("Ingresar su Nombre: ")
    print(f"Es momento de jugar {User_name}, espero que este preparado para el reto \ ahora es tu turno de empezar adivinar la palabra")
    print('''ahora es tu turno de empezar adivinar la palabra''')
    c=open("lista_palabras.txt")
    word_list=[]
    archivo = open("lista_palabras.txt")
    for linea in archivo.readlines():
        word_list.append(linea)  
    archivo.close()
    return [s.rstrip('\n') for s in word_list]
    

def inicio (word_list):
    global look, word
    word=random.choice(word_list).upper()
    look="_ "*len(word)
    print(f'              {look}')

def Inp_Letter(letter):
    """
    Determina si la letra ingresada por el usuariose encuentra en el alfabeto, 
    en la palabra a adivinar y verifica si lo que ingreso el usuario sea
    unicamente y una sola letra del alfabeto
    Args:
        letter (str): letra ingresada por el jugador
    Returns:
        None
    """
    global a, alphab_not_use, look, word
    if letter in alphab_not_use and letter in word:
        look_alpha_not_use(letter)

    elif len(letter) == 1 and letter not in word:
        rem_and_print(letter)
        if a == 8:
            out()
            return

        Inp_Letter(input("por favor ingresa una letra del alfabeto: ").upper())

    elif letter not in alphab_not_use:
        verif_use_letter(letter)



def rem_and_print(letter):
    """
    La letra no esta en la palabra por lo tanto se remueve  del alfabeton para asi garntizar
    que el usuario no repita la letra, ademas hace print del muñeco que sera ahorcado
    Args:
        letter (str): letra ingresada por el jugador
    Returns:
        None
    """
    global a, look, word, alphab_not_use
    print("la letra escojida no se encuentra en la palabra")
    print(f'              {look}')
    if letter in alphab_not_use:
        a+=1
        alphab_not_use.remove(letter)
        do.lose(a,letter)
    pass
         


def verif_use_letter(letter):
    global a, alphab_not_use, look, word
    '''
    Determina si la letra ingresada fue usada anteriormente, si ingreso algo distinto a una letra 
    y que solo haya sido una letra.
    Ademas si la letra es la primera vez usada y como no esta en la palabra a adivinar entonces se
    remueve de alfabeto, muestra el muñeco que sera ahorcado.
    verifica por ultimo si el usuario perdio
    Args:
        letter (str): letra ingresada por el jugador
    Returns:
        si perdio
        str = game over
    '''
    if len(letter) == 1:
        print("ya ingreso esta letra o ha colocado un numero")    
    else:
        print("usted ha colocado mas de una letra o numeros")  
    print(f'              {look}')
    do.lose(a,letter)
    if a == 8:
        out()
        return
    Inp_Letter(input("por favor ingresa una letra del alfabeto: ").upper())



def look_alpha_not_use(letter):
    """
    Verifica que no se haya usado la letra y entonces la remueve del alfabeto, 
    ademas actualiza la variable "look" para que el usuario visualice las palabras 
    que lleva y que le faltan. Tambien verifica si el usuarion adivino la 
    Args:
        letter (str): letra ingresada por el jugador
    Returns:
        si gana
        str = you win
        si pierde
        str = game over
    """
    global a, look, word, alphab_not_use
    alphab_not_use.remove(letter)
    look2=[i if i == letter else "_" for i in word]
    list(map(lambda x, y: x if y=="_" else y, look,look2))
    look=" ".join(list(map(lambda x, y: x if y=="_" else y, look.split(),look2)))
    print(f'              {look}')
    do.lose(a,letter)
    if a == 8:
        out()
        return
    elif "".join(look.split())==word:
        do.win()
        out()
        return
    Inp_Letter(input("por favor ingresa una letra del alfabeto: ").upper())


def out():
    global alphab_not_use, a
    alphab_not_use=[i for i in ascii_uppercase]
    a=0
    print(f"La palabra era {word}")


