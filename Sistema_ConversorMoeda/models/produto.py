class Produto:
    def __init__(self, nome: str, preco: float, moeda: str = 'BRL'):
        self.nome = nome
        self.preco = preco
        self.moeda = moeda
    
    def __str__(self):
        return f"Produto(nome={self.nome}, preco={self.preco:.2f} {self.moeda})"
    
    def get_nome(self):
        return self.nome
    
    def set_nome(self, nome: str):
        self.nome = nome
    
    def get_preco(self):
        return self.preco
    
    def set_preco(self, preco: float):
        self.preco = preco
    
    def get_moeda(self):
        return self.moeda
    
    def set_moeda(self, moeda: str):
        self.moeda = moeda
    
