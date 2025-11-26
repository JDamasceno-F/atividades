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

#from AT014APOIO import Personagem
from AT014APOIO import Guerreiro,Mago,Arqueiro
from AT014APOIO import Alastor_G,Gargula_M,Lirio_A

def AtaqueForte(atacante, alvo):
    dano_total = 0 # Criamos uma variável para guardar o valor do dano


    if isinstance(atacante, Arqueiro): 
        print(f"\nVc atirou Tres flechas!")
        # Calculamos o dano e guardamos na variável
        dano_total = atacante.força + atacante.mira + atacante.arma.power
        print(f"Cálculo: Força {atacante.força} + Mira {atacante.mira} + Arma {atacante.arma.power}")
    elif isinstance(atacante, Mago):
        print(f"\nGIGA FIRE BALL °°°°!!!")
        dano_total = atacante.força + atacante.mana + atacante.arma.power
        print(f"Cálculo: Força {atacante.força} + Mana {atacante.mana} + Arma {atacante.arma.power}")
    elif isinstance(atacante, Guerreiro):
        print(f"\nVC TOMOU UMA PORRADA Forte!!")
        dano_total = atacante.força + atacante.arma.power
        print(f"Cálculo: Força {atacante.força} + Arma {atacante.arma.power}")

    print(f"--> Causou {dano_total} de dano em {alvo.nome}!")
    alvo.receber_dano(dano_total)

# TESTE
# Lirio ataca o Alastor
AtaqueForte(Lirio_A, Alastor_G)

print(f"Vida atual do Alastor: {Alastor_G.get_vida()}")

AtaqueForte(Gargula_M, Alastor_G)

print(f"Vida atual do Alastor: {Alastor_G.get_vida()}")