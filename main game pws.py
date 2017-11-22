import pygame

#kleuren
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
PINK = (255, 0, 255)
GREEN = (0, 255, 0)
#beeldzaken
size = (700, 700)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("main game")
mainscreen = True
levelselect = False
running = False
game_over = False
clock = pygame.time.Clock()
pygame.font.init()
score = 0
#alles van de ball
ball_x = 330
ball_y = 540
ball_radius = 10
ball_color = GREEN
ball_speed_x = 0
ball_speed_y = -3
def ball(screen, x, y):
    pygame.draw.circle(screen, ball_color, [int(x), int(y)], ball_radius, 0)

#alles van de paddle
paddle_x = 310
paddle_y = 550
paddle_width = 80
paddle_height = 5
paddle_speed_x = 0
paddle_speed_y = 0
def paddle(screen, x, y):
    pygame.draw.rect(screen, BLACK,[x, y, paddle_width, paddle_height], 2)
    
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

while mainscreen:
    lettertype=pygame.font.SysFont("comicsansms", 50)
    lettertype2=pygame.font.SysFont("comicsansms", 30)
    label=lettertype.render("WELCOME TO THE GAME", 1, (255, 0, 0))
    label2=lettertype2.render("Press any key to continue", 1, (255, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
                mainscreen = False
                levelselect = True
    screen.fill(BLACK)
    screen.blit(label,(40,250))
    screen.blit(label2,(170,450))
    pygame.display.flip()
    
#levelselect   
while levelselect:
    lettertype = pygame.font.SysFont("comicsansms", 30)
    label = lettertype.render("Press the number of the level", 1, (255, 0, 0))
    label2 = lettertype.render("you want to play", 1, (255, 0, 0))
    label3 = lettertype.render("LEVEL 1: ONE BRICK", 1, (255, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                levelselect = False
                running = True
    screen.fill(BLACK)
    screen.blit(label,(50,50))
    screen.blit(label2,(50,80))
    screen.blit(label3,(50,150))
    pygame.display.flip()

#oneindige mainloop om het spel door te laten gaan
while running:
    #als er een event is kijkt dit welke event en geeft dan iets niews
    for event in pygame.event.get():
        #zo kan je het spel stoppen
        if event.type == pygame.QUIT:
            running = False
        #als je een toets indrukt
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                paddle_speed_x = -3
            elif event.key == pygame.K_RIGHT:
                paddle_speed_x = 3

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                paddle_speed_x = 0

    #als de bal tegen een muur botst
    if ball_y > 600:
        running = False
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
        ball_speed_y = -ball_speed_y

    if ball_rect.colliderect(brick_rect1):
        ball_speed_x = -ball_speed_x
        score += 0.5
    if ball_rect.colliderect(brick_rect2):
        ball_speed_y = -ball_speed_y
        score += 0.5
    if ball_rect.colliderect(brick_rect3):
        ball_speed_y = -ball_speed_y
        score += 0.5
    if ball_rect.colliderect(brick_rect4):
        ball_speed_x = -ball_speed_x
        score += 0.5
    #score
    lettertype=pygame.font.SysFont("comicsansms", 30)
    label3=lettertype.render("Score: " + str(int(score)), 1, (0, 0, 0))
    
    #uitvoeren van de functies die alle voorwerpen tekenen en maken
    screen.fill(WHITE)
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
#game over loop  
while game_over:
    lettertype=pygame.font.SysFont("comicsansms", 50)
    lettertype2=pygame.font.SysFont("comicsansms", 30)
    label=lettertype.render("GAME OVER", 1, (255, 0, 0))
    label2=lettertype2.render("Press any key to leave", 1, (255, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
                game_over = False
    screen.fill(BLACK)
    screen.blit(label,(200,250))
    screen.blit(label2,(180,450))
    pygame.display.flip()
pygame.quit()


