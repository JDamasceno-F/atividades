class Inventario:
    def __init__(self):
        # Criamos uma lista vazia para guardar as coisas
        self.itens = []

    def adicionar_item(self, item):
        self.itens.append(item)
        try:
            print(f"📦 {item.nome} foi guardado na mochila.")
        except:
            print(f"📦 {item} foi guardado na mochila.")
             # Se for só texto, use print(f"{item} adicionado...")

    def listar_itens(self):
        print("\n--- 🎒 Conteúdo da Mochila ---")
        if len(self.itens) == 0:
            print("A mochila está vazia...")
        else:
            for item in self.itens:
                # Tenta mostrar o nome se for objeto, senão mostra o item direto
                try:
                    print(f"- {item.nome}")
                except:
                    print(f"- {item}")

from AT007 import Armas
from AT014APOIO import Cajado,Espada_longa,Arco
from AT008 import Porcao_de_cura,Porcoes

# Cria a mochila
minha_mochila = Inventario()

Coroa_1 = "Coroa de espinhos" #string

# Guarda os itens
minha_mochila.adicionar_item(Cajado)
minha_mochila.adicionar_item(Espada_longa)
minha_mochila.adicionar_item(Arco)
minha_mochila.adicionar_item(Coroa_1)

# Abre a mochila para ver
minha_mochila.listar_itens()