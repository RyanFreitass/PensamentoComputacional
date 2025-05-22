from models.produto import Produto

class ConversorMoeda(Produto):
    
    def __init__(self):
        self.__dolar_real = 5.05 
        self.__euro_real = 6.14
        self.__euro_dolar = 1.22

    def converte_preco_para_usd(self, produto: Produto) -> bool:
        moeda_atual = produto.get_moeda()
        preco_atual = produto.get_preco()

        if moeda_atual == 'BRL':
            preco_novo = preco_atual / self.__dolar_real
        
        elif moeda_atual == 'EUR':
            preco_novo = preco_atual / self.__euro_dolar
        
        elif moeda_atual == 'USD':
            print("Moeda já esta em USD")
            return False
        
        else:
            return False
        
        produto.set_preco(preco_novo)
        produto.set_moeda('USD')
        return True
    
    def converte_preco_para_eur(self, produto: Produto) -> bool:
        moeda_atual = produto.get_moeda()
        preco_atual = produto.get_preco()

        if moeda_atual == 'BRL':
            preco_novo = preco_atual / self.__euro_real
        
        elif moeda_atual == 'USD':
            preco_novo = preco_atual * (1 / self.__euro_dolar)
        
        elif moeda_atual == 'EUR':
            print("Moeda já esta em EUR")
            return False
        
        else:
            return False
        
        produto.set_preco(preco_novo)
        produto.set_moeda('EUR')
        return True

    def converte_preco_para_brl(self, produto: Produto) -> bool:
        moeda_atual = produto.get_moeda()
        preco_atual = produto.get_preco()

        if moeda_atual == 'USD':
            preco_novo = preco_atual * self.__dolar_real
        
        elif moeda_atual == 'EUR':
            preco_novo = preco_atual * self.__euro_real
        
        elif moeda_atual == 'BRL':
            print("Moeda já esta em BRL")
            return False
        
        else:
            return False
        
        produto.set_preco(preco_novo)
        produto.set_moeda('BRL')
        return True