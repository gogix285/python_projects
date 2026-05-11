import random
import time
#import writing.System
from typing import Literal


version = "v1.6.82" #v2.x.x bo ko narediš razmišljanje!!!!

moznosti = ["a1", "b1", "c1", "a2", "b2", "c2", "a3", "b3", "c3"]
dano = []

class Mreza(object):
    a1=" "
    b1=" "
    c1=" "
    a2=" "
    b2=" "
    c2=" "
    a3=" "
    b3=" "
    c3=" "
def kazi_mrezo():
    global mreza
    print(f"c {mreza.c1} | {mreza.c2} | {mreza.c3} ")
    print(" ___ ___ ___")
    print(f"b {mreza.b1} | {mreza.b2} | {mreza.b3} ")
    print(" ___ ___ ___")
    print(f"a {mreza.a1} | {mreza.a2} | {mreza.a3} ")
    print(" 1    2   3")
def najd_in_zbris(obj):
    global moznosti
    for m in moznosti:
        if m == obj:
            moznosti.remove(obj)
def dodaj_v_mrezo(izbira_mesta, user:Literal["rac", "player"]): #Literal=type
    global mreza
    global player_da
    global moznosti
    if user == "player":
        if izbira_mesta == "a1":
            mreza.a1 = "X"
            najd_in_zbris("a1")
        elif izbira_mesta == "b1":
            mreza.b1 = "X"
            najd_in_zbris("b1")
        elif izbira_mesta == "c1":
            mreza.c1 = "X"
            najd_in_zbris("c1")
        elif izbira_mesta == "a2":
            mreza.a2 = "X"
            najd_in_zbris("a2")
        elif izbira_mesta == "b2":
            mreza.b2 = "X"
            najd_in_zbris("b2")
        elif izbira_mesta == "c2":
            mreza.c2 = "X"
            najd_in_zbris("c2")
        elif izbira_mesta == "a3":
            mreza.a3 = "X"
            najd_in_zbris("a3")
        elif izbira_mesta == "b3":
            mreza.b3 = "X"
            najd_in_zbris("b3")
        elif izbira_mesta == "c3":
            mreza.c3 = "X"
            najd_in_zbris("c3")
    elif user == "rac":
        if izbira_mesta == "a1":
            mreza.a1 = "O"
            najd_in_zbris("a1")
        elif izbira_mesta == "b1":
            mreza.b1 = "O"
            najd_in_zbris("b1")
        elif izbira_mesta == "c1":
            mreza.c1 = "O"
            najd_in_zbris("c1")
        elif izbira_mesta == "a2":
            mreza.a2 = "O"
            najd_in_zbris("a2")
        elif izbira_mesta == "b2":
            mreza.b2 = "O"
            najd_in_zbris("b2")
        elif izbira_mesta == "c2":
            mreza.c2 = "O"
            najd_in_zbris("c2")
        elif izbira_mesta == "a3":
            mreza.a3 = "O"
            najd_in_zbris("a3")
        elif izbira_mesta == "b3":
            mreza.b3 = "O"
            najd_in_zbris("b3")
        elif izbira_mesta == "c3":
            mreza.c3 = "O"
            najd_in_zbris("c3")
def konec_igre_ali_player():
    if (mreza.a1 == "X" == mreza.b1 and mreza.c1 == "X"
            or mreza.a2 == "X" == mreza.b2 and mreza.c2 == "X"
            or mreza.a3 == "X" == mreza.b3 and mreza.c3 == "X"
            or mreza.a1 == "X" == mreza.a2 and mreza.a3 == "X"
            or mreza.b1 == "X" == mreza.b2 and mreza.b3 == "X"
            or mreza.c1 == "X" == mreza.c2 and mreza.c3 == "X"
            or mreza.a1 == "X" == mreza.b2 and mreza.c3 == "X"
            or mreza.a3 == "X" == mreza.b2 and mreza.c1 == "X"
    ):
        return True
    else:
        return False
def konec_igre_ali_rac():
    if (mreza.a1 == "O" == mreza.b1 and mreza.c1 == "O"
            or mreza.a2 == "O" == mreza.b2 and mreza.c2 == "O"
            or mreza.a3 == "O" == mreza.b3 and mreza.c3 == "O"
            or mreza.a1 == "O" == mreza.a2 and mreza.a3 == "O"
            or mreza.b1 == "O" == mreza.b2 and mreza.b3 == "O"
            or mreza.c1 == "O" == mreza.c2 and mreza.c3 == "O"
            or mreza.a1 == "O" == mreza.b2 and mreza.c3 == "O"
            or mreza.a3 == "O" == mreza.b2 and mreza.c1 == "O"
    ):
        return True
    else:
        return False
def beri(kaj:Literal["zmaga.txt", "zgubil.txt"]):
    with open(kaj, "r") as f:
        _in = f.read()
        dvadela = _in.split("|")
        b = []
        for i in dvadela:
            b.append(i.split(","))
def dodaj(kaj, kam:Literal["zmaga.txt", "zgubil.txt"]):
    with open(kam, "a") as f:
        _dvadela = []
        for i in kaj:
            _dvadela.append(",".join(i))
        in_ = "|".join(_dvadela)
        f.write("|")
        f.write(in_)

mreza = Mreza()

print("mreža za križce in krožce")
print("TI SI 'X' IN RAČUNALNIK JE 'O'")
kazi_mrezo()


#   MAIN LOOP
while True:
    #player izbira in prikaz
    player_da=str(input("Kam daš: "))
    while not player_da in moznosti:
        print("ne moreš")
        player_da = str(input("Kam daš: "))
    dano.append(player_da)
    dodaj_v_mrezo(player_da, "player")
    kazi_mrezo()
    time.sleep(1)

    # preveri za konec igre prvic
    if konec_igre_ali_player():
        print("ZMAGAL SI!!!! BRAVO")
        dodaj([dano], "zgubil.txt")
        break
    elif konec_igre_ali_rac():
        print("žal si zgubil. Več sreče prihodnjič")
        dodaj([dano], "zmaga.txt")
        break

    #
    print("*******************************")
    #rac izbira in prikaz
    rac_da = random.choice(moznosti)
    dano.append(rac_da)
    dodaj_v_mrezo(rac_da, "rac")
    kazi_mrezo()
    time.sleep(1)

    #preveri za konec igre drugic
    if konec_igre_ali_player():
        print("ZMAGAL SI!!!! BRAVO")
        dodaj([dano], "zgubil.txt")
        break
    elif konec_igre_ali_rac():
        print("žal si zgubil. Več sreče prihodnjič")
        dodaj([dano], "zmaga.txt")
        break
    print(dano)
print(dano)
print("done")
