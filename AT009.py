from AT007 import Armas

class Guerreiro:
    def __init__(self,nome,vida,força,arma):
        self.nome = nome
        self.vida = vida 
        self.força = força
        self.arma = arma

Espada_longa = Armas('Espada_longa', 40)        
Alastor_G = Guerreiro('Alastor',150,30,Espada_longa)

class Mago:
    def __init__(self,nome,vida,força,mana,arma):
        self.nome = nome
        self.vida = vida 
        self.força = força
        self.mana = mana
        self.arma = arma

Cajado = Armas("Cajado",30)
Gargula_M = Mago('Gargula',60,10,200,Cajado)

class Arqueiro:
    def __init__(self,nome,vida,força,mira,arma):
        self.nome = nome
        self.vida = vida 
        self.força = força
        self.mira = mira
        self.arma = arma

Arco = Armas("Arco",25)
Lirio_A = Arqueiro('Lirio',70,40,60,Arco)