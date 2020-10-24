import random
from string import ascii_uppercase
import src.algoritmo as alg
from src import dibujo
User_name=input("Ingresar su Nombre: ")
print(f"Es momento de jugar {User_name}, espero que este preparado para el reto")
print("Let`s Goooooo")
print("ahora es tu turno de empezar adivinar la palabra")
word_list=["marias", "jesus", "casa"]
word=random.choice(word_list).upper()
look="_ "*len(word)
print(look)
letter=input("por favor ingresa una letra del alfabeto :").upper()
alg.Inp_Letter(letter,word,look)
