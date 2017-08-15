
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









