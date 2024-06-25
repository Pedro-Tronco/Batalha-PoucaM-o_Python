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
font = pygame.font.SysFont("comicsans",28)
fontMenu = pygame.font.SysFont("comicsans",55)
fontUI = pygame.font.SysFont("roboto",35)
pygame.mixer.music.load("assets\Battle! Gym Leader - Remix Cover (Pokémon Black and White) - 128.mp3")

black = (0,0,0)
white = (255,255,255)

def start(): 
    pygame.mixer.music.play(-1)
    while True: 
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                quit()

        screen.fill(white)
        screen.blit(back_menu, (0,0))

        pygame.display.update()
        clock.tick(60)

start()