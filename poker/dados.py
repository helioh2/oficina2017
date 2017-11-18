# from namedlist import namedlist

# Carta = namedlist("Carta", "valor,naipe")
# sete_ouro = Carta(7,"O")
# print(sete_ouro.valor)
# print(sete_ouro.naipe)
#
# nove_copas = (9, "C")
#
# tres_paus = "3P"
#
# valor = int(tres_paus[0])
# naipe = tres_paus[1]
# print(valor)
# print(naipe)

''' Carta eh uma string de dois caracteres
composta de valor e naipe
Naipes são representados como: copas = C,
espadas = E, paus = P, ouro = O
Rei = K, Rainha = Q, Valete = J

'''
#Exemplos:
REIS_ESPADA = "KE"
TRES_PAUS = "3P"


''' Mao eh uma lista de 5 cartas'''
'''Exemplos:'''
STRAIGHT1 = ["3O", "4P", "5O", "6E", "7C"]
FLUSH = "2C 7C JC AC 4C".split()
FULL_HOUSE = "6O 6E 6C 3P 3E".split()
ROYAL_STRAIGH_FLUSH = "AP KP QP JP TP".split()
STRAIGHT_FLUSH = "7O 8O 9O TO JO".split()
QUADRA = "9C 9E 9P 9O 3O".split()

