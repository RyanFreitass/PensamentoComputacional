from models.veiculo import Veiculos
from models.caminhao import Caminhao
from models.carro import Carro
from models.moto import Moto

class Frota:
    def __init__(self, veiculo):
        self.__frota = [veiculo]
    
    def adicionar_veiculo(self, veiculo):
        self.__frota.append(veiculo)

    def listar_veiculos(self):
        for veiculo in self.__frota:
            print(veiculo)
    
    def consumo_total(self, distancia):
        consumoTotal = 0
        for veiculo in self.__frota:
            consumoTotal += veiculo.calcular_consumo(distancia)
        return consumoTotal

    
