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
    def validar_cpf(self, cpf):
        padrao_formatado = r'^\d{3}\.\d{3}\.\d{3}-\d{2}$'
        if not re.match(padrao_formatado, cpf):
            return False
        cpf = re.sub(r'[^0-9]', '', cpf)
        if len(cpf) != 11:
            return False
        if cpf == cpf[0] * 11:
            return False
        return True
            

    def validar_placa(self, placa):
        if re.match(r'^[A-Z]{3}[0-9][0-9A-Z][0-9]{2}$', placa):
            return True
        else:
            return False


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