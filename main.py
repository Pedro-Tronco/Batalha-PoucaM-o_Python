import pygame, time

pygame.init()

clock = pygame.time.Clock()
icon  = pygame.image.load("assets/icon.png")
back_batalha = pygame.image.load("assets/background.png")
back_menu = pygame.image.load("assets/background_menu.png")
size = (800,600)
screen = pygame.display.set_mode(size) 
pygame.display.set_caption("Batalha PoucaMão")
pygame.display.set_icon(icon)
menuSFX = pygame.mixer.Sound("assets/menu_select.mp3")
attackSFX1 = pygame.mixer.Sound("assets/attack1.mp3")
attackSFX2 = pygame.mixer.Sound("assets/attack2.mp3")
attackSFX3 = pygame.mixer.Sound("assets/attack3.mp3")
attackSFX4 = pygame.mixer.Sound("assets/attack4.mp3")
switchSFX = pygame.mixer.Sound("assets/switch.mp3")
koSFX = pygame.mixer.Sound("assets/ko.mp3")
font = pygame.font.SysFont("arial",18)
fontMenu = pygame.font.SysFont("arial",55)
fontUI = pygame.font.SysFont("roboto",35)
pygame.mixer.music.load("assets/Battle! Gym Leader - Remix Cover (Pokémon Black and White) - 128.mp3")
pygame.mixer.music.set_volume(0.25)

state_mao = 0
timer_idle = 0

"""
0 = invisivel
1 = idle 1
2 = idle 2
3 = atk 1
4 = atk 2
5 = atk 3
"""

mao1_idle1 = pygame.image.load("assets/mao1-idle1.png")
mao1_idle2 = pygame.image.load("assets/mao1-idle2.png")
mao1_atk1 = pygame.image.load("assets/mao1-atk1.png")
mao1_atk2 = pygame.image.load("assets/mao1-atk2.png")
mao1_atk3 = pygame.image.load("assets/mao1-atk3.png")

pos_player = (180,180)

black = (0,0,0)
white = (255,255,255)


def seleciona_pokemon():
    pygame.mixer.music.play(-1)
    global state_mao, timer_idle
    state_mao = 1
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                quit()
            elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_1:
                state_mao = 3
            elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_2:
                state_mao = 4
            elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_3:
                state_mao = 5

        if state_mao == 1 and timer_idle > 40:
            state_mao = 2
            timer_idle = 0
        elif state_mao == 2 and timer_idle > 40:
            state_mao = 1
            timer_idle = 0
        elif state_mao > 2 and timer_idle > 60:
            state_mao = 1
            timer_idle = 0
                

        screen.fill(white)
        screen.blit(back_batalha, (0,0))

        if state_mao == 1:
            screen.blit(mao1_idle1,(pos_player))
        elif state_mao == 2:
            screen.blit(mao1_idle2,(pos_player))
        elif state_mao == 3:
            screen.blit(mao1_atk1,(pos_player))
        elif state_mao == 4:
            screen.blit(mao1_atk2,(pos_player))
        elif state_mao == 5:
            screen.blit(mao1_atk3,(pos_player))

        pygame.display.update()
        timer_idle += 1
        clock.tick(60)

def start(): 
    while True: 
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                quit()
            elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE:
                pygame.mixer.Sound.play(menuSFX)
                seleciona_pokemon()

        screen.fill(white)
        screen.blit(back_menu, (0,0))
        texto = fontMenu.render("Bem Vindo à Batalha PoucaMão", True, white)
        screen.blit(texto, (10,10))
        texto = fontUI.render("Aperte 'Espaço' para começar!", True, white)
        screen.blit(texto, (10,500))
        texto = fontUI.render("Aperte 'H' para ajuda.", True, white)
        screen.blit(texto, (10,550))

        pygame.display.update()
        clock.tick(60)

start()