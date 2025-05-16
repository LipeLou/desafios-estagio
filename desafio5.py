'''
Dado um array não classificado de inteiros `nums`, 
faça um algoritimo que retorna o comprimento da maior sequência de elementos consecutivos.

Exemplo 1
    Entrada: nums = [100,4,200,1,3,2]
    Saída: 4
    Explicação: A sequência de elementos consecutivos mais longa é [1,2,3,4].
    Portandom, seu comprimento é 4.

Exemplo 2:
    Entrada: nums = [0,3,7,2,5,8,4,6,0,1]
    Saída: 9'''


# Primeiro método pensado
def mair_seq(nums: list[int]) -> int:
    if not nums:
        return 0

    nums.sort()
    mair_seq = 1

    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            continue  # ignora nums repitidos
        elif nums[i] == nums[i - 1] + 1:
            mair_seq += 1
        else:
            break

    return mair_seq

# Método mais eficiente
def maior_sequencia(nums: list[int]) -> int:
    num_set = set(nums)
    maior_seq = 0

    for num in nums:

        if num -1 not in num_set:
            num_atual = num
            seq_atual = 1

            while num_atual + 1 in num_set:
                num_atual += 1
                seq_atual += 1
            maior_seq = max(maior_seq, seq_atual)
    
    return maior_seq


print(maior_sequencia([0,3,7,2,5,8,4,6,0,1]))
print(mair_seq([100,4,200,1,3,2]))
