import tkinter as tk

janela = tk.Tk()
janela.title("Layout Grid")

tk.Label(janela, text="Usuário:").grid(row=0, column=0, padx=5, pady=5)
tk.Entry(janela).grid(row=0, column=1, padx=5, pady=5)
tk.Label(janela, text="Senha:").grid(row=1, column=0, padx=5, pady=5)
tk.Entry(janela, show="*").grid(row=1, column=1, padx=5, pady=5)
tk.Button(janela, text="Entrar").grid(row=2, column=0, columnspan=2, pady=10)

janela.mainloop()