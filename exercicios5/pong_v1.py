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

Bolinha = namedlist("Bolinha", "x dx y dy raio")
'''
Bolinha eh criada como: Bolinha(Int+ Int Int+ Int)
interp. uma bolinha na posicao (x,y) e deslocamentos
dx e dy.
Ex:
'''
BOLA_INICIAL = Bolinha(100,3,100,3, 20)
BOLA2 = Bolinha(200,-3,200,3, 20)
'''Template para dados do tipo Bolinha:
def fn_para_bolinha(bola):
    ... bola.x
        bola.dx
        bola.y
        bola.dy
'''

Plataforma = namedlist("Plataforma", "x, tx, y, ty")
'''...'''

Jogo = namedlist("Jogo", "bolinha, plataforma")
'''...'''
JOGO_INICIAL = Jogo(BOLA_INICIAL, Plataforma(10,15,ALTURA//2, 50))



'''...'''
def move_bola(bolinha):
    # calcula novo dy
    if (bolinha.y == ALTURA and bolinha.dy > 0) \
            or (bolinha.y == 0 and bolinha.dy < 0):  # se vaca bateu na parede
        bolinha.dy = - bolinha.dy
    # usar depurador (debugger)

    # calcula novo y
    bolinha.y = bolinha.y + bolinha.dy

    if bolinha.y > ALTURA:
        bolinha.y = ALTURA
    elif bolinha.y < 0:
        bolinha.y = 0

    # calcula novo dy
    if (bolinha.x == LARGURA and bolinha.dx > 0) \
            or (bolinha.x == 0 and bolinha.dx < 0):  # se vaca bateu na parede
        bolinha.dx = - bolinha.dx
    # usar depurador (debugger)

    # calcula novo y
    bolinha.x = bolinha.x + bolinha.dx

    if bolinha.x > LARGURA:
        bolinha.x = LARGURA
    elif bolinha.x < 0:
        bolinha.x = 0

    return bolinha


def colide(plataforma, bola):
    #versao simples


    # if (plataforma.x+plataforma.tx <=
    #         bola.x - bola.raio <=
    #     plataforma.x-plataforma.tx) and
    #     :
    pass


def inverte(bola):
    bola.dx = -bola.dx


'''...'''
def move_jogo(jogo):
    if colide(jogo.plataforma, jogo.bolinha):
        inverte(jogo.bolinha)
    move_bola(jogo.bolinha)
    return jogo


'''...'''
def trata_mouse(jogo,x,y,me):
    if me == pg.MOUSEMOTION:
        plataforma = jogo.plataforma
        plataforma.y = y - \
                        (plataforma.ty)//2
    return jogo

'''...'''
def desenha_jogo(jogo):
    pg.draw.rect(TELA,
                 (203, 230, 67),
                 (jogo.plataforma.x,
                  jogo.plataforma.y,
                  jogo.plataforma.tx,
                  jogo.plataforma.ty))
    pg.draw.circle(TELA,
                 (203, 230, 67),
                   (jogo.bolinha.x,
                    jogo.bolinha.y), jogo.bolinha.raio)


def main(jogo):
    big_bang(jogo, tela=TELA,
             quando_tick=move_jogo,
             quando_mouse=trata_mouse,
             desenhar=desenha_jogo,
             modo_debug=True
            )

main(JOGO_INICIAL)


