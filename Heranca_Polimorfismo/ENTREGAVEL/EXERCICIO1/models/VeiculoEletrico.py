from models.veiculo import Veiculos
from models.caminhao import Caminhao
from models.carro import Carro
from models.moto import Moto
from models.frota import Frota

class VeiculoEletrico(Veiculos):

    def calcular_consumo(self, distancia):
        return distancia / self.__consumo
    
    def recarregar(self):
        print(f"{self.placa} está sendo carregada!!!")

