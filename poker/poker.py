from dados import *


def pega_valores(mao):
    # valores = []
    # for carta in mao:
    #     valores.append("--23456789TJQKA".index(carta[0]))

    valores = ["--23456789TJQKA".index(carta[0]) for carta in mao]
    return sorted(valores)

    # valores = []
    # for carta in mao:
    #     valor_str = carta[0]
    #     if valor_str == "J":
    #         valores.append(11)
    #     elif valor_str == "Q":
    #         valores.append(12)
    #     elif valor_str == "K":
    #         valores.append(13)
    #     elif valor_str == "A":
    #         valores.append(1)
    #     else:
    #         valores.append(int(valor_str))
    #
    # return sorted(valores)

print(pega_valores(FLUSH))

def pega_naipes(mao):
    pass


''' rank_mao: Mao -> Numero[1,10]'''
def rank_mao(mao):
    valores = pega_valores(mao)
    naipes = pega_naipes(mao)


'''poker: List<Mao> -> Mao'''
def poker(maos):
    return max(maos, key=rank_mao)
