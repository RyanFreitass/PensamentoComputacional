from models.alimenticio import ProdutoAlimenticio
from models.conversor import ConversorMoeda
from models.eletronico import ProdutoEletronico
from models.produto import Produto
from utils.erros import *

alimenticio = ProdutoAlimenticio("Arroz 1KG", 10, 'USD')
eletronico = ProdutoEletronico("Mouse Razer", 219.00, 'EUR')

conversor = ConversorMoeda()

conversor.converte_preco_para_brl(alimenticio)
print(alimenticio)


try:
    nome = input("Digite o nome do produto: ")
    preco = float(input(f"Digite o preço do produto [{nome}]: "))
    if preco == str or preco <= 0:
        raise ValueError
    tipo = input("Digite o tipo do produto [ALIMENTICIO | ELETRONICO]: ").upper()
    if tipo not in ["ALIMENTICIO", "ELETRONICO"]:
        raise TipoProdutoError("Tipo de Produto inválido!!!")
    moeda = input("Digite o tipo da moeda [BRL | USD | EUR | GBP]: ").upper()
    if moeda not in ["BRL", "USD", "EUR", "GBP"]:
        raise MoedaInvalidaError("Moeda Inválida!!!!")

    if tipo == 'ALIMENTICIO':
        produto = ProdutoAlimenticio(nome, preco, moeda)
            
    elif tipo == 'ELETRONICO':
        produto = ProdutoEletronico(nome, preco, moeda)

    else:
        print("Tipo de produto Inválido!!!")
        exit()
    
    #CONVERTER MOEDA
    conversor = ConversorMoeda()

    try:
        resposta = input("Deseja converter o produto? [SIM | NAO]: ").upper()
        if resposta == 'SIM':
            moeda_conversor = input("Digite a moeda que deseja para converter o preço [BRL | USD | EUR | GBP]: ").upper()
            if moeda_conversor == 'BRL':
                if conversor.converte_preco_para_brl(produto):
                    print("Realizado com Sucesso!!!")
                else:
                    print("Erro ao converter!!!")

            elif moeda_conversor == 'USD':
                if conversor.converte_preco_para_usd(produto):
                    print("Realizado com Sucesso!!!")
                else:
                    print("Erro ao converter!!!")
            
            elif moeda_conversor == 'EUR':
                if conversor.converte_preco_para_eur(produto):
                    print("Realizado com Sucesso!!!")
                else:
                    print("Erro ao converter!!!")
            
            elif moeda_conversor == 'GBP':
                if conversor.converte_preco_para_gbp(produto):
                    print("Realizado com Sucesso!!!")
                else:
                    print("Erro ao converter!!!")

            else:
                raise MoedaInvalidaError("Moeda Inválida!!!!")
                exit()
        else:
            exit()

    except MoedaInvalidaError as erro:
        print(f"Erro: {erro}")

    print(produto)

except ValueError:
    print("Erro: preço deve ser um número válido (negativo ou não númerico).")
except MoedaInvalidaError as erro:
    print(f"Erro: {erro}")
except TipoProdutoError as erro:
    print(f"Erro: {erro}")
