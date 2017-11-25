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

straight_flush1 = "TC JC QC KC AC".split()
straight_flush2 = "8C 9C DC JC QC".split()
quadra1 = "4E 4C 4P 4O 6C".split()
full_house1 = "KE KC KP TC TP".split()
flush1 = "QP 8P 6P 4P 3P".split()
straigh1 = "2O 3P 4E 5O 6P".split()
trinca1 = "JP JC JO 5P 8O".split()
doi_pares1 = "TO TP 6E 6P KO".split()
um_par1 = "AC AP 8E 6O 2O".split()
carta_alta1 = "KC JE TP 6C 3O".split()

