class Pessoa:
    def __init__(self, nome, idade, altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura
    
    def aniversario(self):
        self.idade += 1
        print(f"{self.nome} fez aniversario e agora está com {self.idade} anos")
    
    def crescer(self, valor: float):
        print(f"{self.nome} tinha {self.altura} metros")
        if valor > 0:
            self.altura += valor
            print(f"{self.nome} tem atualmente {self.altura:.2f} metros. Cresceu {valor:.2f} metros")
        else:
            print("Valor deve ser positivo")

    def exibir_informacoes(self):
        print(f"Nome: {self.nome}, Idade: {self.idade} anos, Altura: {self.altura} metros")
