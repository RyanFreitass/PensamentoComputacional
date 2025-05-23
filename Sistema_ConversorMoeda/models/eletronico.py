from models.produto import Produto

class ProdutoEletronico(Produto):

    def __str__(self):
        return f"[PRODUTO ELETRONICO]: {self.get_nome()}, {self.get_preco():.2f} ({self.get_moeda()})"