from models.livro import livros

class TesteLivro:
    def teste_livro(self):
        livro = livros("Harry Potter e a Pedra Filosofal", "J.K. Rowling", 1997, 264, 1)

        #avançar a página
        livro.avancar_pagina()

        #voltar pagina
        livro.voltar_pagina()

        #mostrar informações
        livro.exibir_informacoes()        