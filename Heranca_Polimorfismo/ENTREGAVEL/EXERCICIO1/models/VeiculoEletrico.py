from models.veiculo import Veiculos
from models.caminhao import Caminhao
from models.carro import Carro
from models.moto import Moto
from models.frota import Frota

class VeiculoEletrico(Veiculos):
    def __init__(self, placa, modelo, fabricante, ano, cor, valor, consumokwh):
        super().__init__(placa, modelo, fabricante, ano, cor, valor)
        self.consumokwh = consumokwh

    def calcular_consumo(self, distancia):
        return distancia * 0.15
    
    def recarregar(self):
        print(f"{self.modelo} está sendo carregada!!!")

