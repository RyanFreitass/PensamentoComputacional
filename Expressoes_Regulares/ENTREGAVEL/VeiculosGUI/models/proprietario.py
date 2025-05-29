import re
import tkinter as tk
from tkinter import ttk, messagebox

class Proprietario:
    def __init__(self, nome, cpf, placas):
        self.__nome = nome
        self.__cpf = cpf
        self.__placas = []
    

    #CRIAR PROPRIETARIO
    def get_nome(self):
        return self.__nome
    
    def get_cpf(self):
        return self.__cpf
    
    def get_placas(self):
        return self.__placas

    #Validar CPF and PLACA
    def validar_cpf(self):
        cpf = re.sub(r'\d', '', self.__cpf)

        if len(cpf) != 11 or cpf == cpf[0] * 11:
            return False
        
        padrao = r'^\d{3}\.\d{3}\.\d{3}-\d{2}$'
        return re.match(padrao, cpf)

    def validar_placa(self, placa):
        padrao = r'[A-Z]{3}[0-9][A-Z][0-9]{2}$' 
        return re.match(padrao, placa)

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

    def excluir_veiculo(self):
        pass