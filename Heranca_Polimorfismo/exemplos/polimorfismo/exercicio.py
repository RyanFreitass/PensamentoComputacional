class Veiculo:
    def mover(self):
        print("Mover o veiculo")

class Carro(Veiculo):
    def mover(self):
        print("Mover a 60km")

class Bicicleta(Veiculo):
    def mover(self):
        print("Mover a 20km")


veiculos = [Carro(), Bicicleta(), Veiculo()]

for veiculo in veiculos:
    veiculo.mover()