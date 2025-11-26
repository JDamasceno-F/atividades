#CODIGO BASE PARA A QUESTÃO 14
class Personagem:
    def __init__(self, nome, vida, força):
        self.nome = nome
        self.__vida = vida # O "__" torna a vida PRIVADA (escondida)
        self.força = força

    def get_vida(self):
        return self.__vida

    # Método SET: Permite alterar a vida, MAS com regras
    def set_vida(self, nova_vida):
        if nova_vida < 0:
            print(f"Atenção: {self.nome} não pode ter vida negativa. Zerando vida.")
            self.__vida = 0
        else:
            self.__vida = nova_vida

    def receber_dano(self, dano):
        # Pega a vida atual e subtrai o dano
        vida_restante = self.__vida - dano
        #  Manda o valor calculado para o set_vida
        # O set_vida JÁ TEM a proteção que impede ficar negativo 
        self.set_vida(vida_restante)

# O TESTE DO CODIGO FICARÁ NO FINAL

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

