import random
import src.dibujo as do
from string import ascii_uppercase
ascii_uppercase += 'Ñ'
alphab=[i for i in ascii_uppercase]
alphab_not_use=alphab
a=0

def Inp_Letter(letter,word,look):
    global a
    if len(letter) == 1 and letter in alphab and letter in word:
        look_alpha_not_use(letter, alphab_not_use,word,look)

    elif len(letter) == 1 and letter in alphab and letter not in word:
        a+=1
        rem_and_print(letter,look)
        if a == 8:
            return
        space()
        Inp_Letter(input("por favor ingresa una letra del alfabeto: ").upper(),word,look)

    elif len(letter) == 1 or letter not in alphab:
        verif_use_letter(letter,word,look)



def rem_and_print(letter, look):
    global a
    print("la letra escojida no se encuentra en la palabra")
    space()
    print(f'              {look}')
    space()
    alphab_not_use.remove(letter)
    do.lose(a,letter,alphab_not_use)
         


def verif_use_letter(letter,word,look):
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
            return
    space()
    Inp_Letter(input("por favor ingresa una letra del alfabeto: ").upper(),word,look)



def look_alpha_not_use(letter, alphab_not_use,word,look):
    if letter in alphab_not_use:
        alphab_not_use.remove(letter)
        look2=[i if i == letter else "_" for i in word]
        list(map(lambda x, y: x if y=="_" else y, look,look2))
        look=" ".join(list(map(lambda x, y: x if y=="_" else y, look.split(),look2)))
        space()
        print(f'              {look}')
        space()
        do.lose(a,letter,alphab_not_use)
        if a == 8:
            return
        space()
        elif "".join(look.split())==word:
            do.win()
            return
        Inp_Letter(input("por favor ingresa una letra del alfabeto: ").upper(),word,look)


def space():
    print(" ")
    print(" ") 
    print(" ")





        



    



