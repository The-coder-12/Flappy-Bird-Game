import pygame
import sys
import random

pygame.init()

#Display dimensions
w = 1000
h = 500
dis = pygame.display.set_mode((w, h))
pygame.display.set_caption("Flappy Bird")
#Background
bg = pygame.image.load("bg.jpeg")
bg1 = pygame.transform.scale(bg, (w, h))
#Bird
flappy = pygame.image.load("bird-removebg-preview.png")
flappy1 = pygame.transform.scale(flappy, (100, 100))


def U_Died(diemsg, color):
    font_style = pygame.font.SysFont("MS Sans Serif", 50)
    content = font_style.render(diemsg, True, color)
    dis.blit(content, (w / 2, h / 2))
def Game():
    run = True
    score = 0
    #Bird dimensions
    birdx = w / 20
    birdy = 100
    birdspeed = 10
    birdvel = 0
    #Pipe
    pipe = pygame.image.load( "pipe-removebg-preview.png" )
    pipew = 150
    pipeh = 300
    pipe1 = pygame.transform.scale( pipe, (pipew, pipeh) )
    pipe2 = pygame.image.load( "pipe-removebg-preview_-_Copy-removebg-preview.png" )
    pipe2w = 150
    pipe2h = random.randint( 100, 250 )
    pipe3 = pygame.transform.scale( pipe2, (pipe2w, pipe2h) )
    pipespeed = 10
    pipex = w
    pipegap = 50
    #Clock
    clock = pygame.time.Clock()
    #Gravity
    gravity = 1
    #Score
    score = 0

    #Fonts
    def Score():
        font = pygame.font.SysFont("MS Sans Serif", 50)
        content = font.render("Score: " + str(score), True, (0, 0, 0))
        dis.blit(content, (50, 50))

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_UP or event.key == pygame.K_SPACE or event.key == pygame.K_w):
                    birdvel = -birdspeed
                if event.key == pygame.K_q:
                    quit()
                if event.key == pygame.K_r:
                    Game()
        #Update bird position
        birdy += birdvel
        birdvel += gravity
        #Update pipe position
        pipex -= pipespeed
        #Collisions
        if (birdx < pipex + pipew and birdx + 100 > pipex and birdy < pipeh and birdy + 100 > pipeh + pipegap or
            birdx < pipe2w + pipe2w and birdx + 100 > pipe2w and birdy < pipe2h and birdy + 100 > pipe2h + pipegap):
            run = False
        if birdy > h or birdy < 0:
            run = False
        #Generating new pipes
        if pipex < -pipew:
            score += 1
            pipex = w
            pipeh = random.randint(250, 400)
            pipe2h = random.randint(100, 250)

        dis.blit(bg1, (0, 0))
        dis.blit(flappy1, (birdx, birdy))
        dis.blit(pipe1, (pipex, pipeh + pipegap))
        dis.blit(pipe3, (pipex, 0))
        pipex -= pipespeed
        Score()
        while not run:
            U_Died("You died! R to Restart or Q to Quit.", (255, 0, 0))
        pygame.display.update()
        clock.tick(30)
Game()