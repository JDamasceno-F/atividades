from AT019 import Monstro
from AT017APOIO import Guerreiro

def esta_vivo(self):
        # Retorna True se a vida for maior que 0
        # Retorna False se for 0
        if self.__vida > 0:
            return True
        else:
            return False
        
Goblin = Monstro.criar_goblin()

Conan = Guerreiro("Conan", 100, 20, 10,"Espada_longa" )

print(f"--- Início do Combate: {Conan.nome} vs {Goblin.nome} ---")

while Goblin.esta_vivo():
    print("Conan ataca!")
    Conan.atacar(Goblin)
    # Verifica se morreu após o golpe
    if Goblin.esta_vivo():
        print(f"O Goblin ainda está de pé com {Goblin.get_vida()} de HP!\n")
    else:
        print("\n💀 O Goblin caiu derrotado!")
