
from AT009 import Guerreiro,Arqueiro,Mago,Armas
from AT009 import Lirio_A,Gargula_M,Alastor_G

def AtaqueForte(self):
    if isinstance(self, Arqueiro): 
        print(f"\nVc atirou Tres flechas!")
        print(f"seu dano foi = {self.força + self.mira + self.arma.power}")
        print(f"Força:{self.força} + Mira:{self.mira} + Arma:{self.arma.power} ")
    elif isinstance(self, Mago):
        print(f"\nGIGA FIRE BALL °°°°!!!")
        print(f"seu dano foi = {self.força + self.mana + self.arma.power}")
        print(f"Força:{self.força} + Mira:{self.mana} + Arma:{self.arma.power} ")
    elif isinstance(self, Guerreiro):
        print(f"\nVC TOMOU UMA PORRADA Forte!!")
        print(f"seu dano foi = {self.força + self.arma.power}")
        print(f"Força:{self.força} + Arma:{self.arma.power} ")

AtaqueForte(Lirio_A)
AtaqueForte(Alastor_G)
AtaqueForte(Gargula_M)


