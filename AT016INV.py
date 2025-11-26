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