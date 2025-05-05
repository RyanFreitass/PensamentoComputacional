from models.livro import Livro

livro = Livro("Harry Potter e a Pedra Filosofal", "J.K. Rowling", 1997, 264, 1)

#avançar 4 paginas do livro
livro.avancar_pagina()
livro.avancar_pagina()
livro.avancar_pagina()
livro.avancar_pagina()

#voltar 1 pagina do livro
livro.voltar_pagina()

#exibir informações do livro
livro.exibir_informacoes()
