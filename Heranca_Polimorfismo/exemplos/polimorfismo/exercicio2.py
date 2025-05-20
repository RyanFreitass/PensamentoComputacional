class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def calcular_area(self):
        return self.largura * self.altura

class Triangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return (self.base * self.altura) / 2

def exibir_area(objeto):
    area = objeto.calcular_area()
    print(f"A área é: {area}")

r = Retangulo(10, 5)
t = Triangulo(8, 4)

exibir_area(r) 
exibir_area(t)
