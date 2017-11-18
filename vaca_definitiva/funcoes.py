
from dados import *
import math

'''===================='''
''' Funções: '''

'''
mover_vaca_x: Vaca -> Vaca
Produz a próxima vaca (ou seja, fazer ela andar)
'''
def mover_vaca_x(vaca):
    if vaca.x < 0 or vaca.x > LARGURA:
        return "Erro: vaca invalida"
    else:
        #calcula novo dx
        if (vaca.x == PAREDE_DIREITA and vaca.dx > 0) \
                or (vaca.x == PAREDE_ESQUERDA and vaca.dx < 0):  #se vaca bateu na parede
            vaca.dx = - vaca.dx
        #usar depurador (debugger)

        #calcula novo x
        vaca.x = vaca.x + vaca.dx

        if vaca.x > PAREDE_DIREITA:
            vaca.x = PAREDE_DIREITA
        elif vaca.x < PAREDE_ESQUERDA:
            vaca.x = PAREDE_ESQUERDA

        return vaca



'''
mover_cc: Chupacabra -> Chupacabra
Mover o chupacabra no eixo y usando o dy
'''
def mover_cc(chupacabra):
    if chupacabra.y < 0 or chupacabra.y > ALTURA:
        return "Erro: vaca invalida"
    else:
        #calcula novo dy
        if (chupacabra.y == PAREDE_BAIXO and chupacabra.dy > 0) \
                or (chupacabra.y == PAREDE_CIMA and chupacabra.dy < 0):  #se vaca bateu na parede
            chupacabra.dy = - chupacabra.dy
        #usar depurador (debugger)

        #calcula novo y
        chupacabra.y = chupacabra.y + chupacabra.dy

        if chupacabra.y > PAREDE_BAIXO:
            chupacabra.y = PAREDE_BAIXO
        elif chupacabra.y < PAREDE_CIMA:
            chupacabra.y = PAREDE_CIMA

        return chupacabra


'''distancia: Int Int Int Int -> Float
Calcula a distancia entre dois pontos
'''
def distancia(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)



'''
colidirem: Vaca, Chupacabra -> Boolean
Verifica se a vaca e o chupacabra colidiram
'''
def colidirem(vaca, chupacabra):
    raio1 = IMG_VACA_INO.get_width()/2
    raio2 = IMG_CC_VORTANO.get_width()/2
    d = distancia(vaca.x, vaca.y, chupacabra.x, chupacabra.y)
    if d <= raio1 + raio2:
        return True
    #else
    return False

'''
mover_vaca_y: Vaca -> Vaca
Movimenta vaca no eixo y de acordo com dy
'''
def mover_vaca_y(vaca):
    if vaca.y == CHAO:
        vaca.dy = 0
    else:
        vaca.dy += G
        vaca.y += vaca.dy

        if vaca.y >= CHAO:
            vaca.y = CHAO
            vaca.dy = 0
    return vaca

'''
mover_jogo: Jogo -> Jogo
A funcao que eh chamada a cada tick para o jogo
'''
def mover_jogo(jogo):

    for chupacabra in jogo.chupacabras:
        if colidirem(jogo.vaca, chupacabra):
            jogo.game_over = True
            return jogo

    #else
    mover_vaca_x(jogo.vaca)
    mover_vaca_y(jogo.vaca)

    for chupacabra in jogo.chupacabras:
        mover_cc(chupacabra)  # funcao auxiliar (helper)

    return jogo


'''
desenha_vaca: Vaca -> Imagem
Desenha a vaca na tela
'''
def desenha_vaca(vaca):
    if vaca.dx < 0:
        TELA.blit(IMG_VACA_VORTANO,
                  (vaca.x - IMG_VACA_VORTANO.get_width() // 2,
                   vaca.y - IMG_VACA_VORTANO.get_height() // 2))
    else:
        TELA.blit(IMG_VACA_INO,
                  (vaca.x - IMG_VACA_INO.get_width() // 2,
                   vaca.y - IMG_VACA_INO.get_height() // 2))


'''
desenha_chupacabra: Chupacabra -> Imagem
Desenha o chupacabra
'''
def desenha_chupacabra(chupacabra):
    TELA.blit(IMG_CC_VORTANO,
              (chupacabra.x - IMG_CC_VORTANO.get_width() // 2,
               chupacabra.y - IMG_CC_VORTANO.get_height() // 2))


'''
desenha_jogo: Jogo -> Imagem
Desenha o jogo
'''
def desenha_jogo(jogo):
    if jogo.game_over:
        fonte = pg.font.SysFont("monospace", 40)
        ## render: String, Int, Cor

        texto = fonte.render("GAME OVER", 1, (255, 0, 0))

        ## blit: String, (Int, Int)
        TELA.blit(texto, (LARGURA // 2 - 20, ALTURA // 2 - 20))

    else:
        desenha_vaca(jogo.vaca)

        # antes
        # desenha_chupacabra(jogo.chupacabra)

        # depois
        for chupacabra in jogo.chupacabras:
            desenha_chupacabra(chupacabra)


'''
trata_tecla_vaca: Vaca, EventoTecla -> Vaca
Quando teclar espaço, inverte a direção da vaca
'''
def trata_tecla_vaca(vaca, tecla):
    # if tecla == pg.K_SPACE:
    #     vaca.dx = - vaca.dx
    # if tecla == pg.K_LEFT:
    #     vaca.x = vaca.x - abs(vaca.dx)
    # elif tecla == pg.K_RIGHT:
    #     vaca.x = vaca.x + abs(vaca.dx)
    if tecla == pg.K_LEFT:
        vaca.dx = -DX
    elif tecla == pg.K_RIGHT:
        vaca.dx = DX
    elif tecla == pg.K_UP and vaca.y == CHAO:
        vaca.y -= 10  #necessario, senao vaca fica no chao
        vaca.dy = -20
    return vaca


'''
trata_tecla: Jogo, EventoTecla -> Jogo
Trata tecla geral
'''
def trata_tecla(jogo, tecla):
    if jogo.game_over and tecla == pg.K_SPACE :
        return JOGO_INICIAL
    else:
        jogo.vaca = trata_tecla_vaca(jogo.vaca, tecla)
        return jogo


'''                                             
trata_solta_tecla: Vaca, EventoTecla -> Vaca    
Trata solta tecla vaca                 
'''
def trata_solta_tecla_vaca(vaca, tecla):
   if tecla == pg.K_LEFT or tecla == pg.K_RIGHT:
       vaca.dx = 0
   return vaca

'''trata_solta_tecla: Jogo, EventoTecla -> Jogo
Trata solta tecla geral
'''
def trata_solta_tecla(jogo, tecla):
    trata_solta_tecla_vaca(jogo.vaca, tecla)
    return jogo