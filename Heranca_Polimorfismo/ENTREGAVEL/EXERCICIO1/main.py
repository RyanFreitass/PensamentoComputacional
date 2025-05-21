from models.veiculo import Veiculos
from models.caminhao import Caminhao
from models.carro import Carro
from models.moto import Moto
from models.frota import Frota
from models.VeiculoEletrico import VeiculoEletrico

spin = Carro("ABC1234", "Spin", "Chevrolet", 2019, "Prata", 91000, 7.3)
volvo = Caminhao("RTA3J62", "Volvo FH 540", "Volvo", 2020, "Branco", 620000, 2.5)
honda = Moto("Q2Y7B45", "Honda CG", "Honda", 2022, "Vermelha", 14800, 40)
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

'''lista = [
    Carro("IJS3F56", "Spin", "Chevrolet", 2019, "Prata", 91000, 7.3),
    Moto("QXY7B45", "Honda CG", "Honda", 2022, "Vermelha", 14800, 40),
    VeiculoEletrico("UEB4I83", "Tesla CyberTruck", "Tesla Inc.", 2023, "Prata", 550000, 0.15),
]

distancia = int(input("Digite a distancia percorrida em KM: "))
for veiculo in lista:
    consumo = veiculo.calcular_consumo(distancia)
    unidade = "kWh" if isinstance(veiculo, VeiculoEletrico) else "litros"
    print(f"O consumo do {veiculo.modelo} é de {consumo:.2f} {unidade}")

#RECARREGAR
placa = input("Digite a placa do veiculo que deseja recarregar: ")
for veiculo in lista:
    if veiculo.placa == placa:
        if isinstance(veiculo, VeiculoEletrico):
            veiculo.recarregar()
        else:
            print(f"{veiculo.modelo} não é um veiculo eletrico")'''

#PLACA
'''print("Placa inicial: ", spin.get_placa())

honda.set_placa("Q2Y7B98")
print("Placa alterada: ", honda.get_placa())'''

veiculos = [
    Carro("ABC1234", "Spin", "Chevrolet", 2019, "Prata", 91000, 7.3),
    Moto("Q2Y7B45", "Honda CG", "Honda", 2022, "Vermelha", 14800, 40),
    VeiculoEletrico("UEB4I83", "Tesla CyberTruck", "Tesla Inc.", 2023, "Prata", 550000, 0.15),
    Carro("ABC1234", "Onix", "Chevrolet", 2021, "Preto", 80000, 6.5),  
    Moto("Q2Y7B45", "Yamaha XTZ", "Yamaha", 2020, "Azul", 12000, 38), 
    VeiculoEletrico("XYZ9876", "Nissan Leaf", "Nissan", 2021, "Branco", 180000, 0.12)
]

# Verificando veículos duplicados pela placa
print("Veículos duplicados (pela placa):")
for i in range(len(veiculos)):
    for j in range(i+1, len(veiculos)):
        if veiculos[i] == veiculos[j]:
            print(f"{veiculos[i].modelo} (placa {veiculos[i].get_placa()}) é igual a {veiculos[j].modelo} (placa {veiculos[j].get_placa()})")