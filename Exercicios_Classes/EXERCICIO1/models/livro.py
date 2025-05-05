class Livro:
    def __init__(self, titulo, autor, ano_publicacao, numero_paginas, pagina_atual):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.numero_paginas = numero_paginas
        self.pagina_atual = 0
    
    def avancar_pagina(self):
        if self.pagina_atual > self.numero_paginas:
            print("Número de Páginas ultrapassadas")
        else:
            self.pagina_atual += 1
            print(f"Você está na página {self.pagina_atual} do livro {self.titulo}")
        
    def voltar_pagina(self):
        if self.pagina_atual < 1:
            print("Número de Páginas ultrapassadas")
        else:
            self.pagina_atual -= 1
            print(f"Você está na página {self.pagina_atual} do livro {self.titulo}")

    def exibir_informacoes(self):
        print(f"Livro: {self.titulo}, Autor: {self.autor}, Ano de Publicação: {self.ano_publicacao}, Número de Páginas: {self.numero_paginas}, Página Atual: {self.pagina_atual}")
