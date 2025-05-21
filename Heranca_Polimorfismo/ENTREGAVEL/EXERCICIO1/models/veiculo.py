class Veiculos:

    def __init__(self, placa: str, modelo: str, marca: str, ano: int, cor: str, valor_fipe: float) -> None:
        self.placa = placa
        self.modelo = modelo
        self.marca = marca
        self.ano = ano
        self.cor = cor
        self.valor_fipe = valor_fipe

    
    def __str__(self) -> str:
        infor = f"Placa: {self.placa}\n"
        infor += f"Modelo: {self.modelo}\n"
        infor += f"Marca: {self.marca}\n"
        infor += f"Ano: {self.ano}\n"
        infor += f"Cor: {self.cor}\n"
        infor += f"Valor Fipe: {self.valor_fipe}\n"
        return infor
    
    def calcular_consumo(self, distancia):
        return distancia / self.__consumo 

    def getPlaca(self) -> str:
        return self.__placa
    
    def setValorFipe(self, valor):
        self.__valor_fipe = valor
        return True
    
    def __eq__(self, other):
        if isinstance(other, Veiculos):
            return self.placa == other.getPlaca()
        else:
            return False
        