from models.veiculo import Veiculos

class Carro(Veiculos):  
    def __init__(self, placa, modelo, marca, ano, cor, valor_fipe, consumo: int):

        super().__init__(placa, modelo, marca, ano, cor, valor_fipe)
        self.__consumo = consumo
    
    def calcular_consumo(self, distancia):
        return distancia / self.__consumo 

    def __str__(self):
        infos = super().__str__()
        infos += f'Consumo: {self.__consumo} km/l'
        return infos