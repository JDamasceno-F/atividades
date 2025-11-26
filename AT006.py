print("       ")

from AT001 import Guerreiro
from AT002 import Mago
from AT003 import Arqueiro

#personagens

Gargula_M = Mago('Gargula',60,10,200)

Lirio_A = Arqueiro('Lirio',70,40,60)

Alastor_G = Guerreiro('Alastor',150,30)
#açoes

def ataque_s(self):
        if isinstance(self, Arqueiro): 
            print(f"Vc atirou uma flecha!")
        elif isinstance(self, Mago):
            print(f"FIRE BALL °°°°!!!")
        elif isinstance(self, Guerreiro):
             print(f"VC TOMOU UMA PORRADA FRACA!!")

#Realizando as açoes
ataque_s(Alastor_G)
ataque_s(Lirio_A)
ataque_s(Gargula_M)


print("       ")