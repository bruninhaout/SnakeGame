import pygame

fundo = (59, 55, 158)
cobra = (235, 213, 106)

dimensoes = (600, 600)
x = 300
y = 300

d = 20

lista_cobra = [[x, y]]

tela = pygame.display.set_mode((dimensoes))
pygame.display.set_caption("Snake.io")

tela.fill(fundo)

clock = pygame.time.Clock()

def desenha_cobra(lista_cobra):
    tela.fill(fundo)
    for unidade in lista_cobra:
        pygame.draw.rect(tela, cobra, [unidade[0], unidade[1], d, d])


def mover_cobra(lista_cobra):
    delta_x = 0
    delta_y = 0

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                delta_x = -d
                delta_y = 0
            elif event.key == pygame.K_RIGHT:
                delta_x = d
                delta_y = 0
            elif event.key == pygame.K_UP:
                delta_x = 0
                delta_y = -d
            elif event.key == pygame.K_DOWN:
                delta_x = 0
                delta_y = d

    x_novo = lista_cobra[-1][0] + delta_x
    y_novo = lista_cobra[-1][1] + delta_y

    lista_cobra.append([x_novo, y_novo])

    del lista_cobra[0]

    return lista_cobra

while True:
    pygame.display.update()
    desenha_cobra(lista_cobra)
    lista_cobra = mover_cobra(lista_cobra)
    print(lista_cobra)

    clock.tick(30)