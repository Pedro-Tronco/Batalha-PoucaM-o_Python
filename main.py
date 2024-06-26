import pygame
from random import randint

pygame.init()

clock = pygame.time.Clock()
icon  = pygame.image.load("Recursos/icon.ico")
back_batalha = pygame.image.load("Recursos/background.png")
back_menu = pygame.image.load("Recursos/background_menu.png")
size = (800,600)
screen = pygame.display.set_mode(size) 
pygame.display.set_caption("Batalha PoucaMão")
pygame.display.set_icon(icon)
menuSFX = pygame.mixer.Sound("Recursos/menu_select.mp3")
attackSFX1 = pygame.mixer.Sound("Recursos/attack1.mp3")
attackSFX2 = pygame.mixer.Sound("Recursos/attack2.mp3")
attackSFX3 = pygame.mixer.Sound("Recursos/attack3.mp3")
switchSFX = pygame.mixer.Sound("Recursos/switch.mp3")
koSFX = pygame.mixer.Sound("Recursos/ko.mp3")
font = pygame.font.SysFont("roboto",24)
fontMenu = pygame.font.SysFont("roboto",65)
fontUI = pygame.font.SysFont("roboto",35)
pygame.mixer.music.load("Recursos/Battle! Gym Leader - Remix Cover (Pokémon Black and White) - 128.mp3")
pygame.mixer.music.set_volume(0.3)

timer_idle_player = 0
timer_idle_enemy = 0
golpe_player = 0; golpe_enemy = 0
"""1= Tesoura, 2= Papel, 3= Pedra"""
state_mao_player = 0; state_mao_enemy = 0
"""0= invisivel, 1= idle1, 2= idle2, 3= atk1, 4= atk2, 5= atk3, 6= dano, 7= def"""

mao_player_idle1 = pygame.image.load("Recursos/mao1-idle1.png")
mao_player_idle2 = pygame.image.load("Recursos/mao1-idle2.png")
mao_player_atk1 = pygame.image.load("Recursos/mao1-atk1.png")
mao_player_atk2 = pygame.image.load("Recursos/mao1-atk2.png")
mao_player_atk3 = pygame.image.load("Recursos/mao1-atk3.png")
mao_player_dmg = pygame.image.load("Recursos/mao1-dmg.png")
mao_player_def = pygame.image.load("Recursos/mao1-def.png") 

mao_enemy_idle1 = pygame.image.load("Recursos/mao2-idle1.png")
mao_enemy_idle2 = pygame.image.load("Recursos/mao2-idle2.png")
mao_enemy_atk1 = pygame.image.load("Recursos/mao2-atk1.png")
mao_enemy_atk2 = pygame.image.load("Recursos/mao2-atk2.png")
mao_enemy_atk3 = pygame.image.load("Recursos/mao2-atk3.png")
mao_enemy_dmg = pygame.image.load("Recursos/mao2-dmg.png")
mao_enemy_def = pygame.image.load("Recursos/mao2-def.png") 

pos_player = [60,55]
pos_enemy = [550,155]
allow_choice = True
player_hp = 200
enemy_hp = 200
player_choice = 0
enemy_choice = 0

black = (0,0,0)
white = (255,255,255)
gray = (65,65,65)

def animacao_tesoura(player): 
    """True = player, False = enemy"""
    global pos_player, pos_enemy, timer_idle_player, timer_idle_enemy, state_mao_player, state_mao_enemy, player_choice, enemy_choice
    if player:
        if timer_idle_player <= 20:
            pos_player[0] = 60 - timer_idle_player*2
        elif timer_idle_player > 30 and timer_idle_player < 50: 
            pos_player[0] = -510 + timer_idle_player*17
        elif timer_idle_player >=50 and timer_idle_player < 60:
            pos_player[0] = 425 - timer_idle_player*2.5
            state_mao_enemy = 6
        elif timer_idle_player == 60:
            pos_player[0] = 60
            pos_player[1] = 55
            damage_calc()
    else:
        if timer_idle_enemy <= 20:
            pos_enemy[0] = 550 + timer_idle_enemy*2
        elif timer_idle_enemy > 30 and timer_idle_enemy < 50: 
            pos_enemy[0] = 850 - timer_idle_enemy*8
        elif timer_idle_enemy >= 50 and timer_idle_enemy < 60:
            pos_enemy[0] = 350 + timer_idle_enemy*2.5
            state_mao_player = 6
        elif timer_idle_enemy == 60:
            pos_enemy[0] = 550
            pos_enemy[1] = 155
            damage_calc()

def animacao_papel(player): 
    """True = player, False = enemy"""
    global pos_player, pos_enemy, timer_idle_player, timer_idle_enemy, state_mao_player, state_mao_enemy, player_choice, enemy_choice
    if player:
        if timer_idle_player <=25:
            pos_player[0] = 60 - timer_idle_player*2
        elif timer_idle_player >= 30 and timer_idle_player <=41:
            pos_player[0] = -740 + timer_idle_player*25
            pos_player[1] = 105 - timer_idle_player*2
        elif timer_idle_player >41 and timer_idle_player < 45: 
            state_mao_enemy = 6
        elif timer_idle_player >= 45 and timer_idle_player < 60:
            pos_player[0] = 295 - timer_idle_player*2
            pos_player[1] = 10 + timer_idle_player//2
        elif timer_idle_player == 60:
            pos_player[0] = 60
            pos_player[1] = 55
            damage_calc()
    else:
        if timer_idle_enemy <=25:
            pos_enemy[0] = 550 + timer_idle_enemy
        elif timer_idle_enemy >= 30 and timer_idle_enemy <=41:
            pos_enemy[0] = 940 - timer_idle_enemy*12
            pos_enemy[1] = 185 - timer_idle_enemy
        elif timer_idle_enemy >41 and timer_idle_enemy < 45: 
            state_mao_player = 6
        elif timer_idle_enemy >= 45 and timer_idle_enemy < 60:
            pos_enemy[0] = 415 + timer_idle_enemy
            pos_enemy[1] = 145 + timer_idle_enemy//4
        elif timer_idle_enemy == 60:
            pos_enemy[0] = 550
            pos_enemy[1] = 155
            damage_calc()

def animacao_pedra(player):
    """True = player, False = enemy"""
    global pos_player, pos_enemy, timer_idle_player, timer_idle_enemy, state_mao_player, state_mao_enemy, player_choice, enemy_choice
    if player:
        if timer_idle_player <= 10:
            pos_player[1] = 55 - timer_idle_player*2
        elif timer_idle_player <= 30:
            pos_player[1] = 15 + timer_idle_player*2
        elif timer_idle_player > 30 and timer_idle_player <40:
            pos_player[1] = 135 - timer_idle_player*2
        elif timer_idle_player >= 40 and timer_idle_player <= 45:
            pos_player[1] = 55
            state_mao_player = 7
        elif timer_idle_player > 45 and timer_idle_player <= 50:
            state_mao_player = 5
        elif timer_idle_player > 50 and timer_idle_player <= 55:
            state_mao_player = 7
        elif timer_idle_player > 55 and timer_idle_player < 60:
            state_mao_player = 5
            pos_player[0] = 60
            pos_player[1] = 55
        elif timer_idle_player == 60:
            if player_choice >= enemy_choice:
                state_mao_enemy = enemy_choice + 2
    else:
        if timer_idle_enemy <= 10:
            pos_enemy[1] = 155 - timer_idle_enemy
        elif timer_idle_enemy <= 30:
            pos_enemy[1] = 135 + timer_idle_enemy
        elif timer_idle_enemy > 30 and timer_idle_enemy <40:
            pos_enemy[1] = 195 - timer_idle_enemy
        elif timer_idle_enemy >= 40 and timer_idle_enemy <= 45:
            pos_enemy[1] = 155
            state_mao_enemy = 7
        elif timer_idle_enemy > 45 and timer_idle_enemy <= 50:
            state_mao_enemy = 5
        elif timer_idle_enemy > 50 and timer_idle_enemy <= 55:
            state_mao_enemy = 7
        elif timer_idle_enemy > 55 and timer_idle_enemy <60:
            state_mao_enemy = 5
            pos_enemy[0] = 550
            pos_enemy[1] = 155
        elif timer_idle_enemy == 60:
            if enemy_choice > player_choice:
                state_mao_player = player_choice + 2
    
def batalha(choice):
    global player_choice, enemy_choice, state_mao_player, state_mao_enemy, timer_idle_player, timer_idle_enemy
    timer_idle_enemy = 0; timer_idle_player = 0
    player_choice = choice
    enemy_choice = randint(1,3)
    if player_choice >= enemy_choice:
        state_mao_player = player_choice + 2
    else:
        state_mao_enemy = enemy_choice + 2

def damage_calc():
    global timer_idle_enemy, timer_idle_player, state_mao_player, state_mao_enemy, player_choice, enemy_choice
    print("a")
    if player_choice >= enemy_choice:
        state_mao_enemy = enemy_choice +2
    else:
        state_mao_player = player_choice +2

def main():
    pygame.mixer.music.play(-1)
    global state_mao_player, timer_idle_player, state_mao_enemy, timer_idle_enemy, allow_choice, player_choice, enemy_choice
    state_mao_player = 1
    state_mao_enemy = 2

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                quit()
            elif evento.type == pygame.MOUSEBUTTONDOWN and allow_choice:
                if button_pedra.collidepoint(evento.pos):
                    batalha(3)
                elif button_papel.collidepoint(evento.pos):
                    batalha(2)
                elif button_tesoura.collidepoint(evento.pos):
                    batalha(1)

        if state_mao_player == 1 and timer_idle_player > 40:
            state_mao_player = 2
            timer_idle_player = 0
        elif state_mao_player == 2 and timer_idle_player > 40:
            state_mao_player = 1
            timer_idle_player = 0
        elif state_mao_player > 2 and timer_idle_player > 60:
            state_mao_player = 1
            timer_idle_player = 0
        elif state_mao_player == 3:
            animacao_tesoura(True)
        elif state_mao_player == 4:
            animacao_papel(True)
        elif state_mao_player == 5 or state_mao_player == 7:
            animacao_pedra(True)

        if state_mao_enemy == 1 and timer_idle_enemy > 40:
            state_mao_enemy = 2
            timer_idle_enemy = 0
        elif state_mao_enemy == 2 and timer_idle_enemy > 40:
            state_mao_enemy = 1
            timer_idle_enemy = 0
        elif state_mao_enemy > 2 and timer_idle_enemy > 60:
            state_mao_enemy = 2
            timer_idle_enemy = 0
        elif state_mao_enemy == 3:
            animacao_tesoura(False)
        elif state_mao_enemy == 4:
            animacao_papel(False)
        elif state_mao_enemy == 5 or state_mao_enemy == 7:
            animacao_pedra(False)

        screen.fill(white)
        screen.blit(back_batalha, (0,0))

        pygame.draw.rect(screen,gray,(50,520,200,60))
        button_pedra = pygame.draw.rect(screen, black, (50,520,200,60),3)
        texto = fontUI.render("PEDRA", True, white)
        screen.blit(texto, (105,540))
        pygame.draw.rect(screen, gray, (300,520,200,60))
        button_papel = pygame.draw.rect(screen, black, (300,520,200,60),3)
        texto = fontUI.render("PAPEL", True, white)
        screen.blit(texto, (360,540))
        pygame.draw.rect(screen, gray, (550,520,200,60))
        button_tesoura = pygame.draw.rect(screen, black, (550,520,200,60),3)
        texto = fontUI.render("TESOURA", True, white)
        screen.blit(texto, (590,540))

        if state_mao_player == 1:
            screen.blit(mao_player_idle1,(pos_player))
        elif state_mao_player == 2:
            screen.blit(mao_player_idle2,(pos_player))
        elif state_mao_player == 3:
            screen.blit(mao_player_atk1,(pos_player))
        elif state_mao_player == 4:
            screen.blit(mao_player_atk2,(pos_player))
        elif state_mao_player == 5:
            screen.blit(mao_player_atk3,(pos_player))
        elif state_mao_player == 6:
            screen.blit(mao_player_dmg,(pos_player))
        elif state_mao_player == 7:
            screen.blit(mao_player_def,(pos_player))

        if state_mao_enemy == 1:
            screen.blit(mao_enemy_idle1,(pos_enemy))
        elif state_mao_enemy == 2:
            screen.blit(mao_enemy_idle2,(pos_enemy))
        elif state_mao_enemy == 3:
            screen.blit(mao_enemy_atk1,(pos_enemy))
        elif state_mao_enemy == 4:
            screen.blit(mao_enemy_atk2,(pos_enemy))
        elif state_mao_enemy == 5:
            screen.blit(mao_enemy_atk3,(pos_enemy))
        elif state_mao_enemy == 6:
            screen.blit(mao_enemy_dmg,(pos_enemy))
        elif state_mao_enemy == 7:
            screen.blit(mao_enemy_def,(pos_enemy))

        pygame.display.update()
        timer_idle_player += 1
        timer_idle_enemy += 1
        clock.tick(60)

def help():
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                quit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if button_menu.collidepoint(evento.pos):
                    pygame.mixer.Sound.play(menuSFX)
                    menu()

        screen.fill(white)
        screen.blit(back_menu, (0,0))
        texto = fontMenu.render("Regras", True, white)
        screen.blit(texto, (10,10))
        texto = font.render("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA", True, white)
        screen.blit(texto, (10,150))
        button_menu = pygame.draw.rect(screen, black, (400,520,300,60))
        texto = fontUI.render("Voltar para o Menu", True, white)
        screen.blit(texto, (440,540))

        pygame.display.update()
        clock.tick(60)

def menu(): 
    while True: 
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                quit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if button_start.collidepoint(evento.pos):
                    pygame.mixer.Sound.play(menuSFX)
                    main()
                elif button_help.collidepoint(evento.pos):
                    pygame.mixer.Sound.play(menuSFX)
                    help()

        screen.fill(white)
        screen.blit(back_menu, (0,0))
        texto = fontMenu.render("Bem Vindo à Batalha PoucaMão", True, white)
        screen.blit(texto, (10,10))
        button_start = pygame.draw.rect(screen, black, (50,520,300,60))
        texto = fontUI.render("JOGAR", True, white)
        screen.blit(texto, (140,540))
        button_help = pygame.draw.rect(screen, black, (400,520,300,60))
        texto = fontUI.render("Ajuda", True, white)
        screen.blit(texto, (520,540))

        pygame.display.update()
        clock.tick(60)

menu()