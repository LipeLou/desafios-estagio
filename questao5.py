'''
5) Escreva um programa que inverta os caracteres de um string.
IMPORTANTE:
a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
b) Evite usar funções prontas, como, por exemplo, reverse;
'''

# Entrando com a string
txt = input('Digite um texto: ')

# Invertendo ela
for i in range(1, len(txt) + 1):
    print(f'{txt[-i]}', end='')