"""
11. remove_adjacent

Dada uma lista de números, retorne uma lista onde todos elementos
adjacentes iguais são reduzidos a um único elemento.

Exemplo: [1, 2, 2, 3]
Irá retornar: [1, 2, 3]
"""

def remove_adjacent(nums):
    # Solução 1 - /ricardodcn
    # l_nova = nums[:1]
    # l_nova[1:] = [j for i, j in zip(nums, nums[1:]) if i != j]
    # return l_nova

    # Solução 2 - /zeny-brus
    if nums == []:
        return nums
    else:
        return [a for a, b in zip(nums, nums[1:] + [not nums[-1]]) if a != b]

    # Solução 3 - /avellar1975
    #return [v for i, v in enumerate(nums) if nums[i] != nums[i - 1] or i == 0]

    # Solução 4 - /pamatro
    # def remove_adjacent(nums):
    #     result = []
    #     for num in nums:
    #         if len(result) == 0 or num != result[-1]:
    #             result.append(num)
    #     return result


# --- Daqui para baixo são apenas códigos auxiliáries de teste. ---

def test(f, in_, expected):
    """
    Executa a função f com o parâmetro in_ e compara o resultado com expected.
    :return: Exibe uma mensagem indicando se a função f está correta ou não.
    """
    out = f(in_)

    if out == expected:
        sign = '✅'
        info = ''
    else:
        sign = '❌'
        info = f'e o correto é {expected!r}'

    print(f'{sign} {f.__name__}({in_!r}) retornou {out!r} {info}')


if __name__ == '__main__':
    # Testes que verificam o resultado do seu código em alguns cenários.
    test(remove_adjacent, [1, 2, 2, 3], [1, 2, 3])
    test(remove_adjacent, [2, 2, 3, 3, 3], [2, 3])
    test(remove_adjacent, [], [])
    test(remove_adjacent, [2, 2, 3, 3, 3, 2, 2], [2, 3, 2])
