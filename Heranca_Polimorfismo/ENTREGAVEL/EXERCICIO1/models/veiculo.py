class Veiculos:

    def __init__(self, placa: str, modelo: str, marca: str, ano: int, cor: str, valor_fipe: float) -> None:
        self.__placa = None
        self.set_placa(placa)
        self.modelo = modelo
        self.marca = marca
        self.ano = ano
        self.cor = cor
        self.valor_fipe = valor_fipe

    
    def __str__(self) -> str:
        infor = f"Placa: {self.__placa}\n"
        infor += f"Modelo: {self.modelo}\n"
        infor += f"Marca: {self.marca}\n"
        infor += f"Ano: {self.ano}\n"
        infor += f"Cor: {self.cor}\n"
        infor += f"Valor Fipe: {self.valor_fipe}\n"
        return infor
    
    def calcular_consumo(self, distancia):
        return distancia / self.__consumo 

    def get_placa(self) -> str:
        return self.__placa
    
    def set_placa(self, nova_placa):
        nova_placa = nova_placa.upper()
        if len(nova_placa) == 7:
            # Padrão antigo: ABC1234
            if nova_placa[:3].isalpha() and nova_placa[3:].isdigit():
                self.__placa = nova_placa
            # Padrão Mercosul: ABC1D23
            elif nova_placa[:3].isalpha() and nova_placa[3].isdigit() and nova_placa[4].isalpha() and nova_placa[5:].isdigit():
                self.__placa = nova_placa
            else:
                print("Placa inválida. Formato incorreto.")
        else:
            print("Placa inválida. Deve conter exatamente 7 caracteres.")

        

    def setValorFipe(self, valor):
        self.valor_fipe = valor
        return True
    
    def __eq__(self, other):
        if isinstance(other, Veiculos):
            return self.__placa == other.get_placa()
        else:
            return False
        