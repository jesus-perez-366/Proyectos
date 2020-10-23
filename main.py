import random
from string import ascii_uppercase
import src.algoritmo as alg
User_name=input("Ingresar su Nombre: ")
print(f"Es momento de jugar {User_name}, espero que este preparado para el reto")
print("Let`s Goooooo")
print("ahora es tu turno de empezar adivinar la palabra")
word_list=["maria", "jesus", "casa"]
word=random.choice(word_list)
print("_ "*len(word))
letter=input("por favor ingresa una letra del alfabeto :").upper
alg.Inp_Letter(letter,word)
