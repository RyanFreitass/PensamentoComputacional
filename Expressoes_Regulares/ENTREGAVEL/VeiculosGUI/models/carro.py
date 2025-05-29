from models.veiculo import Veiculo


class Carro(Veiculo):
    def __init__(self, placa, marca, modelo, ano, num_portas):
        super().__init__(placa, marca, modelo, ano)
        self.__num_portas = num_portas
    
    def get_num_portas(self):
        return self.__num_portas
    
    def __str__(self):
        return f"Carro: {super().__str__()} - {self.__num_portas} portas"