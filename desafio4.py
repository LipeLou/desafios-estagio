'''
4) Escreva um programa que inverta os caracteres de um string.
IMPORTANTE:
a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
b) Evite usar funções prontas, como, por exemplo, reverse;
'''

def inverter_str(txt: str) -> str:
    return txt[::-1]

# Entrando com a string e invertendo ela
txt = input('Digite um texto: ')
print(inverter_str(txt))
