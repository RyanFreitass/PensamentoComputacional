import re

def validar_cartao(cartao):
#VISA = 4
#MASTERCARD = 51, 52, 53, 54, 55
#American Express = 34, 37
#16 Digitos
    padrao = r'^[^0-9]'