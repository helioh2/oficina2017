
from collections import namedtuple

Pessoa = namedtuple("Pessoa", "nome,cpf,telefone,endereco")

p1 = Pessoa("Fulano", 8383838, "+55 44 289292", "Rua Pioneiro")

print("O nome do objeto p1 eh: "+p1.nome)  #acessando o campo nome de p1
print("O cpf do objeto p1 eh: "+str(p1.cpf))


pessoa2 = Pessoa("Beltrano", 2828282, "+252 337373", "Rua La Paloma")
print(pessoa2.nome)


print("jdksjdkjskdj \n\n\n shjsjsjsks")

print(pessoa2.nome)
print(pessoa2.cpf)


Coordenada = namedtuple("Coordenada", "x y")

ponto_origem = Coordenada(50,20)
print("A nave está na posicao", ponto_origem.x, ",", ponto_origem.y)






'''Definição de dados (USANDO A RECEITA)'''

Musica = namedtuple("Musica", "titulo,artista,album,genero,duracao")
'''
Musica é criado dessa forma: Musica(String, String, String, String, Int)
interp. representa uma musica com as informacoes
Exemplos:
'''
RACIONAIS1 = Musica("Diario de um Detento", "Racionais MC", \
                    "Sobrevidendo no Inferno", "Rap", 600)
PATATIPATATA = Musica("Arco iris feliz", "Patati", "Algodão doce",\
                      "Infantil", 300)
'''Template

def fn_para_musica(m):
    ... m.titulo
        m.artista
        m.album
        m.genero
        m.duracao
'''

'''Fim das definições de dados'''


'''
musica_mais_longa: Musica, Musica -> Musica
Retorna a musica que tem maior duração
'''
def musica_mais_longa(m1, m2):
    if m1.duracao >= m2.duracao:
        return m1
    else:
        return m2


import unittest

class MeusTestes(unittest.TestCase):

    def test_musica_mais_longa(self):
        self.assertEqual(  musica_mais_longa(RACIONAIS1, PATATIPATATA), RACIONAIS1)



# unittest.main()  # não excluir












