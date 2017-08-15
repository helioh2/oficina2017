#!/usr/bin/python

import pygame as pg
import sys

COR_BRANCO = (255, 255, 255)

def big_bang(inic, tela,
             quando_tick=lambda e: e, \
             frequencia=20, \
             desenhar=lambda e: TELA_BRANCO, \
             quando_tecla=lambda e, k: e, \
             quando_mouse=lambda e, x, y: e, \
             parar_quando=lambda e: False):

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
            elif event.type == pg.MOUSEBUTTONDOWN:
                x, y = pg.mouse.get_pos()
                estado = quando_mouse(estado, x, y)

        estado = quando_tick(estado)

        tela.fill(COR_BRANCO)
        desenhar(estado)

        clock.tick(frequencia)