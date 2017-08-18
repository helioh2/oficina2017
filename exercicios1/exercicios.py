import unittest

''' EXERCÍCIOS
Obrigatorio UTILIZAR RECEITA DE PROJETO!!!
Todos os testes devem ser feitos dentro da classe Tests no final do arquivo.
Faca os testes antes do codigo, conforme a receita de projeto e a tecnica TDD.

(ATENÇÃO: Nao apague os comentarios entre aspas triplas, apenas os
comentarios na frente de #).
'''

'''
1. Defina uma funcao que encontre o maior valor entre 2 valores dados
'''


'''
2. Defina uma funcao que receba 3 numeros como parametros
e retorne a soma dos quadrados dos dois maiores numeros.
'''

#escreva seu programa aqui (incluindo assinatura, codigo e stub).
#os testes devem ser feitos dentro da classe Tests no final do arquivo


'''
3. Defina uma funcao que calcule a distancia de um ponto no plano cartesiano (representado por dois
numeros) a origem.
'''

#escreva seu programa aqui (incluindo assinatura, codigo e stub).
#os testes devem ser feitos dentro da classe Tests no final do arquivo

'''
4. Defina uma funcao que receba como parametro 3 numeros que representam
os lados de um triangulo e classifique o triangulo como equilatero,
isosceles ou escaleno. Veja a pagina sobre triangulos na Wikipedia.
'''

#escreva seu programa aqui (incluindo assinatura, codigo e stub).
#os testes devem ser feitos dentro da classe Tests no final do arquivo

'''
5. Defina uma funcao que classifique o grau de obesidade de uma
pessoa usando o IMC.
'''

#escreva seu programa aqui (incluindo assinatura, codigo e stub).
#os testes devem ser feitos dentro da classe Tests no final do arquivo

'''
6. Desenvolva uma funcao 'juros_poupanca' que consome uma quantia depositada
de dinheiro, e produz a quantia de juros recebida em um ano. O banco
paga 4% para depositos de até R$1000, 4,5% para depositos de até
R$5000 e 5% para depositos acima de R$5000.
'''

#escreva seu programa aqui (incluindo assinatura, codigo e stub).
#os testes devem ser feitos dentro da classe Tests no final do arquivo

'''
7. Defina uma funcao chamada fahrenheit_para_celsius que consome uma temperatura
medida em Fahrenheit e produz a equivalente em Celsius. Pesquise a formula
na internet ou em um livro.
'''

#escreva seu programa aqui (incluindo assinatura, codigo e stub).
#os testes devem ser feitos dentro da classe Tests no final do arquivo

'''
8. Os Estados Unidos e a Grã-Bretanha utilizam o sistema de medidas inglês. 
O resto do mundo usa o sistema metrico. Pessoas que viajam bastante,
principalmente a negócios, frequentemente precisam fazer a conversão
entre esses sistemas de medidas. A tabela abaixo mostra as seis principais
unidades de medida do sistema ingles:
             ingles            	metrico
           1 polegada      =       2.54 cm
           1 pé = 12 polegadas
           1 jarda = 3 pés
           1 vara = 5(1/2)	jardas
           1 furlong = 40 varas
           1 milha = 8 furlongs 
 Desenvolva as funcoes polegadas_para_cm, pes_para_polegadas, jardas_para_pes,
 varas_para_jardas, furlongs_para_varas e milhas_para_furlongs.
 Então desenvolva as funcoes pes_para_cm, jardas_para_cm, varas_para_polegadas,
 e milhas_para_pes
 DICA: Reuse as funcoes o maximo possivel. Use constantes.
'''

#escreva seu programa aqui (incluindo assinatura, codigo e stub).
#os testes devem ser feitos dentro da classe Tests no final do arquivo


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
