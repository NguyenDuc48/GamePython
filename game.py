import pygame
from random import randint

pygame.init()

screen = pygame.display.set_mode((650,650))
pygame.display.set_caption("NTĐ_K66A5_HUS")
running = True
clock = pygame.time.Clock()
lx = pygame.image.load("lx.png")

background = pygame.image.load("HUS.png")
background = pygame.transform.scale(background,(650,650))
metor = pygame.image.load("me.png")
plane = pygame.image.load("new.png")
tube1_x = randint(500,600)
tube2_x = randint(700,900)
tube3_x = randint(1300,1400)
tube1_inv_x = randint(700,800)
tube2_inv_x = randint(900,1000)
tube3_inv_x = randint(1100,1200)
meteo1_x = randint(600,700)
meteo2_x = randint(1050,1100)

tube1_y = randint(-100,250)
tube2_y = randint(-100,250)
tube3_y = randint(-100,250)
meteo1_y = 0
meteo2_y = 0


tube1_height = randint(100,150)
tube2_height = randint(100,150)
tube3_height = randint(100,150)

bird_x = 40
bird_y = 400
BIRD_WIDTH = 80
BIRD_HEIGHT = 80
plane = pygame.transform.scale(plane,(BIRD_WIDTH,  BIRD_HEIGHT))

metor = pygame.transform.scale(metor,(80,80))
meteo_drop_velocity = 2
GRAVITY = 0.5
TUBE_WIDTH = 100
DISTANT = 250
TUBE_VELOCITY = 2.5

BLUE = (0,0,255)
GREEN = (0,255,0)
RED = (255,0,0)

score  = 0
font = pygame.font.SysFont('sans', 20)

tube1_pass = False
tube2_pass = False
tube3_pass = False
tube1_inv_pass = False
tube2_inv_pass = False
tube3_inv_pass = False
pausing = False
sound = pygame.mixer.Sound('faded.mp3')
pygame.mixer.Sound.play(sound)
while running:
    clock.tick(60)
    screen.fill(BLUE)
    screen.blit(background,(0,0))
    

    img1 = pygame.transform.scale(lx,(TUBE_WIDTH, tube1_height))
    img2 = pygame.transform.scale(lx,(TUBE_WIDTH, tube2_height))
    img3 = pygame.transform.scale(lx,(TUBE_WIDTH, tube3_height))
    img4 = pygame.transform.scale(lx,(TUBE_WIDTH,  700 - DISTANT -tube1_height) )
    img5 = pygame.transform.scale(lx,(TUBE_WIDTH,  700 - DISTANT -tube2_height) )
    img6 = pygame.transform.scale(lx,(TUBE_WIDTH,  700 - DISTANT -tube3_height) )

    meteo1 = screen.blit(metor, (meteo1_x, meteo1_y))
    meteo2 = screen.blit(metor, (meteo2_x, meteo2_y))

    Tube1 = screen.blit(img1,(tube1_x,tube1_y))
    Tube2 = screen.blit(img2,(tube2_x,tube2_y))
    Tube3 = screen.blit(img3,(tube3_x,tube3_y))

    Tube1_int = screen.blit(img4,(tube1_inv_x,tube1_height + DISTANT ))
    Tube2_int = screen.blit(img5,(tube2_inv_x,tube2_height + DISTANT ))
    Tube3_int = screen.blit(img6,(tube3_inv_x,tube3_height + DISTANT ))

    

    #Tube1 = pygame.draw.rect(screen, GREEN, (tube1_x, tube1_y, TUBE_WIDTH, tube1_height)  )
    

    # Tube1_int = pygame.draw.rect(screen, GREEN, (tube1_inv_x, tube1_height + DISTANT , TUBE_WIDTH, 400 - DISTANT -tube1_height)  )
    # Tube2_int = pygame.draw.rect(screen, GREEN, (tube2_inv_x, tube2_height + DISTANT , TUBE_WIDTH, 400 - DISTANT -tube2_height)  )
    # Tube3_int = pygame.draw.rect(screen, GREEN, (tube3_inv_x, tube3_height + DISTANT , TUBE_WIDTH, 400 - DISTANT -tube3_height)  )

    bird_rect = screen.blit(plane, (bird_x, bird_y))
    tube2_x-=TUBE_VELOCITY
    tube3_x-=TUBE_VELOCITY
    tube1_x-=TUBE_VELOCITY
    meteo1_x-=TUBE_VELOCITY
    if meteo1_x < 680:
   
        meteo1_y+=2.5
    meteo2_x-=TUBE_VELOCITY
    if meteo2_x < 680:
        meteo2_y+=2.5
    
    

    score_txt =  font.render("Score "+ str(score) , True , (255,0,0))
    screen.blit(score_txt, (5,5))
    #bird_y+= bird_drop_velocity
    #bird_drop_velocity+= GRAVITY

    if bird_x > tube1_x + TUBE_WIDTH and tube1_pass == False:
        score+=1
        tube1_pass = True
    if bird_x > tube2_x + TUBE_WIDTH and tube2_pass == False:
        score+=1
        tube2_pass = True
    if bird_x > tube3_x + TUBE_WIDTH and tube3_pass == False:
        score+=1
        tube3_pass = True
    if meteo1_y > 630:
        meteo1_y = randint(-200,0)
        meteo1_x = randint(1200,1300)
    if meteo2_y > 630:
        meteo2_y = 0
        meteo2_x = randint(1200,1300)
    if tube1_x < -50:
        tube1_x = randint(1400,1600)
        tube1_height = randint(100,400)
        tube1_pass =False
    if tube2_x < -50:
        tube2_x = randint(1400,1600)
        tube2_height = randint(100,400)
        tube2_pass =False

    if tube3_x < -50:
        tube3_x = randint(1400,1600)
        tube3_height = randint(200,300)
        tube3_pass = False

    if tube1_inv_x < -50:
        tube1_x = randint(1300,1600)
        tube1_height = randint(200,300)
        tube1_pass =False
    if tube2_inv_x < -50:
        tube1_x = randint(1300,1600)
        tube1_height = randint(200,300)

        tube1_pass =False
    if tube3_inv_x < -50:
        tube1_x = randint(1300,1600)
        tube1_height = randint(100,400)
        tube1_pass =False
    
    for i in [Tube1, Tube1_int, Tube2, Tube2_int, Tube3, Tube3_int, meteo1, meteo2 ]:
             if ( bird_rect.colliderect(i)):
                meteo_drop_velocity = 0 
                TUBE_VELOCITY = 0
                result_txt = font.render("Your Score: " + str(score), True, (255,0,0) )
                screen.blit(result_txt, (200,50))
                press_space = font.render("Press 'c' to continue ", True, (255,0,0))
                screen.blit(press_space, (200,100))
                pausing = True
                
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c and pausing == True:
                    tube1_x = 600
                    tube2_x = 900
                    tube3_x = 1200                
                    bird_x = 250
                    bird_y = 250
                    meteo_drop_velocity =2
                    TUBE_VELOCITY = 3
                    
                    pausing = False
                    score = 0 
            
            if pausing ==False:
                if event.key == pygame.K_UP:
                    bird_y-=40
                if event.key == pygame.K_DOWN:
                    bird_y+=40
                if event.key == pygame.K_RIGHT:
                    bird_x+=40
                if event.key == pygame.K_LEFT:
                    bird_x-=40
               

    pygame.display.flip()


pygame.quit()