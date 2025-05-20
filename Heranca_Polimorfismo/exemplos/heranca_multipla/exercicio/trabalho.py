class funcionario:
    def trabalhar(self):
        print("Trabalhando")
        
class Aluno:
    def estudar(self):
        print("Estudando")

class estagiario(funcionario, Aluno):
    pass

ryan = estagiario()
ryan.trabalhar()
ryan.estudar()
