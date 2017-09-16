#!/usr/bin/python

import pygame as pg
import sys, os

COR_BRANCO = (255, 255, 255)



def big_bang(inic, tela,
             quando_tick=lambda e: e, \
             frequencia=28, \
             desenhar=lambda e: pg.Surface((0,0)), \
             quando_tecla=lambda e, k: e, \
             quando_mouse=lambda e, x, y, ev: e, \
             parar_quando=lambda e: False):

    def desenha_tela():
        tela.fill(COR_BRANCO)
        desenhar(estado)

    pg.init()
    estado = inic
    clock = pg.time.Clock()


    while True:

        pg.display.flip()

        if parar_quando(estado):
            print(estado)
            sys.exit(0)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                print(estado)
                sys.exit(0)

            if event.type == pg.KEYDOWN:
                estado = quando_tecla(estado, event.key)
                desenha_tela()

            elif event.type in [pg.MOUSEBUTTONDOWN, pg.MOUSEBUTTONUP, pg.MOUSEMOTION]:
                x, y = pg.mouse.get_pos()
                estado = quando_mouse(estado, x, y, event.type)
                desenha_tela()

        estado = quando_tick(estado)

        desenha_tela()

        clock.tick(frequencia)