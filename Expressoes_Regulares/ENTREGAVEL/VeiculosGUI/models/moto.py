from models.veiculo import Veiculo

class Moto(Veiculo):
    def __init__(self, placa, marca, modelo, ano, cilindrada):
        super().__init__(placa, marca, modelo, ano)
        self.__cilindrada = cilindrada
    
    def get_cilindrada(self):
        return self.__cilindrada
    
    def __str__(self):
        return f"Moto: {super().__str__()} - {self.__cilindrada} cc"