import random
import string
import os

def gerar_senha():
    senha = []
    maiusculo = random.choice(string.ascii_uppercase)
    minusculo = random.choice(string.ascii_lowercase)
    tamanho = random.randint(5,10)
    numeric = random.randint(1,9)
    for x in range(0, tamanho):
        opcao = random.randint(1,3)
        match opcao:
            case 1:
                senha.append(random.choice(string.ascii_uppercase))
            case 2:
                senha.append(random.choice(string.ascii_lowercase))
            case 3:
                senha.append(str(random.randint(1,9)))
                
    senha.insert(random.randint(0,5), maiusculo)
    senha.insert(random.randint(0,6), minusculo)
    senha.insert(random.randint(0,7), str(numeric))
    
    senha = ''.join(senha)
    return senha
        

while True:
    x = input('')
    if x != '':
        break
    print(gerar_senha())