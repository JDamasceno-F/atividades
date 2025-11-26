from AT017APOIO import Personagem

class Mago(Personagem):
    def __init__(self,nome,vida,força,mana,arma):
        super().__init__(nome, vida, força)
        self.mana = mana
        self.arma = arma
    # ESTE MÉTODO SUBSTITUI O "ATACAR" DO PAI
    def atacar(self, alvo):
        # O dano do mago usa INTELIGÊNCIA/MANA em vez de só força
        # (Ajuste 'self.mana' se o nome do seu atributo for outro)
        dano = self.força + self.mana 
        
        print(f"🔥 {self.nome} lança uma BOLA DE FOGO em {alvo.nome}!")
        print(f"--> Dano Mágico: {dano}")
        
        # Chama o método de receber dano do alvo
        alvo.receber_dano(dano)

class Arqueiro(Personagem):
    def __init__(self,nome,vida,força,mira,arma):
        super().__init__(nome, vida, força)
        self.mira = mira
        self.arma = arma
    def atacar(self, alvo):
        # O dano do arqueiro soma a MIRA (precisão)
        dano = self.força + self.mira
        
        print(f"🏹 {self.nome} dispara uma flecha precisa em {alvo.nome}!")
        print(f"--> Dano de Precisão: {dano}")
        
        alvo.receber_dano(dano)

# 1. Cria os lutadores (NOVOS, para evitar erro de versão antiga)
# (Ajuste os números conforme seu __init__: nome, vida, forca, atributo_especial, arma)
Merlin = Mago("Merlin", 100, 10, 50, "Cajado") 
Legolas = Arqueiro("Legolas", 100, 15, 40, "Arco")
Ogro = Personagem("Ogro Feio", 200, 20) # Alvo genérico

# 2. Testando o ataque do Mago
print("\n--- Turno do Mago ---")
Merlin.atacar(Ogro) 
# Deve aparecer "BOLA DE FOGO" e usar a soma da mana

# 3. Testando o ataque do Arqueiro
print("\n--- Turno do Arqueiro ---")
Legolas.atacar(Ogro)
# Deve aparecer "FLECHA PRECISA" e usar a soma da mira