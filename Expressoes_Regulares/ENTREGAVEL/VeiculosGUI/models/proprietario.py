import re
import tkinter as tk
from tkinter import ttk, messagebox

class Proprietario:
    def __init__(self, nome, cpf, placas):
        self.__nome = nome
        self.__cpf = cpf
        self.__placas = list(placas)
    

    #CRIAR PROPRIETARIO
    def get_nome(self):
        return self.__nome
    
    def get_cpf(self):
        return self.__cpf
    
    def get_placas(self):
        return self.__placas

    def adicionar_veiculo(self, placa):
        placa = placa.upper()
        if self.validar_placa(placa):
            if placa not in self.__placas:
                self.__placas.append(placa)
                return True
            else:
                return False  
        else:
            return None

    def __str__(self):
        return f"Proprietário: {self.__nome}, CPF: {self.__cpf}, Veículos: {', '.join(self.__placas) if self.__placas else 'Nenhum'}"