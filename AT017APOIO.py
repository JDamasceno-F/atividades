from AT016INV import Inventario
from AT008 import Porcao_de_cura

class Personagem:
    def __init__(self, nome, vida, força):
        self.nome = nome
        self.__vida = vida # O "__" torna a vida PRIVADA (escondida)
        self.força = força
        self.inventario = Inventario()

    def get_vida(self):
        return self.__vida

    def set_vida(self, nova_vida):
        if nova_vida < 0:
            print(f"Atenção: {self.nome} não pode ter vida negativa. Zerando vida.")
            self.__vida = 0
        else:
            self.__vida = nova_vida

    def receber_dano(self, dano):
        vida_restante = self.__vida - dano 
        self.set_vida(vida_restante)

#ignore:

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
