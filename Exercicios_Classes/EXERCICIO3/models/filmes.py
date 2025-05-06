class Filme:
    def __init__(self, titulo, genero, duracao, avaliacao):
        self.titulo = titulo
        self.genero = genero
        self.duracao = duracao
        self.avaliacao = avaliacao
    
    def avaliar(self, nota: float):
        if nota >= 0 and nota <= 10.0:
            self.avaliacao += nota
            print(f"A nota para o Filme: {self.titulo} recebeu nota {self.avaliacao}")
        else:
            print("Apenas Nota entre 0.0 e 10.0")

    def exibir_informações(self):
        if not self.avaliacao:
            print("Nenhuma nota válida adicionada!!!")
        else:
            print(f"Titulo Filme: {self.titulo}, Genero: {self.genero}, Duração: {self.duracao} minutos, Avaliação: {self.avaliacao}")
