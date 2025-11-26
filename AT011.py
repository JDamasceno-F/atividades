class Personagem:
    def __init__(self, nome, vida, forca):
        self.nome = nome
        self.vida = vida
        self.forca = forca

#corrigindo as classes:

from AT007 import Armas
#ignore pfv isso é para importar para outras ativides

class Guerreiro(Personagem):
    def __init__(self,nome,vida,força,Resistencia,arma):
        super().__init__(nome, vida, força)
        self.Resistencia = Resistencia
        self.arma = arma

Espada_longa = Armas('Espada_longa', 40)        
Alastor_G = Guerreiro('Alastor',150,30,15,Espada_longa)

class Mago(Personagem):
    def __init__(self,nome,vida,força,mana,arma):
        super().__init__(nome, vida, força)
        self.mana = mana
        self.arma = arma

Cajado = Armas("Cajado",30)
Gargula_M = Mago('Gargula',60,10,200,Cajado)

class Arqueiro(Personagem):
    def __init__(self,nome,vida,força,mira,arma):
        super().__init__(nome, vida, força)
        self.mira = mira
        self.arma = arma

Arco = Armas("Arco",25)
Lirio_A = Arqueiro('Lirio',70,40,60,Arco)