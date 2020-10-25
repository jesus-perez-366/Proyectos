import random
import src.dibujo as do
from string import ascii_uppercase
ascii_uppercase += 'Ñ'
alphab=[i for i in ascii_uppercase]
alphab_not_use=[i for i in ascii_uppercase]
a=0
def Inp_Letter(letter,word,look):
    """
    Determina si la letra ingresada por el usuariose encuentra en el alfabeto, 
    en la palabra a adivinar y verifica si lo que ingreso el usuario sea
    unicamente y una sola letra del alfabeto
    Args:
        letter (str): letra ingresada por el jugador
        word (str): palabra que se debe adivinar
        look (str): es la palabra pero cada letra representada por "_"
    Returns:
        None
    """
    global a
    global alphab_not_use

    if len(letter) == 1 and letter in alphab_not_use and letter in word:
        look_alpha_not_use(letter, alphab_not_use,word,look)

    elif len(letter) == 1 and letter in alphab and letter not in word:
        a+=1
        rem_and_print(letter,look)
        if a == 8:
            a=0
            alphab_not_use=[i for i in ascii_uppercase]
            return
        space()
        Inp_Letter(input("por favor ingresa una letra del alfabeto: ").upper(),word,look)

    elif len(letter) == 1 or letter not in alphab:
        verif_use_letter(letter,word,look)



def rem_and_print(letter, look):
    """
    La letra no esta en la palabra por lo tanto se remueve  del alfabeton para asi garntizar
    que el usuario no repita la letra, ademas hace print del muñeco que sera ahorcado
    Args:
        letter (str): letra ingresada por el jugador
        look (str): es la palabra pero cada letra representada por "_"
    Returns:
        None
    """
    global a
    print("la letra escojida no se encuentra en la palabra")
    space()
    print(f'              {look}')
    space()
    alphab_not_use.remove(letter)
    do.lose(a,letter,alphab_not_use)
         


def verif_use_letter(letter,word,look):
    global a
    global alphab_not_use
    '''
    Determina si la letra ingresada fue usada anteriormente, si ingreso algo distinto a una letra 
    y que solo haya sido una letra.

    Ademas si la letra es la primera vez usada y como no esta en la palabra a adivinar entonces se
    remueve de alfabeto, muestra el muñeco que sera ahorcado.

    verifica por ultimo si el usuario perdio

    Args:
        letter (str): letra ingresada por el jugador
        word (str): palabra que se debe adivinar
        look (str): es la palabra pero cada letra representada por "_"
    Returns:
        si perdio
        str = indicado que ha perdido

    '''
    if len(letter) == 1:
        if letter not in alphab_not_use:
            print("Esta letra usted ya la uso o coloco un caracter especial")            
        else: 
            print("Ha ingresado un numero ")    
    else:
        print("usted ha colocado mas de una letra o numeros")  
    space()
    print(f'              {look}')
    space()
    do.lose(a,letter,alphab_not_use)
    if a == 8:
        alphab_not_use=[i for i in ascii_uppercase]
        a=0
        return
    space()
    Inp_Letter(input("por favor ingresa una letra del alfabeto: ").upper(),word,look)



def look_alpha_not_use(letter, alphab_not_use,word,look):
    """
    Verifica que no se haya usado la letra y entonces la remueve del alfabeto, 
    ademas actualiza la variable "look" para que el usuario visualice las palabras 
    que lleva y que le faltan. Tambien verifica si el usuarion adivino la 
    Args:
        letter (str): letra ingresada por el jugador
        alphab_not_use (list): son las letras que no ha colocado el usuario
        word (str): palabra que se debe adivinar
        look (str): es la palabra pero cada letra representada por "_"
    Returns:
        si gana
        str = indicado que es el ganador

        si pierde
        str = indicado que ha perdido

    """
    global a
    alphab_not_use.remove(letter)
    look2=[i if i == letter else "_" for i in word]
    list(map(lambda x, y: x if y=="_" else y, look,look2))
    look=" ".join(list(map(lambda x, y: x if y=="_" else y, look.split(),look2)))
    space()
    print(f'              {look}')
    space()
    do.lose(a,letter,alphab_not_use)
    if a == 8:
        alphab_not_use=[i for i in ascii_uppercase]
        a=0
        return
    elif "".join(look.split())==word:
        do.win()
        alphab_not_use=[i for i in ascii_uppercase]
        a=0
        return
    Inp_Letter(input("por favor ingresa una letra del alfabeto: ").upper(),word,look)


def space():
    ''' 
    Genera 3 espacio a lo vertical, no requiere de argumentos

    return:
        None
    '''
    print(" ")
    print(" ") 
    print(" ")





        



    



