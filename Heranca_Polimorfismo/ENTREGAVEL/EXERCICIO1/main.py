from models.veiculo import Veiculos
from models.caminhao import Caminhao
from models.carro import Carro
from models.moto import Moto
from models.frota import Frota
from models.VeiculoEletrico import VeiculoEletrico

spin = Carro("IJS3F56", "Spin", "Chevrolet", 2019, "Prata", 91000, 7.3)
volvo = Caminhao("RTA3J62", "Volvo FH 540", "Volvo", 2020, "Branco", 620000, 2.5)
honda = Moto("QXY7B45", "Honda CG", "Honda", 2022, "Vermelha", 14800, 40)
tesla = VeiculoEletrico("UEB4I83", "Tesla CyberTruck", "Tesla Inc.", 2023, "Prata", 550000, 0.15)

'''print(spin)
distancia = int(input("Digite a distancia percorrida: "))
spin.calcular_consumo(distancia)
print(spin)
'''
'''frota = Frota(spin)

frota.adicionar_veiculo(spin)
frota.adicionar_veiculo(spin)

distancia = int(input("Digite a distancia percorrida em KM: "))
print(f"O consumo total da frota é de {frota.consumo_total(distancia):.2f}")'''

lista = []
lista.append(spin)
lista.append(honda)
lista.append(tesla)
