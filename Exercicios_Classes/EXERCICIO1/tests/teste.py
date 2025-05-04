import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.livro import Livro

class TesteLivro:
    def teste_livro(self):
        livro = Livro("Harry Potter e a Pedra Filosofal", "J.K. Rowling", 1997, 264, 1)

        #avançar a página
        livro.avancar_pagina()

        #voltar pagina
        livro.voltar_pagina()

        #mostrar informações
        livro.exibir_informacoes()        