import tkinter as tk

janela = tk.Tk()
janela.title("Exemplo Label")
janela.geometry("300x100")

rotulo = tk.Label(janela, text="Bem-vindo ao Tkinter!", font=("Arial", 16))
rotulo.pack(pady=20)

janela.mainloop()