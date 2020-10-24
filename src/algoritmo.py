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
                look=look.split()
                look[position-1] = i
                look=" ".join(look)
        print(look)
        if count==len(word):
            print('''
YYYYYYY       YYYYYYY     OOOOOOOOO     UUUUUUUU     UUUUUUUU                    WWWWWWWW                           WWWWWWWWIIIIIIIIIINNNNNNNN        NNNNNNNN
Y:::::Y       Y:::::Y   OO:::::::::OO   U::::::U     U::::::U                    W::::::W                           W::::::WI::::::::IN:::::::N       N::::::N
Y:::::Y       Y:::::Y OO:::::::::::::OO U::::::U     U::::::U                    W::::::W                           W::::::WI::::::::IN::::::::N      N::::::N
Y::::::Y     Y::::::YO:::::::OOO:::::::OUU:::::U     U:::::UU                    W::::::W                           W::::::WII::::::IIN:::::::::N     N::::::N
YYY:::::Y   Y:::::YYYO::::::O   O::::::O U:::::U     U:::::U                      W:::::W           WWWWW           W:::::W   I::::I  N::::::::::N    N::::::N
   Y:::::Y Y:::::Y   O:::::O     O:::::O U:::::D     D:::::U                       W:::::W         W:::::W         W:::::W    I::::I  N:::::::::::N   N::::::N
    Y:::::Y:::::Y    O:::::O     O:::::O U:::::D     D:::::U                        W:::::W       W:::::::W       W:::::W     I::::I  N:::::::N::::N  N::::::N
     Y:::::::::Y     O:::::O     O:::::O U:::::D     D:::::U                         W:::::W     W:::::::::W     W:::::W      I::::I  N::::::N N::::N N::::::N
      Y:::::::Y      O:::::O     O:::::O U:::::D     D:::::U                          W:::::W   W:::::W:::::W   W:::::W       I::::I  N::::::N  N::::N:::::::N
       Y:::::Y       O:::::O     O:::::O U:::::D     D:::::U                           W:::::W W:::::W W:::::W W:::::W        I::::I  N::::::N   N:::::::::::N
       Y:::::Y       O:::::O     O:::::O U:::::D     D:::::U                            W:::::W:::::W   W:::::W:::::W         I::::I  N::::::N    N::::::::::N
       Y:::::Y       O::::::O   O::::::O U::::::U   U::::::U                             W:::::::::W     W:::::::::W          I::::I  N::::::N     N:::::::::N
       Y:::::Y       O:::::::OOO:::::::O U:::::::UUU:::::::U                              W:::::::W       W:::::::W         II::::::IIN::::::N      N::::::::N
    YYYY:::::YYYY     OO:::::::::::::OO   UU:::::::::::::UU                                W:::::W         W:::::W          I::::::::IN::::::N       N:::::::N
    Y:::::::::::Y       OO:::::::::OO       UU:::::::::UU                                   W:::W           W:::W           I::::::::IN::::::N        N::::::N
    YYYYYYYYYYYYY         OOOOOOOOO           UUUUUUUUU                                      WWW             WWW            IIIIIIIIIINNNNNNNN         NNNNNNN

            ''')
            return
        Inp_Letter(input("por favor ingresa una letra del alfabeto2 :").upper(),word,look)

def look_word(letter,word,look):
    if letter in word:
        look_alpha_not_use(letter, alphab_not_use,word,look)
    else:
        print("la letra escojida no la tiene la palabra")
        alphab_not_use.remove(letter)
        print("")
        print(look)
        toy(a)
        if a == 9:
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

        GGGGGGGGGGGGG               AAA               MMMMMMMM               MMMMMMMMEEEEEEEEEEEEEEEEEEEEEE                    OOOOOOOOO     VVVVVVVV           VVVVVVVVEEEEEEEEEEEEEEEEEEEEEERRRRRRRRRRRRRRRRR   
     GGG::::::::::::G              A:::A              M:::::::M             M:::::::ME::::::::::::::::::::E                  OO:::::::::OO   V::::::V           V::::::VE::::::::::::::::::::ER::::::::::::::::R  
   GG:::::::::::::::G             A:::::A             M::::::::M           M::::::::ME::::::::::::::::::::E                OO:::::::::::::OO V::::::V           V::::::VE::::::::::::::::::::ER::::::RRRRRR:::::R 
  G:::::GGGGGGGG::::G            A:::::::A            M:::::::::M         M:::::::::MEE::::::EEEEEEEEE::::E               O:::::::OOO:::::::OV::::::V           V::::::VEE::::::EEEEEEEEE::::ERR:::::R     R:::::R
 G:::::G       GGGGGG           A:::::::::A           M::::::::::M       M::::::::::M  E:::::E       EEEEEE               O::::::O   O::::::O V:::::V           V:::::V   E:::::E       EEEEEE  R::::R     R:::::R
G:::::G                        A:::::A:::::A          M:::::::::::M     M:::::::::::M  E:::::E                            O:::::O     O:::::O  V:::::V         V:::::V    E:::::E               R::::R     R:::::R
G:::::G                       A:::::A A:::::A         M:::::::M::::M   M::::M:::::::M  E::::::EEEEEEEEEE                  O:::::O     O:::::O   V:::::V       V:::::V     E::::::EEEEEEEEEE     R::::RRRRRR:::::R 
G:::::G    GGGGGGGGGG        A:::::A   A:::::A        M::::::M M::::M M::::M M::::::M  E:::::::::::::::E                  O:::::O     O:::::O    V:::::V     V:::::V      E:::::::::::::::E     R:::::::::::::RR  
G:::::G    G::::::::G       A:::::A     A:::::A       M::::::M  M::::M::::M  M::::::M  E:::::::::::::::E                  O:::::O     O:::::O     V:::::V   V:::::V       E:::::::::::::::E     R::::RRRRRR:::::R 
G:::::G    GGGGG::::G      A:::::AAAAAAAAA:::::A      M::::::M   M:::::::M   M::::::M  E::::::EEEEEEEEEE                  O:::::O     O:::::O      V:::::V V:::::V        E::::::EEEEEEEEEE     R::::R     R:::::R
G:::::G        G::::G     A:::::::::::::::::::::A     M::::::M    M:::::M    M::::::M  E:::::E                            O:::::O     O:::::O       V:::::V:::::V         E:::::E               R::::R     R:::::R
 G:::::G       G::::G    A:::::AAAAAAAAAAAAA:::::A    M::::::M     MMMMM     M::::::M  E:::::E       EEEEEE               O::::::O   O::::::O        V:::::::::V          E:::::E       EEEEEE  R::::R     R:::::R
  G:::::GGGGGGGG::::G   A:::::A             A:::::A   M::::::M               M::::::MEE::::::EEEEEEEE:::::E               O:::::::OOO:::::::O         V:::::::V         EE::::::EEEEEEEE:::::ERR:::::R     R:::::R
   GG:::::::::::::::G  A:::::A               A:::::A  M::::::M               M::::::ME::::::::::::::::::::E                OO:::::::::::::OO           V:::::V          E::::::::::::::::::::ER::::::R     R:::::R
     GGG::::::GGG:::G A:::::A                 A:::::A M::::::M               M::::::ME::::::::::::::::::::E                  OO:::::::::OO              V:::V           E::::::::::::::::::::ER::::::R     R:::::R
        GGGGGG   GGGGAAAAAAA                   AAAAAAAMMMMMMMM               MMMMMMMMEEEEEEEEEEEEEEEEEEEEEE                    OOOOOOOOO                 VVV            EEEEEEEEEEEEEEEEEEEEEERRRRRRRR     RRRRRRR
        ''')
        return



