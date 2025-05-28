import tkinter as tk

def mostrar_texto():
    texto = entrada.get()
    rotulo.config(text=f"Você digitou: {texto}")
    

janela = tk.Tk()
janela.title("Exemplo Entry")
janela.geometry("300x150")

entrada = tk.Entry(janela)
entrada.pack(pady=10)

botao = tk.Button(janela, text="Exibir", command=mostrar_texto)
botao.pack(pady=5)

rotulo = tk.Label(janela, text='')
rotulo.pack(pady=5)
janela.mainloop()
