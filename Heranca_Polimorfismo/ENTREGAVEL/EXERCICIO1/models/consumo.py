class Veiculos:
    def calcular_consumo(self, distancia):
        pass

class Carro(Veiculos):
    def calcular_consumo(self, distancia):
        eficiencia = 12
        consumo = distancia / eficiencia
        return consumo
    
class Moto(Veiculos):
    def calcular_consumo(self, distancia):
        eficiencia = 20
        consumo = distancia / eficiencia
        return consumo
    
class Caminhao(Veiculos):
    def calcular_consumo(self, distancia):
        eficiencia = 5
        consumo = distancia / eficiencia
        return consumo
