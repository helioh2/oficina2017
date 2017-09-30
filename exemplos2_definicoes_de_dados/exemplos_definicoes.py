
'''
ContagemRegressiva é um Int[0, 10]
interp.: o numero de segundos faltantes
Exemplos:
'''
C1 = 10  #inicio
C2 = 5  #meio
C3 = 0  #fim
'''Template de funcoes que recebem ContagemRegressiva:
def fn_para_contagem_regressiva(cont):
    ... cont    #faz algo com cont
'''



'''
CorSemaforo eh um dos possiveis valores:
- "vermelho"
- "amarelo"
- "verde"
interp.: a cor atual acesa do semáforo
Exemplos: dispensa

Template para funcoes que recebem CorSemaforo:
def fn_para_cor_semaforo(cs):
    if cs == "vermelho":
        ...
    elif cs == "amarelo":
        ...
    elif cs == "verde":
        ...

(template baseado em dados enumerados)    
'''
    

'''
Passaro eh um dos tipos:
- False
- Int positivo (>=0)
interp. False significa que nao tem passaro na tela,
e se for Int entao significa a posicao x do passaro
Exemplos:
'''
P_MORTO = False
P1 = 3
'''Template para funcao que recebe Passaro:
def fn_para_passaro(p):
    if not passaro:
        ...
    elif type(passaro) is int:
        ... passaro
'''



'''
Proximidade é um desses:
- Float (30, inf.]
- Float (5, 30]
- Float [0, 5]
interp. distancia em centimetros entre foguete e obstaculo tal que
    - Float [30, inf.] é considerado "seguro"
    - Float (5, 30] é considerado "cuidado"
    - Float [0, 5] é considerado "perigo"
Exemplos:
'''
PR1 = 40.0
PR2 = 0.9
''' Template para funcao que recebe Proximidade:
def fn_para_proximidade(p):
    if p > 30:
        ... p
    elif 5 < p <= 30:
        ... p
    elif 0 <= p <= 5:
        ... p
'''


''' 
Exemplos de dados compostos:
'''

''' Maneira 1: dado imutavel usando namedtuple'''

from collections import namedtuple

Pessoa = namedtuple("Pessoa", "nome endereco cpf") #nome, endereco e cpf são os campos
'''
Pessoa é criada como: Pessoa(String String Int)
interp. uma pessoa com nome, endereço e cpf
Ex:
'''
FULANO = Pessoa("Fulano", "Rua Pioneiro", 28282828)
BELTRANO = Pessoa("Beltrano", "Av Kennedy", 636363)
'''Template para dados do tipo Pessoa:
def fn_para_pessoa(p):
    ... p.nome
        p.endereco
        p.cpf           #faz algo com os campos do tipo Pessoa
'''


''' Maneira 2: dados mutaveis usando class'''

class Aluno:
    '''
    Aluno é criado como: Aluno(String, String, Int)
    interp. aluno com nome, curso e GRR
    exemplos:
    JOAO = Aluno("João", "Computação", 20187272)
    MARIA = Aluno("Maria", "Exatas", 201837372
    '''
    def __init__(self, nome, curso, grr):  #construtor com os campos do tipo
        self.nome = nome
        self.curso = curso
        self.grr = grr
    '''
    Template para dados do tipo Aluno:
    def fn_para_aluno(a):
        ... a.nome
            a.curso
            a.grr         #faz algo com os campos do aluno
    '''


''' Maneira 3: dado mutavel usando namedlist'''

from namedlist import namedlist

Bolinha = namedlist("Bolinha", "x dx y dy")
'''
Bolinha eh criada como: Bolinha(Int+ Int Int+ Int)
interp. uma bolinha na posicao (x,y) e deslocamentos
dx e dy.
Ex:
'''
BOLA_INICIAL = Bolinha(100,3,100,3)
BOLA2 = Bolinha(200,-3,200,3)
'''Template para dados do tipo Bolinha:
def fn_para_bolinha(bola):
    ... bola.x
        bola.dx
        bola.y
        bola.dy
'''



