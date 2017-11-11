'''

Reaproveitando mais uma vez o exemplo da bolinha:
crie um programa com a bolinha que desliza pela tela
e que contenha também uma plataforma, como se fosse
a raquete do jogo Pong. Essa plataforma nada mais é
do que um retângulo (pode ser na horizontal ou na
vertical). Quando a bola encostar na raquete, ela
deve quicar, assim como faz quando encosta na parede.
A raquete deve ser movimentada simplesmente
ao mover o ponteiro do mouse pela tela.

'''




from universe import *

(LARGURA, ALTURA) = (600, 400)
TELA = pg.display.set_mode((LARGURA, ALTURA))


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

Plataforma = namedlist("Plataforma", "x,y")
'''...'''

Jogo = namedlist("Jogo", "bolinha, plataforma")
'''...'''
JOGO_INICIAL = Jogo(BOLA_INICIAL, Plataforma(10,ALTURA//2))



'''...'''
def move_bola(bolinha):
    return bolinha

'''...'''
def move_jogo(jogo):
    move_bola(jogo.bolinha)
    return jogo


'''...'''
def trata_mouse(jogo,x,y,me):
    if me == pg.MOUSEMOTION:
        plataforma = jogo.plataforma
        plataforma.y = y
    return jogo

'''...'''
def desenha_jogo(jogo):
    pg.draw.rect(TELA,
                 (203, 230, 67),
                 (jogo.plataforma.x,
                  jogo.plataforma.y, 20,40))
    pg.draw.circle(TELA,
                 (203, 230, 67),
                   (jogo.bolinha.x,
                    jogo.bolinha.y), 20)


def main(jogo):
    big_bang(jogo, tela=TELA,
             quando_tick=move_jogo,
             quando_mouse=trata_mouse,
             desenhar=desenha_jogo,
             modo_debug=True
            )

main(JOGO_INICIAL)


