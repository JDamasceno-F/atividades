from AT016INV import Inventario
from AT014APOIO import Alastor_G
from AT014APOIO import Armas

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

class Guerreiro(Personagem):
    def __init__(self,nome,vida,força,Resistencia,arma):
        super().__init__(nome, vida, força)
        self.Resistencia = Resistencia
        self.arma = arma

Espada_longa = Armas('Espada_longa', 40)        
Alastor_G = Guerreiro('Alastor',150,30,15,Espada_longa)

#TESTANDO O CODIGO
Alastor_G.inventario.adicionar_item(Espada_longa)
Alastor_G.inventario.adicionar_item("Capacete")

Alastor_G.inventario.listar_itens()