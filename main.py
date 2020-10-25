import random
import src.algoritmo as alg
User_name=input("Ingresar su Nombre: ")
alg.space()
print(f"Es momento de jugar {User_name}, espero que este preparado para el reto")
alg.space()
print('''ahora es tu turno de empezar adivinar la palabra''')
alg.space()
word_list=["marias", "jesus", "casa"]
word=random.choice(word_list).upper()
look="_ "*len(word)
print(f'              {look}')
alg.space()
letter=input("por favor ingresa una letra del alfabeto :").upper()
alg.Inp_Letter(letter,word,look)
