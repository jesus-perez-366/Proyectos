import random
from string import ascii_uppercase
ascii_uppercase += 'Ñ'
alphab=[i for i in ascii_uppercase]
alphab_not_use=alphab
count=0
position=0
a=1
def look_alpha_not_use(letter, alphab_not_use,word,look):
    global count
    global position
    if letter in alphab_not_use:
        alphab_not_use.remove(letter)
        position=0
        for i in word:
            position+=1
            if i == letter:
                count+=1
                print(count)
                look=look.split()
                look[position-1] = i
                look=" ".join(look)
                print(look)

                #hay que pensar como sustituir los _ por las letras
        if count==len(word):
            print('''
_____.___.________   ____ ___      __      __.___ _______   
\__  |   |\_____  \ |    |   \    /  \    /  \   |\      \  
 /   |   | /   |   \|    |   /    \   \/\/   /   |/   |   \ 
 \____   |/    |    \    |  /      \        /|   /    |    \ 
 / ______|\_______  /______/        \__/\  / |___\____|__  /
 \/               \/                     \/              \/

            ''')
            return
        Inp_Letter(input("por favor ingresa una letra del alfabeto2 :").upper(),word,look)

def look_word(letter,word,look):
    if letter in word:
        look_alpha_not_use(letter, alphab_not_use,word,look)
    else:
        print("la letra escojida no la tiene la palabra")
        alphab_not_use.remove(letter)
        toy(a)
        print("")
        print(look)
        if a == 9:
            print("Perdiste!!!!!!")
            return
        Inp_Letter(input("por favor ingresa una letra del alfabeto4 :").upper(),word,look)
        #inventarse lo del dibujo
        

def look_alphab (letter,alphab,word,look):
    if letter in alphab:
        look_word(letter,word,look)

    else:
        if letter > "20" :
            print("la letra escojida usted ya la uso")
            print(look)
            Inp_Letter(input("por favor ingresa una letra del alfabeto5 :").upper(),word,look)
        else:
            print("usted ha ingresado un numero o un caracter")
            print(look)
            Inp_Letter(input("por favor ingresa una letra del alfabeto5 :").upper(),word,look)


def Inp_Letter(letter,word,look):
    if len(letter) == 1:
        look_alphab(letter,alphab,word,look)
    else:
            print("ingreso mas de una letra")
            print(look)
            Inp_Letter(input("por favor ingresa una letra del alfabeto5 :").upper(),word,look)


def toy(b):
    print(b)
    global a
    if b == 1:
        a=2
        print('''     
    ________________________
    ''')
        print(a)
    elif b == 2:
        a=3
        print(''' 
                |
                |
                |
                |
                |
                | 
    ____________|____________
    ''')
                    
    elif b == 3:
        a=4
        print('''   
                _____________
                |
                |
                |
                |
                |
                | 
    ____________|____________
    ''')

    elif b == 4:
        a=5
        print('''   
                _____________
                |            O
                |
                |
                |
                |
                | 
    ____________|____________
    ''')

    elif b == 5:
        a=6
        print('''   
                _____________
                |            O
                |            |
                |            |
                |
                |
                | 
    ____________|____________
    ''')

    elif b == 6:
        a=7
        print('''   
                _____________
                |            O
                |           /|
                |            |
                |           /
                |
                | 
    ____________|____________
    ''')

    elif b == 7:
        a=8
        print('''
                _____________
                |            O
                |           /|/
                |            |
                |           / /
                |
                | 
    ____________|____________
    ''')

    elif b == 8:
        a=9
        print('''   
                _______________
                |          |_O_|
                |           /|/
                |            |
                |           / /
                |
                | 
    ____________|____________
    ''')
        print('''  

  ________    _____      _____  ___________ ____________   _________________________ 
 /  _____/   /  _  \    /     \ \_   _____/ \_____  \   \ /   /\_   _____/\______   \ 
/   \  ___  /  /_\  \  /  \ /  \ |    __)_   /   |   \   Y   /  |    __)_  |       _/
\    \_\  \/    |    \/    Y    \|        \ /    |    \     /   |        \ |    |   \ 
 \______  /\____|__  /\____|__  /_______  / \_______  /\___/   /_______  / |____|_  /
        \/         \/         \/        \/          \/                 \/         \/ 
        ''')




