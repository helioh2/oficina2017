import unittest

'''EXERCÍCIOS:
O uso das receitas de projeto é obrigatório!! Os testes devem estar na classe Test no final
do arquivo.
'''

'''
Idade é um Natural
interp. a idade de uma pessoa em anos
Ex:
'''
I_FULANO = 18
I_BELTRANO = 25


'''
1.

PROBLEMA 1A: Considere a definição acima.

Projete uma função chamada 'eh_adolescente' que determina se uma pessoa
de uma idade específica é um adolescente (i.e., entre a idade 13 a 19)
(dica: se eh adolescente, retorne true, senão, retorne false
'''

###escreva o codigo aqui




'''
-------------//------------
2.

PROBLEMA 2A:

Você está projetando um programa para rastrear a viagem de um foguete
enquanto ele desce a 100 km de distância da Terra. Você está interessado
apenas na descida a partir de 100 km até o chão.

Projete uma definição de dados para representar a distância do foguete.
Chame de DistanciaDescidaFoguete.

'''

###escreva a definição aqui

'''
PROBLEMA 2B:

Projete uma função que imprima a distância que falta para o foguete chegar
na terra por meio de uma curta string que possa ser publicada no Twitter.
Por exemplo: "Altitude atual: 80 km da superfície".
Quando a descida acabar, a mensagem deve aparecer "O foguete pousou!".
Dê o seguinte nome para a função: 'distancia-foguete-para-msg'.

'''

###escreva o codigo aqui


'''
------------//------------
3.

PROBLEMA 3A:

Você precisa desenvolver um sistema para classificar edifícios no centro
de Curitiba, com base no quão velhos são.
De acordo com as leis da cidade, há três diferentes níveis de classificação:
novo, velho e patrimônio.

Projete uma definição de dado para representar esses níveis de classificação.
Chame de CondicaoEdificio.

'''

###escreva a definição aqui


'''
PROBLEMA 3B:

A cidade precisa demolir todos os edifícios classificados como "velho".
Você foi contratado para projetar uma função chamada 'demolir', que
determina se o edifício deve ser demolido ou não. (dica: "demolir"=True,
"não demolir"=False)

'''

###escreva o codigo aqui




'''
-------------------//--------------
4.

PROBLEMA 4:

Considere um jogo onde você precisa representar a quantidade de vidas de
seu personagem.
A única coisa que importa sobre essas vidas é:

    - se o personagem está morto (sem vida, game over)
    - se o personagem está vivo então pode ter 0 ou mais vidas extras.

Projete uma definição de dados chamada Vidas para representar quantas
vidas tem seu personagem.

Projete uma função chamada 'ganhar-vida' que permite aumentar as vidas
de um personagem. A função deve apenas aumentar a vida de um
persongagem se ele não estiver morto, caso contrário o personagem
continua morto.

'''

###escreva definicoes e codigo aqui



'''
---------------------//--------------
5.

PROBLEMA 5A:

Projete uma definição de dados para representar um filme, incluindo  
título, custo de produção, e ano que foi lançado.

Para ajudar a criar alguns exemplos, abaixo temos alguns fatos sobre alguns filmes: 
"Titanic" - custo: 200000000 lancamento: 1997
"Avatar" - custo: 237000000 lancamento: 2009
"The Avengers" - custo: 220000000 lancamento: 2012

No entanto, sinta-se livre para pesquisar.
DICA: terá que usar namedtuple ou class para criar um tipo composto (veja arquivo de exemplos)
'''

###escreva a definição aqui


'''
PROBLEMA 5B:

Projete uma função que RECEBE DOIS filmes e retorne
o título do filme lançado mais recentemente.
'''




'''Para cada nova funcao criada, voce deve criar uma funcao
dentro da classe Test para testá-la, conforme o template
'''
class Test(unittest.TestCase):

    pass #retirar após colocar primeiro teste

    #...
    ''' <<template>>
    def test_<nome_funcao>(self):
        self.assertEqual(<chamada_da_funcao>, <resultado_esperado>)
        self.assertEqual(<chamada_da_funcao>, <resultado_esperado>)
        ...
    '''

unittest.main()  #não excluir



