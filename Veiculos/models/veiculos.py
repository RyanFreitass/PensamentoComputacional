class veiculos:
    def __init__(self, modelo, marca, placa, ano, cor, velocidade, latitude, longitude):
        self.modelo = modelo
        self.marca = marca
        self.placa = placa
        self.ano = ano
        self.cor = cor
        self.velocidade = velocidade
        self.latitude = latitude
        self.longitude = longitude

    def acelerar(self):
        self.velocidade += 10
        print(f"O carro de placa {self.placa} foi acelerado até {self.velocidade} km/h")

    def frear(self):
        if self.velocidade > 0:
            self.velocidade -= 10
            print(f"O carro de placa {self.placa} foi freado até {self.velocidade} km/h")
        else:
            print(f"O carro de placa {self.placa} está parado.")        

    def mostrarInfos(self):
        print(f"O veiculo {self.modelo}, de placa {self.placa} está a {self.velocidade} km/hr")
