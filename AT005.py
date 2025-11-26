#ESPAÇ_O
print("       ")

from AT001 import Guerreiro
from AT002 import Mago
from AT003 import Arqueiro

#Personagens
Gargula_M = Mago('Gargula',60,10,200)

Lirio_A = Arqueiro('Lirio',70,40,60)

Alastor_G = Guerreiro('Alastor',150,30)

def status(self):
    print("--Status do personagem--")
    print(f" nome:{self.nome}")
    print(f" vida:{self.vida}")
    print(f" força:{self.força}")
    
    if isinstance(self, Arqueiro): 
        print(f" mira:{self.mira}")
    elif isinstance(self, Mago):
        print(f" mana:{self.mana}")
    

#Verificando o Status
status(Lirio_A)
status(Alastor_G)
status(Gargula_M)



#ESPAÇ_O
print("       ")