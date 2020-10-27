  
import random
import src.algoritmo as alg
import src.dibujo as do
rep="S"
word_list=[]
word_list=alg.word_list()
while rep == "S" or rep == "SI":
    alg.inicio (word_list)
    letter=input("por favor ingresa una letra del alfabeto :").upper()
    alg.Inp_Letter(letter)
    rep=input("Desea volver a jugar S/N:").upper()
