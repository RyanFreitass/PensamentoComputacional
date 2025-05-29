from models.veiculo import Veiculo

class Caminhao(Veiculo):
    def __init__(self, placa, marca, modelo, ano, capacidade_carga):
        super().__init__(placa, marca, modelo, ano)
        self.__capacidade_carga = capacidade_carga
    
    def get_capacidade_carga(self):
        return self.__capacidade_carga
    
    def __str__(self):
        return f"Caminhão: {super().__str__()} - Carga: {self.__capacidade_carga} kg"