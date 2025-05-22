from models.produto import Produto

class ProdutoAlimenticio(Produto):

    def __str__(self):
        return f"[PRODUTO ALIMENTICIO] {self.get_nome()}, {self.get_preco():.2f} ({self.get_moeda()})"