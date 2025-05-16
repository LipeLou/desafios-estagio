''' 
1) Dado a sequência de Fibonacci, 
onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores 
(exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), 
escreva um programa, informado um número, ele calcule a sequência de Fibonacci 
e retorne uma mensagem avisando se o número informado pertence ou não a sequência.
'''

# função que cria uma sequencia fibonacci até o número desejado
def fibonacci(n):
    seq = [0, 1]
    while seq[-1] <= n:
        proximo_numero = seq[-1] + seq[-2]
        seq.append(proximo_numero)
    return seq

# Entrando com algum número e chamando a função
num_informado = int(input('Digite o número à ser a avaliado: '))
sequencia = fibonacci(num_informado)

# Verificando se está ou não na sequencia
if num_informado in sequencia:
    print(f'Número informado ({num_informado}) pertence sequência!')
else:
    print(f'Número informado ({num_informado}) NÃO pertence a sequência!')


