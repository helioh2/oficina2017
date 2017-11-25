from dados import *


def pega_valores(mao):
    # valores = []
    # for carta in mao:
    #     valores.append("--23456789TJQKA".index(carta[0]))


    #LIST COMPREHENSION
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
    naipes = [carta[1] for carta in mao]
    return naipes


def straight(valores):
    '''
    Verifica se os valores formam uma sequência
    :param valores:List<Int>
    :return:Boolean
    '''
    # for i in range(1,5):
    #     if valores[i-1] + 1 != valores[i]:
    #         return False
    # return True

    return max(valores) - min(valores) == 4 and len(set(valores)) == 5


def flush(naipes):
    '''

    :param naipes:List<Char>
    :return: Boolean
    '''
    return (len(set(naipes)) == 1)

# print(flush(['P', 'P', 'P', 'P', 'P']))

def mesmo_valor(valores, quant):
    for valor in valores:
        if valores.count(valor) == quant:
            return True
    return False

def quadra(valores):
    '''

    :param valores:List<Int>
    :return:Boolean
    '''
    # for valor in valores:
    #     if valores.count(valor) == 4:
    #         return True
    # return False
    return mesmo_valor(valores, 4) #delegação

def trinca(valores):
    return mesmo_valor(valores, 3)

def um_par(valores):
    return mesmo_valor(valores, 2)



# print(quadra([11, 11, 11, 10, 9]))


''' rank_mao: Mao -> Numero[1,10]'''
def rank_mao(mao):
    valores = pega_valores(mao)
    naipes = pega_naipes(mao)
    if straight(valores) and flush(naipes):
        return 22
    elif quadra(valores):
        return 21
    elif trinca(valores) and um_par(valores):
        return (20, sorted(valores, reverse=True))
    elif flush(naipes):
        return 19
    elif straight(valores):
        return 18
    elif trinca(valores):
        return 17
    elif dois_pares(valores):
        return 16
    elif um_par(valores):
        return 15
    else:
        return max(valores)



'''poker: List<Mao> -> Mao'''
def poker(maos):
    return max(maos, key=rank_mao)
