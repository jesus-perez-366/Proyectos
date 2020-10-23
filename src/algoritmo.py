import random
from string import ascii_uppercase
ascii_uppercase += 'Ñ'
alphab=[i for i in ascii_uppercase]
alphab_not_use=alphab
def Inp_Letter(letter,word):
    letter=input("por favor ingresa una letra del alfabeto :").upper
    if letter in alphab:
        if letter in word:
            if letter in alphab_not_use:
                alphab_not_use.remove(letter)
                for i in word:
                    if i == letter:
                        count+=1
                        #hay que pensar como sustituir los _ por las letras
                    elif count==len(word):
                        print("Usted es el Ganador!!!!!!")
                        return
                Inp_Letter(input("por favor ingresa una letra del alfabeto :").upper,word)
            else:
                print("usted ya uso esta letra")
                Inp_Letter(input("por favor ingresa una letra del alfabeto :").upper,word)
        else:
            print("la letra escojida no la tiene la palabra")
            alphab_not_use.remove(letter)
            
            #inventarse lo del dibujo
            
    else:
        if False:
            print("Perdiste!!!!!!")
            return
        else:
            Inp_Letter(input("por favor ingresa una letra del alfabeto :").upper,word)

