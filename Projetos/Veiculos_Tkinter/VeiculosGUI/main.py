from models.carro import Carro
from models.moto import Moto
from models.caminhao import Caminhao
from models.proprietario import Proprietario
from utils.erros import *
import tkinter as tk
from tkinter import ttk, messagebox
import re
from datetime import datetime

# Classe principal
class SistemaVeiculos:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Cadastro de Veículos")
        self.root.geometry("1000x800")
        self.root.resizable(True, True)
        
        # Lista para armazenar os veículos cadastrados
        self.veiculos = []

        #Lista para armazenar os proprietarios
        self.proprietarios = []
        
        # Configura o container para as telas
        self.container = tk.Frame(root)
        self.container.pack(fill="both", expand=True)
        
        # Configura o grid do container
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)
        
        # Criar as telas
        self.tela_principal = tk.Frame(self.container)
        self.tela_cadastro = tk.Frame(self.container)
        self.cadastro_proprietario = tk.Frame(self.container)
        self.listar_proprietario =  tk.Frame(self.container)
        self.tela_listagem = tk.Frame(self.container)
        
        # Posiciona as telas no mesmo local
        for tela in (self.tela_principal, self.tela_cadastro, self.cadastro_proprietario, self.listar_proprietario, self.tela_listagem):
            tela.grid(row=0, column=0, sticky="nsew")
        
        # Configura cada tela
        self.configurar_tela_principal()
        self.configurar_tela_cadastro()
        self.configurar_tela_cadastro_proprietario()
        self.configurar_tela_listar_proprietario()
        self.configurar_tela_listagem()
        
        # Mostrar a tela principal
        self.mostrar_tela(self.tela_principal)
    
    def mostrar_tela(self, tela):
        if tela == self.listar_proprietario:
            self.atualizar_listagem_proprietarios()
        tela.tkraise()
    
    def configurar_tela_principal(self):
        # Frame principal
        frame = tk.Frame(self.tela_principal, padx=20, pady=20)
        frame.place(relx=0.5, rely=0.5, anchor="center")
        
        # Título
        titulo = tk.Label(frame, text="SISTEMA DE CADASTRO DE VEÍCULOS", font=("Arial", 16, "bold"))
        titulo.pack(pady=(0, 30))
        
        # Botões
        btn_cadastrar = tk.Button(frame, text="Cadastrar Novo Veículo", width=25, height=2,
                                 command=lambda: self.mostrar_tela(self.tela_cadastro))
        btn_cadastrar.pack(pady=10)
        
        btn_listar = tk.Button(frame, text="Listar Veículos", width=25, height=2,
                              command=lambda: self.mostrar_tela(self.tela_listagem))
        btn_listar.pack(pady=10)

        btn_cadastrar_proprietario = tk.Button(frame, text="Cadastrar Proprietario", width=25, height=2,
                                               command=lambda: self.mostrar_tela(self.cadastro_proprietario))
        btn_cadastrar_proprietario.pack(pady=10)
        
        btn_listar_proprietario = tk.Button(frame, text="Listar Proprietários", width=25, height=2,
                                    command=lambda: [self.atualizar_listagem_proprietarios(), self.mostrar_tela(self.listar_proprietario)])
        btn_listar_proprietario.pack(pady=10)

        btn_sair = tk.Button(frame, text="Sair", width=25, height=2,
                           command=self.root.quit)
        btn_sair.pack(pady=10)
    
    def configurar_tela_cadastro(self):
        # Título
        titulo = tk.Label(self.tela_cadastro, text="CADASTRO DE VEÍCULO", font=("Arial", 16, "bold"))
        titulo.pack(pady=20)
        
        # Frame para o formulário
        form_frame = tk.Frame(self.tela_cadastro, padx=20)
        form_frame.pack(fill="both")
        
        # Campos comuns
        tk.Label(form_frame, text="Placa:").grid(row=0, column=0, sticky="e", pady=5)
        self.placa_entry = tk.Entry(form_frame, width=15)
        self.placa_entry.grid(row=0, column=1, sticky="w", pady=5)
        
        tk.Label(form_frame, text="Marca:").grid(row=1, column=0, sticky="e", pady=5)
        self.marca_entry = tk.Entry(form_frame, width=20)
        self.marca_entry.grid(row=1, column=1, sticky="w", pady=5)
        
        tk.Label(form_frame, text="Modelo:").grid(row=2, column=0, sticky="e", pady=5)
        self.modelo_entry = tk.Entry(form_frame, width=20)
        self.modelo_entry.grid(row=2, column=1, sticky="w", pady=5)
        
        tk.Label(form_frame, text="Ano:").grid(row=3, column=0, sticky="e", pady=5)
        self.ano_entry = tk.Entry(form_frame, width=6)
        self.ano_entry.grid(row=3, column=1, sticky="w", pady=5)
        
        # Seletor de tipo de veículo
        tk.Label(form_frame, text="Tipo:").grid(row=4, column=0, sticky="e", pady=5)
        self.tipo_var = tk.StringVar(value="Carro")
        
        tipo_frame = tk.Frame(form_frame)
        tipo_frame.grid(row=4, column=1, sticky="w", pady=5)
        
        tk.Radiobutton(tipo_frame, text="Carro", variable=self.tipo_var, value="Carro",
                     command=self.mostrar_campos_especificos).pack(side="left")
        tk.Radiobutton(tipo_frame, text="Moto", variable=self.tipo_var, value="Moto",
                     command=self.mostrar_campos_especificos).pack(side="left")
        tk.Radiobutton(tipo_frame, text="Caminhão", variable=self.tipo_var, value="Caminhao",
                     command=self.mostrar_campos_especificos).pack(side="left")
        
        # Frame para campos específicos
        self.campos_especificos_frame = tk.Frame(form_frame)
        self.campos_especificos_frame.grid(row=5, column=0, columnspan=2, pady=10)
        
        # Campos específicos para Carro
        self.frame_carro = tk.Frame(self.campos_especificos_frame)
        tk.Label(self.frame_carro, text="Número de Portas:").pack(side="left")
        self.portas_entry = tk.Entry(self.frame_carro, width=5)
        self.portas_entry.pack(side="left", padx=5)
        
        # Campos específicos para Moto
        self.frame_moto = tk.Frame(self.campos_especificos_frame)
        tk.Label(self.frame_moto, text="Cilindrada (cc):").pack(side="left")
        self.cilindrada_entry = tk.Entry(self.frame_moto, width=7)
        self.cilindrada_entry.pack(side="left", padx=5)
        
        # Campos específicos para Caminhão
        self.frame_caminhao = tk.Frame(self.campos_especificos_frame)
        tk.Label(self.frame_caminhao, text="Capacidade de Carga (kg):").pack(side="left")
        self.capacidade_entry = tk.Entry(self.frame_caminhao, width=10)
        self.capacidade_entry.pack(side="left", padx=5)
        
        # Mostrar os campos iniciais (Carro)
        self.mostrar_campos_especificos()
        
        # Botões de ação
        botoes_frame = tk.Frame(self.tela_cadastro)
        botoes_frame.pack(pady=20)
        
        tk.Button(botoes_frame, text="Cancelar", width=10,
                command=lambda: self.mostrar_tela(self.tela_principal)).pack(side="left", padx=10)
        
        tk.Button(botoes_frame, text="Salvar", width=10,
                command=self.salvar_veiculo).pack(side="left", padx=10)
    
    def mostrar_campos_especificos(self):
        # Esconder todos os frames de campos específicos
        self.frame_carro.pack_forget()
        self.frame_moto.pack_forget()
        self.frame_caminhao.pack_forget()
        
        # Mostrar apenas o frame correspondente ao tipo selecionado
        tipo = self.tipo_var.get()
        if tipo == "Carro":
            self.frame_carro.pack()
        elif tipo == "Moto":
            self.frame_moto.pack()
        elif tipo == "Caminhao":
            self.frame_caminhao.pack()


    def configurar_tela_cadastro_proprietario(self):
        # Titulo
        titulo = tk.Label(self.cadastro_proprietario, text="CADASTRO DE PROPRIETARIOS", font=("Arial", 16, "bold"))
        titulo.pack(pady=20)

        # Frame
        filtro_frame = tk.Frame(self.cadastro_proprietario)
        filtro_frame.pack(fill="x", padx=20, pady=5)


        tk.Label(filtro_frame, text="Nome:").grid(row=0, column=0, sticky="e", pady=5)
        self.nome_entry = tk.Entry(filtro_frame, width=15)
        self.nome_entry.grid(row=0, column=1, sticky="w", pady=5)
        
        tk.Label(filtro_frame, text="CPF:").grid(row=1, column=0, sticky="e", pady=5)
        self.cpf_entry = tk.Entry(filtro_frame, width=20)
        self.cpf_entry.grid(row=1, column=1, sticky="w", pady=5)
        
        tk.Label(filtro_frame, text="Placa:").grid(row=2, column=0, sticky="e", pady=5)
        self.placa_proprietario_entry = tk.Entry(filtro_frame, width=20)
        self.placa_proprietario_entry.grid(row=2, column=1, sticky="w", pady=5)

        # BOTOES AÇÃO
        botoes_frame_proprietario = tk.Frame(self.cadastro_proprietario)
        botoes_frame_proprietario.pack(pady=20)
        
        tk.Button(botoes_frame_proprietario, text="Cancelar", width=10,
                command=lambda: self.mostrar_tela(self.tela_principal)).pack(side="left", padx=10)
        
        tk.Button(botoes_frame_proprietario, text="Salvar", width=10,
                command=self.salvar_proprietario).pack(side="left", padx=10)
        

        

    def configurar_tela_listagem(self):
        # Título
        titulo = tk.Label(self.tela_listagem, text="VEÍCULOS CADASTRADOS", font=("Arial", 16, "bold"))
        titulo.pack(pady=20)
        
        # Frame para filtro
        filtro_frame = tk.Frame(self.tela_listagem)
        filtro_frame.pack(fill="x", padx=20, pady=5)
        
        tk.Label(filtro_frame, text="Filtrar por tipo:").pack(side="left")
        self.filtro_var = tk.StringVar(value="Todos")
        filtro_combo = ttk.Combobox(filtro_frame, textvariable=self.filtro_var, 
                                  values=["Todos", "Carro", "Moto", "Caminhão"], width=15)
        filtro_combo.pack(side="left", padx=5)
        
        filtro_btn = tk.Button(filtro_frame, text="Filtrar", command=self.filtrar_veiculos)
        filtro_btn.pack(side="left", padx=5)
        
        # Frame para a lista
        lista_frame = tk.Frame(self.tela_listagem, padx=20)
        lista_frame.pack(fill="both", expand=True, pady=10)
        
        # Scrollbar
        scrollbar = tk.Scrollbar(lista_frame)
        scrollbar.pack(side="right", fill="y")
        
        # Listbox
        self.listbox = tk.Listbox(lista_frame, width=70, height=10, font=("Arial", 10))
        self.listbox.pack(side="left", fill="both", expand=True)
        
        # Configura scrollbar
        self.listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.listbox.yview)
        
        # Botões
        botoes_frame = tk.Frame(self.tela_listagem)
        botoes_frame.pack(pady=15)
        
        tk.Button(botoes_frame, text="Ver Detalhes", width=12,
                command=self.ver_detalhes).pack(side="left", padx=5)
        
        tk.Button(botoes_frame, text="Voltar", width=12,
                command=lambda: self.mostrar_tela(self.tela_principal)).pack(side="left", padx=5)
        

    def configurar_tela_listar_proprietario(self):
        # Título
        titulo = tk.Label(self.listar_proprietario, text="PROPRIETÁRIOS CADASTRADOS", font=("Arial", 16, "bold"))
        titulo.pack(pady=20)
        # Frame para filtro
        filtro_frame = tk.Frame(self.listar_proprietario)
        filtro_frame.pack(fill="x", padx=20, pady=5)
        tk.Label(filtro_frame, text="Filtrar por nome:").grid(row=0, column=0, sticky="e", pady=5)
        self.filtro_var_proprietario = tk.StringVar(value="Todos")
        self.filtro_combo = ttk.Combobox(filtro_frame, textvariable=self.filtro_var_proprietario,
                                    values=["Todos"] + [p.get_nome() for p in self.proprietarios], width=20)
        self.filtro_combo.grid(row=0, column=1, sticky="w", pady=5)
        

        filtro_btn = tk.Button(filtro_frame, text="Filtrar", command=self.filtrar_proprietario) 
        filtro_btn.grid(row=0, column=2, padx=5, pady=5)
        # Frame para a lista
        lista_frame = tk.Frame(self.listar_proprietario, padx=20)
        lista_frame.pack(fill="both", expand=True, pady=10)
        # Scrollbar
        scrollbar = tk.Scrollbar(lista_frame)
        scrollbar.pack(side="right", fill="y")
        # Listbox
        self.listbox_proprietario = tk.Listbox(lista_frame, width=70, height=10, font=("Arial", 10))
        self.listbox_proprietario.pack(side="left", fill="both", expand=True)
        # Configura scrollbar
        self.listbox_proprietario.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.listbox_proprietario.yview)
        # Botões
        botoes_frame = tk.Frame(self.listar_proprietario)
        botoes_frame.pack(pady=15)
        tk.Button(botoes_frame, text="Ver Detalhes", width=12,
                command=self.ver_detalhes_proprietario).pack(side="left", padx=5)
        tk.Button(botoes_frame, text="Voltar", width=12,
                command=lambda: self.mostrar_tela(self.tela_principal)).pack(side="left", padx=5)


    def salvar_proprietario(self):
        nome = self.nome_entry.get().strip()
        cpf = self.cpf_entry.get().strip()
        placa = self.placa_proprietario_entry.get().strip().upper()

        # Campos obrigatórios
        if not nome or not cpf or not placa:
            messagebox.showwarning("Dados incompletos", "Preencha todos os campos obrigatórios!")
            return

        # Verificar se a placa existe em algum veículo cadastrado
        if not any(veiculo.get_placa() == placa for veiculo in self.veiculos):
            messagebox.showwarning("Placa não encontrada", "Cadastre primeiro o veículo com essa placa.")
            return

        # Validar CPF
        if not re.match(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$', cpf):
            messagebox.showwarning("CPF inválido", "O CPF deve ser digitado corretamente")
            return

        # Verificar se o CPF já está cadastrado
        if any(p.get_cpf() == cpf for p in self.proprietarios):
            messagebox.showwarning("CPF já cadastrado", "Já existe um proprietário com esse CPF.")
            return
        
        # Validar placa
        if not re.match(r'^[A-Z]{3}[0-9][0-9A-Z][0-9]{2}$', placa):
            messagebox.showwarning("Placa inválida", "A placa deve seguir o padrão ABC1234 ou ABC1D23")
            return
        
        
        # Criar o proprietário
        proprietario = Proprietario(nome, cpf, [placa])
        # Adicionar o proprietário à lista
        self.proprietarios.append(proprietario)
        messagebox.showinfo("Sucesso", "Proprietário cadastrado com sucesso!")
        # Limpar campos
        self.nome_entry.delete(0, "end")
        self.cpf_entry.delete(0, "end")
        self.placa_proprietario_entry.delete(0, "end")
        # Voltar para a tela principal
        self.mostrar_tela(self.tela_principal)


    # Método para atualizar a lista de proprietários na tela de listagem
    def atualizar_listagem_proprietarios(self):
        # Atualizar os nomes no combobox
        self.filtro_combo['values'] = ["Todos"] + [p.get_nome() for p in self.proprietarios]
        self.filtro_var_proprietario.set("Todos")
        # Limpar a listbox
        self.listbox_proprietario.delete(0, "end")
        for proprietario in self.proprietarios:
            self.listbox_proprietario.insert("end", str(proprietario))


    def atualizar_listagem_veiculos(self):
        self.listbox.delete(0, "end")
        for veiculo in self.veiculos:
            self.listbox.insert("end", str(veiculo))


    def salvar_veiculo(self):
        # Obter dados comuns
        placa = self.placa_entry.get().strip().upper()
        marca = self.marca_entry.get().strip()
        modelo = self.modelo_entry.get().strip()
        ano_str = self.ano_entry.get().strip()
        tipo = self.tipo_var.get()
        
        # Validar campos obrigatórios
        if not placa or not marca or not modelo or not ano_str:
            messagebox.showwarning("Dados incompletos", "Preencha todos os campos obrigatórios!")
            return
        
        # Validar formato da placa (ABC1234 ou ABC1D23)
        if not re.match(r'^[A-Z]{3}[0-9][0-9A-Z][0-9]{2}$', placa):
            messagebox.showwarning("Placa inválida", "A placa deve seguir o padrão ABC1234 ou ABC1D23")
            return
        
        # Validar ano
        try:
            ano = int(ano_str)
            ano_atual = datetime.now().year
            if ano < 1900 or ano > ano_atual + 1:
                messagebox.showwarning("Ano inválido", f"O ano deve estar entre 1900 e {ano_atual + 1}")
                return
        except ValueError:
            messagebox.showwarning("Ano inválido", "O ano deve ser um número")
            return
        
        # Criar o veículo do tipo específico
        if tipo == "Carro":
            num_portas_str = self.portas_entry.get().strip()
            if not num_portas_str:
                messagebox.showwarning("Dados incompletos", "Informe o número de portas")
                return
            try:
                num_portas = int(num_portas_str)
                if num_portas < 1 or num_portas > 5:
                    messagebox.showwarning("Valor inválido", "O número de portas deve estar entre 1 e 5")
                    return
                veiculo = Carro(placa, marca, modelo, ano, num_portas)
            except ValueError:
                messagebox.showwarning("Valor inválido", "O número de portas deve ser um número")
                return
                
        elif tipo == "Moto":
            cilindrada_str = self.cilindrada_entry.get().strip()
            if not cilindrada_str:
                messagebox.showwarning("Dados incompletos", "Informe a cilindrada")
                return
            try:
                cilindrada = int(cilindrada_str)
                if cilindrada < 50 or cilindrada > 2000:
                    messagebox.showwarning("Valor inválido", "A cilindrada deve estar entre 50 e 2000 cc")
                    return
                veiculo = Moto(placa, marca, modelo, ano, cilindrada)
            except ValueError:
                messagebox.showwarning("Valor inválido", "A cilindrada deve ser um número")
                return
                
        elif tipo == "Caminhao":
            capacidade_str = self.capacidade_entry.get().strip()
            if not capacidade_str:
                messagebox.showwarning("Dados incompletos", "Informe a capacidade de carga")
                return
            try:
                capacidade = float(capacidade_str)
                if capacidade <= 0:
                    messagebox.showwarning("Valor inválido", "A capacidade de carga deve ser maior que zero")
                    return
                veiculo = Caminhao(placa, marca, modelo, ano, capacidade)
            except ValueError:
                messagebox.showwarning("Valor inválido", "A capacidade de carga deve ser um número")
                return
        
        # Adicionar o veículo à lista
        self.veiculos.append(veiculo)
        messagebox.showinfo("Sucesso", "Veículo cadastrado com sucesso!")
        
        # Limpar campos
        self.placa_entry.delete(0, "end")
        self.marca_entry.delete(0, "end")
        self.modelo_entry.delete(0, "end")
        self.ano_entry.delete(0, "end")
        self.portas_entry.delete(0, "end")
        self.cilindrada_entry.delete(0, "end")
        self.capacidade_entry.delete(0, "end")
        
        # Voltar para a tela principal
        self.mostrar_tela(self.tela_principal)

    def filtrar_veiculos(self):
        # Limpar a lista
        self.listbox.delete(0, "end")
        
        # Filtrar veículos pelo tipo
        filtro = self.filtro_var.get()
        
        for veiculo in self.veiculos:
            if filtro == "Todos":
                self.listbox.insert("end", str(veiculo))
            elif filtro == "Carro" and isinstance(veiculo, Carro):
                self.listbox.insert("end", str(veiculo))
            elif filtro == "Moto" and isinstance(veiculo, Moto):
                self.listbox.insert("end", str(veiculo))
            elif filtro == "Caminhão" and isinstance(veiculo, Caminhao):
                self.listbox.insert("end", str(veiculo))

    def filtrar_proprietario(self):
        # Limpar a lista
        self.listbox.delete(0, "end")

        # Obter o filtro selecionado
        filtro = self.filtro_var_proprietario.get()

        # Filtrar proprietários pelo nome
        if filtro == "Todos":
            for proprietario in self.proprietarios:
                self.listbox.insert("end", str(proprietario))



    def ver_detalhes_proprietario(self):
        # Obter o índice selecionado
        selecionado = self.listbox_proprietario.curselection()
        if not selecionado:
            messagebox.showinfo("Aviso", "Selecione um proprietário para ver os detalhes")
            return
        
        # Obter o proprietário correspondente à seleção
        proprietario = self.proprietarios[selecionado[0]]
        
        # Montar a mensagem de detalhes
        detalhes = str(proprietario)

        for veiculo in self.veiculos:
            if proprietario.get_placas()[0] == veiculo.get_placa():
                if isinstance(veiculo, Carro):
                    detalhes += '\n\nTipo: Carro'
                elif isinstance(veiculo, Moto):
                    detalhes += '\n\nTipo: Moto'
                elif isinstance(veiculo, Caminhao):
                    detalhes += '\n\nTipo: Caminhão'
        
        # Mostrar detalhes
        messagebox.showinfo("Detalhes do Proprietário", detalhes)

        

    
    def ver_detalhes(self):
        # Obter o índice selecionado
        selecionado = self.listbox.curselection()
        if not selecionado:
            messagebox.showinfo("Aviso", "Selecione um veículo para ver os detalhes")
            return
        
        # Obter o veículo correspondente à seleção
        filtro = self.filtro_var.get()
        veiculos_filtrados = []
        
        for veiculo in self.veiculos:
            if filtro == "Todos":
                veiculos_filtrados.append(veiculo)
            elif filtro == "Carro" and isinstance(veiculo, Carro):
                veiculos_filtrados.append(veiculo)
            elif filtro == "Moto" and isinstance(veiculo, Moto):
                veiculos_filtrados.append(veiculo)
            elif filtro == "Caminhão" and isinstance(veiculo, Caminhao):
                veiculos_filtrados.append(veiculo)
        
        veiculo = veiculos_filtrados[selecionado[0]]
        
        # Montar a mensagem de detalhes usando polimorfismo
        detalhes = str(veiculo)
        
        # Adicionar informações específicas
        if isinstance(veiculo, Carro):
            detalhes += f"\nNúmero de Portas: {veiculo.get_num_portas()}"
        elif isinstance(veiculo, Moto):
            detalhes += f"\nCilindrada: {veiculo.get_cilindrada()} cc"
        elif isinstance(veiculo, Caminhao):
            detalhes += f"\nCapacidade de Carga: {veiculo.get_capacidade_carga()} kg"
        
        # Mostrar detalhes
        messagebox.showinfo("Detalhes do Veículo", detalhes)

# Iniciar a aplicação
if __name__ == "__main__":
    root = tk.Tk()
    app = SistemaVeiculos(root)
    root.mainloop()