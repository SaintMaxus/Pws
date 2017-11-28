import pygame
import random
import math

#kleuren
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
PINK = (255, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
#beeldzaken
size = (700, 700)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("main game")
mainscreen = True
levelselect = False
level_1 = False
level_2 = False
game_over = False
clock = pygame.time.Clock()
pygame.font.init()
score = 0
#alles van de ball
ball_x = 335
ball_y = 540
ball_radius = 10
ball_color = GREEN
ball_speed_total = 6
ball_speed_x = random.randrange(-1,1,2) * (math.sqrt((ball_speed_total **2) - (random.randrange(0, 35, 1))))
ball_speed_y = -(math.sqrt((ball_speed_total **2) - abs((ball_speed_x **2))))
ball_change = 3
def ball(screen, x, y):
    pygame.draw.circle(screen, ball_color, [int(x), int(y)], ball_radius, 0)

#ball en paddle collision dingen
ball_change = 3
speed_change = 0

#alles van de paddle
paddle_x = 310
paddle_y = 550
paddle_width = 80
paddle_height = 5
paddle_speed_x = 0
paddle_speed_y = 0
def paddle(screen, x, y):
    pygame.draw.rect(screen, BLACK,[x, y, paddle_width, paddle_height], 2)
#alles van level2
#alles van de paddle2
paddle2_x = 310
paddle2_y = 50

#alles van de verticale paddles
def paddlevertical(screen, x, y):
    pygame.draw.rect(screen, BLACK,[x, y, paddlevert_width, paddlevert_height], 2)
paddle3_x = 50
paddle3_y = 260
paddle4_x = 630
paddle4_y = 260
paddlevert_width = 5
paddlevert_height = 80
    
#alles van de bricks
brick_x = 320
brick_y = 280
brick_width = 40
brick_height = 40
brick_color = PINK
def brick(screen, x, y):
    pygame.draw.rect(screen, brick_color, [x, y, brick_width, brick_height], 0)

#walls
wall_width = 15
wall_color = BLACK
wall_height = 700
wall1_x = 0
wall1_y = 0
wall2_x = 685
wall2_y = 0
wall3_y = 610
def wallvert(screen, x, y):
    pygame.draw.rect(screen, wall_color, [x, y, wall_width, wall_height], 0)
def wallhorz(screen, x, y):
    pygame.draw.rect(screen, wall_color, [x, y, wall_height, wall_width], 0)

#achtergrondboom
def drawTree(x1, y1, angle, depth, color):
    if depth:
        x2 = x1 + int(math.cos(math.radians(angle)) * depth * 10.0)
        y2 = y1 + int(math.sin(math.radians(angle)) * depth * 10.0)
        pygame.draw.line(screen, color, (x1, y1), (x2, y2), 2)
        drawTree(x2, y2, angle - 20, depth - 1, color)
        drawTree(x2, y2, angle + 20, depth - 1, color)
        
while mainscreen:
    lettertype=pygame.font.SysFont("comicsansms", 50)
    lettertype2=pygame.font.SysFont("comicsansms", 30)
    lettertype3=pygame.font.SysFont("comicsansms",22)
    label=lettertype.render("WELCOME TO THE GAME", 1, RED)
    label2=lettertype2.render("Press any key to continue", 1, RED)
    label3=lettertype3.render("Door: Max Minnema 6B",1,PINK)
    
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
                mainscreen = False
                levelselect = True
    screen.fill(BLACK)
    drawTree(350, 550, -90, 9, WHITE)
    screen.blit(label,(40,50))
    screen.blit(label2,(160,480))
    screen.blit(label3,(220,550))
    pygame.display.flip()
    
#levelselect   
while levelselect:
    lettertype = pygame.font.SysFont("comicsansms", 30)
    label = lettertype.render("Press the number of the level", 1, RED)
    label2 = lettertype.render("you want to play", 1, RED)
    label3 = lettertype.render("LEVEL 1: 1 BRICK", 1, RED)
    label4 = lettertype.render("LEVEL 2: 4 PLATFORMS 1 BRICK", 1, RED)
    for event in pygame.event.get():
        #zo kan je het spel stoppen
        if event.type == pygame.QUIT:
            levelselect = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                levelselect = False
                level_1 = True
            elif event.key == pygame.K_2:
                levelselect = False
                level_2 = True
    screen.fill(BLACK)
    drawTree(350, 700, -90, 9, WHITE)
    screen.blit(label,(50,50))
    screen.blit(label2,(50,80))
    screen.blit(label3,(50,150))
    screen.blit(label4,(50,190))
    pygame.display.flip()

#level 1 mainloop
while level_1:
    #als er een event is kijkt dit welke event en geeft dan iets niews
    for event in pygame.event.get():
        #zo kan je het spel stoppen
        if event.type == pygame.QUIT:
            level_1 = False
        #als je een toets indrukt
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                paddle_speed_x = -5
            elif event.key == pygame.K_RIGHT:
                paddle_speed_x = 5
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                paddle_speed_x = 0

    #als de bal tegen een muur botst
    if ball_y > 600:
        level_1 = False
        game_over = True
    if ball_y < 25:
        ball_speed_y = -ball_speed_y
    if ball_x < 25:
        ball_speed_x = -ball_speed_x
    if ball_x > 675:
        ball_speed_x = -ball_speed_x


    #positie van de bal en paddle
    ball_y = ball_y + ball_speed_y
    ball_x = ball_x + ball_speed_x        
    paddle_x = paddle_x + paddle_speed_x

    #hitboxen van alle voorwerpen
    ball_rect = pygame.Rect(ball_x-ball_radius, ball_y-ball_radius, ball_radius*2,ball_radius*2)
    paddle_rect = pygame.Rect(paddle_x, paddle_y, paddle_width, paddle_height)

    brick_rect1 = pygame.Rect(brick_x, brick_y, 2, brick_height)
    brick_rect2 = pygame.Rect(brick_x, brick_y, brick_width, 2)
    brick_rect3 = pygame.Rect(brick_x, brick_y + brick_height - 2, brick_width, 2)
    brick_rect4 = pygame.Rect(brick_x + brick_width - 2, brick_y, 2, brick_height)
    #als de bal ergens tegen aanbotst
    if ball_rect.colliderect(paddle_rect):
        collisionpoint = -(paddle_width/2)
        collisionpoint += (ball_x - paddle_x)
        speed_change = (collisionpoint/(paddle_width/2)) * ball_change
        ball_speed_y = -(abs((ball_speed_y + speed_change)))
        ball_speed_x = ball_speed_x + speed_change
    

    if ball_rect.colliderect(brick_rect1):
        ball_speed_x = -ball_speed_x
        score += 1
    if ball_rect.colliderect(brick_rect2):
        ball_speed_y = -ball_speed_y
        score += 1
    if ball_rect.colliderect(brick_rect3):
        ball_speed_y = -ball_speed_y
        score += 1
    if ball_rect.colliderect(brick_rect4):
        ball_speed_x = -ball_speed_x
        score += 1
    #score
    lettertype=pygame.font.SysFont("comicsansms", 30)
    label3=lettertype.render("Score: " + str(int(score)), 1, (0, 0, 0))
    
    #uitvoeren van de functies die alle voorwerpen tekenen en maken
    screen.fill(WHITE)
    drawTree(340, 610, -90, 9,BLACK)
    paddle(screen, paddle_x, paddle_y)
    wallvert(screen, wall1_x, wall1_y)
    wallvert(screen, wall2_x, wall2_y)
    wallhorz(screen, wall1_x, wall2_y)
    wallhorz(screen, wall1_x, wall3_y)
    ball(screen, ball_x, ball_y)
    brick(screen, brick_x, brick_y)
    screen.blit(label3,(20,630))
    pygame.display.flip()
    clock.tick(60)

#level 2 mainloop
while level_2:
    #als er een event is kijkt dit welke event en geeft dan iets niews
    for event in pygame.event.get():
        #zo kan je het spel stoppen
        if event.type == pygame.QUIT:
            level_2 = False
        #als je een toets indrukt
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                paddle_speed_x = -5
            elif event.key == pygame.K_RIGHT:
                paddle_speed_x = 5
            elif event.key == pygame.K_UP:
                paddle_speed_y = -5
            elif event.key == pygame.K_DOWN:
                paddle_speed_y = 5
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                paddle_speed_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                paddle_speed_y = 0
    #als de bal tegen een muur botst
    if ball_y > 600:
        level_2 = False
        game_over = True
    if ball_y < 25:
        level_2 = False
        game_over = True
    if ball_x < 25:
        level_2 = False
        game_over = True
    if ball_x > 675:
        level_2 = False
        game_over = True


    #positie van de bal en paddle
    ball_y = ball_y + ball_speed_y
    ball_x = ball_x + ball_speed_x        
    paddle_x = paddle_x + paddle_speed_x
    paddle2_x = paddle2_x + paddle_speed_x
    paddle3_y = paddle3_y + paddle_speed_y
    paddle4_y = paddle4_y + paddle_speed_y
    #hitboxen van alle voorwerpen
    ball_rect = pygame.Rect(ball_x-ball_radius, ball_y-ball_radius, ball_radius*2,ball_radius*2)
    paddle_rect = pygame.Rect(paddle_x, paddle_y, paddle_width, paddle_height)
    paddle2_rect = pygame.Rect(paddle2_x, paddle2_y, paddle_width, paddle_height)
    paddle3_rect = pygame.Rect(paddle3_x, paddle3_y, paddlevert_width, paddlevert_height)
    paddle4_rect = pygame.Rect(paddle4_x, paddle4_y, paddlevert_width, paddlevert_height)
    brick_rect1 = pygame.Rect(brick_x, brick_y, 2, brick_height)
    brick_rect2 = pygame.Rect(brick_x, brick_y, brick_width, 2)
    brick_rect3 = pygame.Rect(brick_x, brick_y + brick_height - 2, brick_width, 2)
    brick_rect4 = pygame.Rect(brick_x + brick_width - 2, brick_y, 2, brick_height)
    #als de bal ergens tegen aanbotst
    if ball_rect.colliderect(paddle_rect):
        collisionpoint = -(paddle_width/2)
        collisionpoint += (ball_x - paddle_x)
        speed_change = (collisionpoint/(paddle_width/2)) * ball_change
        ball_speed_y = -(abs((ball_speed_y + speed_change)))
        ball_speed_x = ball_speed_x + speed_change
    if ball_rect.colliderect(paddle2_rect):
        collisionpoint = -(paddle_width/2)
        collisionpoint += (ball_x - paddle_x)
        speed_change = (collisionpoint/(paddle_width/2)) * ball_change
        ball_speed_y = (abs((ball_speed_y + speed_change)))
        ball_speed_x = ball_speed_x + speed_change
        
    if ball_rect.colliderect(paddle3_rect):
        collisionpoint = -(paddle_width/2)
        collisionpoint += (ball_y - paddle3_y)
        speed_change = (collisionpoint/(paddle_width/2)) * ball_change
        ball_speed_x = (abs((ball_speed_x + speed_change)))
        ball_speed_y = ball_speed_y + speed_change
        
    if ball_rect.colliderect(paddle4_rect):
        collisionpoint = -(paddle_width/2)
        collisionpoint += (ball_y - paddle4_y)
        speed_change = (collisionpoint/(paddle_width/2)) * ball_change
        ball_speed_x = -(abs((ball_speed_x + speed_change)))
        ball_speed_y = ball_speed_y + speed_change
        
    if ball_rect.colliderect(brick_rect1):
        ball_speed_x = -ball_speed_x
        score += 1
    if ball_rect.colliderect(brick_rect2):
        ball_speed_y = -ball_speed_y
        score += 1
    if ball_rect.colliderect(brick_rect3):
        ball_speed_y = -ball_speed_y
        score += 1
    if ball_rect.colliderect(brick_rect4):
        ball_speed_x = -ball_speed_x
        score += 1
    #score
    lettertype=pygame.font.SysFont("comicsansms", 30)
    label3=lettertype.render("Score: " + str(int(score)), 1, (0, 0, 0))
    
    #uitvoeren van de functies die alle voorwerpen tekenen en maken
    screen.fill(WHITE)
    drawTree(340, 610, -90, 9,BLACK)
    paddle(screen, paddle_x, paddle_y)
    paddle(screen, paddle2_x, paddle2_y)
    paddlevertical(screen, paddle3_x, paddle3_y)
    paddlevertical(screen, paddle4_x, paddle4_y)
    wallvert(screen, wall1_x, wall1_y)
    wallvert(screen, wall2_x, wall2_y)
    wallhorz(screen, wall1_x, wall2_y)
    wallhorz(screen, wall1_x, wall3_y)
    ball(screen, ball_x, ball_y)
    brick(screen, brick_x, brick_y)
    screen.blit(label3,(20,630))
    pygame.display.flip()
    clock.tick(60)    
#game over loop  
while game_over:
    lettertype=pygame.font.SysFont("comicsansms", 50)
    lettertype2=pygame.font.SysFont("comicsansms", 30)
    label=lettertype.render("GAME OVER", 1, RED)
    label2=lettertype2.render("Press any key to QUIT", 1, RED)
    label3=lettertype2.render("Your score was: " + str(int(score)), 1, RED)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
                
                game_over = False
    screen.fill(BLACK)
    drawTree(350, 550, -90, 9, WHITE)
    screen.blit(label,(200,50))
    screen.blit(label2,(180,490))
    screen.blit(label3, (200,450))
    pygame.display.flip()
pygame.quit()






