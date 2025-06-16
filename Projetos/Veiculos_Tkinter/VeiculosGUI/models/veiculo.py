class Veiculo:
    def __init__(self, placa, marca, modelo, ano):
        self.__placa = placa
        self.__marca = marca
        self.__modelo = modelo
        self.__ano = ano
    
    def get_placa(self):
        return self.__placa
        
    def get_marca(self):
        return self.__marca
        
    def get_modelo(self):
        return self.__modelo
        
    def get_ano(self):
        return self.__ano
    
    def __str__(self):
        return f"{self.__marca} {self.__modelo} ({self.__ano}) - Placa: {self.__placa}"