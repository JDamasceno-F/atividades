from AT016INV import Inventario
from AT008 import Porcao_de_cura
from AT017APOIO import Armas

class Personagem:
    def __init__(self, nome, vida, força):
        self.nome = nome
        self.__vida = vida # O "__" torna a vida PRIVADA (escondida)
        self.força = força
        self.inventario = Inventario()
        self.vida_maxima = vida #limite máximo de vida

    def get_vida(self):
        return self.__vida

    def set_vida(self, nova_vida):
        if nova_vida < 0:
            print(f"Atenção: {self.nome} não pode ter vida negativa. Zerando vida.")
            self.__vida = 0
        elif nova_vida > self.vida_maxima:
            # Proteção para não curar além do máximo
            self.__vida = self.vida_maxima 
        else:
            self.__vida = nova_vida

    def receber_dano(self, dano):
        vida_restante = self.__vida - dano 
        self.set_vida(vida_restante)

    def receber_cura(self, cura):
        vida_recuperada = self.__vida + cura
        self.set_vida(vida_recuperada)
        print(f" {self.nome} recuperou {cura} HP! Vida: {self.__vida}/{self.vida_maxima}")

    def beberpocao(self):
        from AT008 import Porcao_de_cura
        if Porcao_de_cura in self.inventario.itens:# Procura pelo TEXTO exato na lista
            self.inventario.itens.remove(Porcao_de_cura) # Tira da mochila
            self.receber_cura(Porcao_de_cura.valor) # Cura 50 pontos
            print("Glup glup... Poção consumida.")
        else:
            print(" Você não tem Poção de Cura na mochila!")

class Guerreiro(Personagem):
    def __init__(self,nome,vida,força,Resistencia,arma):
        super().__init__(nome, vida, força)
        self.Resistencia = Resistencia
        self.arma = arma

Espada_longa = Armas('Espada_longa', 40)        
Alastor_G = Guerreiro('Alastor',150,30,15,Espada_longa)

Alastor_G.inventario.adicionar_item(Porcao_de_cura)
Alastor_G.receber_dano(50)
print(f"Vida pós-dano: {Alastor_G.get_vida()}")

#TESTE 
Alastor_G.beberpocao()