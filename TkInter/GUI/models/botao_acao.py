import tkinter as tk

def clique():
    rotulo.config(text="Botão pressionado!")

janela = tk.Tk()
janela.title("Exemplo Botão")
janela.geometry("300x150")

rotulo = tk.Label(janela, text="Clique no botão abaixo")
rotulo.pack(pady=10)

botao = tk.Button(janela, text="Clique Aqui", command=clique)
botao.pack(pady=10)

janela.mainloop()