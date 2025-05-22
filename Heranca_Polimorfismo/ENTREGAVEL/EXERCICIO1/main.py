from models.veiculo import Veiculos
from models.caminhao import Caminhao
from models.carro import Carro
from models.moto import Moto
from models.frota import Frota
from models.VeiculoEletrico import VeiculoEletrico
from utils.erros import *


spin = Carro("ABC1234", "Spin", "Chevrolet", 2019, "Prata", 91000, 7.3)
volvo = Caminhao("RTA3J62", "Volvo FH 540", "Volvo", 2020, "Branco", 620000, 2.5)
honda = Moto("Q2Y7B45", "Honda CG", "Honda", 2022, "Vermelha", 14800, 40)
tesla = VeiculoEletrico("UEB4I83", "Tesla CyberTruck", "Tesla Inc.", 2023, "Prata", 550000, 0.15)


#PRIMEIRO TESTE DE CALCULAR CONSUMO
print(spin)
distancia = int(input("Digite a distancia percorrida: "))
spin.calcular_consumo(distancia)
print(spin)


#FROTA
frota = Frota(spin)

frota.adicionar_veiculo(spin)
frota.adicionar_veiculo(spin)

distancia = int(input("Digite a distancia percorrida em KM: "))
print(f"O consumo total da frota é de {frota.consumo_total(distancia):.2f}")


#VEICULO ELETRICO
lista = [
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
            print(f"{veiculo.modelo} não é um veiculo eletrico")

#PLACA
print("Placa inicial: ", spin.get_placa())

honda.set_placa("Q2Y7B98")
print("Placa alterada: ", honda.get_placa())


#COMPARAR VEICULOS
veiculos = [
    Carro("ABC1234", "Spin", "Chevrolet", 2019, "Prata", 91000, 7.3),
    Moto("ABC1D23", "Honda CG", "Honda", 2022, "Vermelha", 14800, 40),
    VeiculoEletrico("ABC1D23", "Tesla CyberTruck", "Tesla Inc.", 2023, "Prata", 550000, 0.15),
    Carro("ABC1234", "Onix", "Chevrolet", 2021, "Preto", 80000, 6.5),  
    Moto("ABC1D23", "Yamaha XTZ", "Yamaha", 2020, "Azul", 12000, 38), 
]
# Verificando veículos duplicados pela placa
print("Veículos duplicados (pela placa):")
for a in range(len(veiculos)):
    for b in range(a+1, len(veiculos)):
        if veiculos[a] == veiculos[b]:
            print(f"{veiculos[a].modelo} (placa {veiculos[a].get_placa()}) é igual a {veiculos[b].modelo} (placa {veiculos[b].get_placa()})")

#DISTANCIA [ERRO]
try:
    distancia = float(input("Digite a distancia: "))
    if distancia < 0:
        raise DistanciaNegativa("Distancia Negativa não é permitida!!")
except ValueError as erro:
    print(f"Erro: {erro}")
except DistanciaNegativa as erro:
    print(f"Erro: {erro}")

#DISTANCIA EXCEDIDA [ERRO]
try: 
    distancia = float(input("Digite a distancia [EXCEDIDA]: "))
    if distancia > 100:
        raise DistanciaExcedida("Distancia Maxima excedida ")
except ValueError as erro:
    print(f"Erro: {erro}")
except DistanciaExcedida as erro:
    print(f"Erro: {erro}")


#TIPO VEICULO [ERRO]
try:
    veiculo = input("Digite o tipo de veiculo: ")
    tipos_veiculo = ["carro", "moto", "caminhao"]
    if veiculo not in tipos_veiculo:
        raise TipoVeiculo("Tipo de veiculo incorreto!!!")
        
except ValueError as erro:
    print(f"Erro: {erro}")
except TipoVeiculo as erro:
    print(f"Erro: {erro}")


#PLACA INVALIDA [ERRO]
try:
    placas = []
    placa = input("Digite a sua placa por gentileza: ").upper
    placas.append(placa)
    for i in placas:
        if len(placas) == 7:
            if placas[:3].isaplha() and placas[3:].isdigit():
                print(f"a placa {placa} é válida ao padrão Brasileiro:")
            else:
                raise PlacaInvalida("Placa inválida ao padrão Brasileiro [4 LETRAS | 3 NUMEROS]")
        else:
            print("PLACA INVÁLIDA, 7 CARACTERES NO MÁXIMO")
except ValueError as erro:
    print(f"Erro: {erro}")


#FROTA CONSUMO [ERRO]
lista_veiculos = [
    Carro("IJS3F56", "Spin", "Chevrolet", 2019, "Prata", 91000, 7.3),
    Moto("QXY7B45", "Honda CG", "Honda", 2022, "Vermelha", 14800, 40),
    VeiculoEletrico("UEB4I83", "Tesla CyberTruck", "Tesla Inc.", 2023, "Prata", 550000, 0.15),
]

try:
    distancia = float(input("Digite a distancia percorrida: "))
    if distancia < 0:
        raise ValueError("Distância negativa não é permitida!")
    for veiculo in lista_veiculos:
        consumo = veiculo.calcular_consumo(distancia)
        print(f"{veiculo.modelo} com placa {veiculo.get_placa()} tem o consumo {consumo: .2f}")
except ValueError as erro:
    print(f"Erro: {erro}")
except FrotaConsumo as erro:
    print(f"Erro: {erro}")
