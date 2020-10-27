import random
import src.algoritmo as alg
import src.dibujo as do
do.incio()
alg.space()
User_name=input("Ingresar su Nombre: ")
alg.space()
print(f"Es momento de jugar {User_name}, espero que este preparado para el reto")
alg.space()
print('''ahora es tu turno de empezar adivinar la palabra.''')
alg.space()
c=open("lista_palabras.txt")
word_list=[]
rep="S"
archivo = open("lista_palabras.txt")
for linea in archivo.readlines():
    word_list.append(linea)  
archivo.close()
word_list=[s.rstrip('\n') for s in word_list]
while rep == "S" or rep == "SI":
    word=random.choice(word_list).upper()
    look="_ "*len(word)
    print(f'              {look}')
    alg.space()
    letter=input("por favor ingresa una letra del alfabeto :").upper()
    alg.Inp_Letter(letter,word,look)
    print(f"La palabra era {word}")
    alg.space()
    rep=input("Desea volver a jugar S/N:").upper()
    

