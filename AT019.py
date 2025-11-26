from AT017APOIO import Personagem

class Monstro(Personagem):
    
    # Este é o método "Fábrica"
    @classmethod
    def criar_goblin(cls):
        # Aqui definimos os atributos PADRÃO de todo Goblin
        return cls("Goblin", 50, 10)

    @classmethod
    def criar_chefao(cls):
        return cls("Rei Goblin", 200, 40)
    
    def esta_vivo(self):
        # Retorna True se a vida for maior que 0
        # Retorna False se for 0
        if self.get_vida() > 0:
            return True
        else:
            return False
    
monstro1 = Monstro.criar_goblin()
monstro2 = Monstro.criar_goblin()
monstro3 = Monstro.criar_goblin()
chefao = Monstro.criar_chefao()

print(f"Monstro 1: {monstro1.nome} | Vida: {monstro1.get_vida()}")
print(f"Chefe: {chefao.nome} | Vida: {chefao.get_vida()}")