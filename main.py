import pygame
import random

fundo = (59, 55, 158)
cobra = (235, 213, 106)
comida = (255, 0, 0)

dimensoes = (600, 600)
x = 300
y = 300

d = 20

lista_cobra = [[x, y]]

dx = 0
dy = 0

x_comida = round(random.randrange(0, 600 - d)/20) * 20
y_comida = round(random.randrange(0, 600 - d)/20) * 20

tela = pygame.display.set_mode((dimensoes))
pygame.display.set_caption("Snake.io")

tela.fill(fundo)

clock = pygame.time.Clock()

def desenha_cobra(lista_cobra):
    tela.fill(fundo)
    for unidade in lista_cobra:
        pygame.draw.rect(tela, cobra, [unidade[0], unidade[1], d, d])


def mover_cobra(dx, dy, lista_cobra):

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dx = -d
                dy = 0
            elif event.key == pygame.K_RIGHT:
                dx = d
                dy = 0
            elif event.key == pygame.K_UP:
                dx = 0
                dy = -d
            elif event.key == pygame.K_DOWN:
                dx = 0
                dy = d

    x_novo = lista_cobra[-1][0] + dx
    y_novo = lista_cobra[-1][1] + dy

    lista_cobra.append([x_novo, y_novo])

    del lista_cobra[0]

    return dx, dy, lista_cobra


def verifica_comida(dx, dy, x_comida, y_comida, lista_cobra):
    head = lista_cobra[-1]

    x_novo = head[0] + dx
    y_novo = head[1] + dy

    if head[0] == x_comida and head[1] == y_comida:
        lista_cobra.append([x_novo, y_novo])

    pygame.draw.rect(tela, comida, [x_comida, y_comida, d, d])

    return x_comida, y_comida, lista_cobra

while True:
    pygame.display.update()
    desenha_cobra(lista_cobra)
    dx, dy, lista_cobra = mover_cobra(dx, dy, lista_cobra)
    x_comida, y_comida, lista_cobra = verifica_comida(dx, dy, x_comida, y_comida, lista_cobra)
    print(lista_cobra)

    clock.tick(9)