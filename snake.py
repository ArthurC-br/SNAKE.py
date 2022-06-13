import pygame
from pygame.locals import *
from random import randint

pygame.init()

widht = 640
height = 480
x_snake = (height/2)
y_snake = (widht/2)
x_maca = (randint(20,620)//10)*10
y_maca = (randint(20,460)//10)*10
speed = 10
rota = 1
pontos = 0
lista_snake = []
compri_snake = 10

fonte = pygame.font.SysFont('arial', 30, bold=True,italic=True)
screen = pygame.display.set_mode((widht, height))
pygame.display.set_caption('Snake')
tick = pygame.time.Clock()
kill = False

def aumenta_snake(lista_snake):
    for XeY in lista_snake:
        pygame.draw.rect(screen, (0,255,0), (XeY[0], XeY[1], 20, 20))

def start_game():
    global pontos,compri_snake,x_snake,y_snake,x_maca,y_maca,lista_snake,lista_head,kill
    pontos=0
    compri_snake=3
    x_snake = (height / 2)
    y_snake = (widht / 2)
    x_maca = (randint(20, 620) // 10) * 10
    y_maca = (randint(20, 460) // 10) * 10
    lista_snake = []
    lista_head = []
    kill = False
while True:
    tick.tick(20)
    screen.fill((255,255,255))

    mensagem = f'Pontos: {pontos}'
    texto_formatado = fonte.render(mensagem, True, (0, 0, 0))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        if event.type == KEYDOWN:
            if event.key == K_UP and rota>=3:
                rota = 1
            if event.key == K_DOWN and rota>=3:
                rota = 2
            if event.key == K_LEFT and rota<=2:
                rota = 3
            if event.key == K_RIGHT and rota<=2:
                rota = 4

    if rota == 1:
        y_snake -= speed
    if rota == 2:
        y_snake += speed
    if rota == 3:
        x_snake -= speed
    if rota == 4:
        x_snake += speed


    maca = pygame.draw.rect(screen, (0, 255, 0), (x_snake, y_snake, 20, 20))
    snake = pygame.draw.rect(screen, (255, 0, 0), (x_maca, y_maca, 20, 20))

    lista_head = []
    lista_head.append(x_snake)
    lista_head.append(y_snake)
    lista_snake.append(lista_head)
    if lista_snake.count(lista_head)>1:
        kill = True
    fonte2 = pygame.font.SysFont('arial', 20,bold=True,italic=True)
    mensagem2 = 'Game Over! Pressione a tecla R para jogar novamente'
    texto_formatado2 = fonte2.render(mensagem2, True, (0, 0, 0))
    ret_mensagem = texto_formatado2.get_rect()
    while kill:
            screen.fill((255,255,255))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        start_game()
            ret_mensagem.center = (widht//2,height//2)
            screen.blit(texto_formatado2, ret_mensagem)
            pygame.display.update()

    if len(lista_snake) > compri_snake:
        del lista_snake[0]


    aumenta_snake(lista_snake)

    screen.blit(texto_formatado, (460,20))
    pygame.display.update()

    if maca.colliderect(snake):
        x_maca = (randint(20,620)//10)*10
        y_maca = (randint(20,460)//10)*10
        pontos += 1
        compri_snake += 1

    if x_snake >= widht:
        kill = True
    if y_snake >= height:
        kill = True
    if y_snake <= 0:
        kill = True
    if x_snake <= 0:
        kill = True

