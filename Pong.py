import pygame , sys , random

pygame.init()
pygame.mixer.init()

font=pygame.font.Font(pygame.font.get_default_font(),20)

clock=pygame.time.Clock()

height=700
width=400


def Ball_anim():
    global Ball_speed_x,Ball_speed_y
    Ball.x+=Ball_speed_x
    Ball.y+=Ball_speed_y
    if Ball.top<=0 or Ball.bottom>=width :
        Ball_speed_y*=-1
    if Ball.left<=0 or Ball.right>=height :
        Ball_speed_x*=-1
    if Ball.colliderect(Player):
        Ball_speed_x=random.randrange(0,12,6)
        Ball_speed_y=random.randrange(-6,12,6)
        pygame.mixer.music.play()
    if Ball.colliderect(COM):
        Ball_speed_x=random.randrange(-6,6,6)
        Ball_speed_y=random.randrange(-6,12,6)
        pygame.mixer.music.play()


def Player_anim():
    global Player_speed
    Player.y+=Player_speed
    if Player.top<=9 or Player.bottom>=width-9:
        Player_speed=0

        
i,j=0,0
def Ball_Crash():
    global i,j
    if Ball.left<=0 :
        j+=1
    if Ball.right>=height:
        i+=1


def AI():
    global COM_speed
    COM.y+=COM_speed
    if Ball.x<height/2:
        if Ball.y<width/2:
            COM_speed=7
        elif Ball.y>width/2:
            COM_speed=-7
        else :
            COM_speed=0
    if COM.top<=7 or COM.bottom>=width-7:
        COM_speed=0
    if COM.top<=7:
        COM_speed=7
    if COM.bottom>=width-7:
        COM_speed=-7



pygame.mixer.music.load("kick.wav")
pygame.mixer.music.play()



Blue=(0,0,255)
Red=(255,0,0)
Green=(0,255,0)
Gray=(30,30,30)
White=(255,255,255)
Black=(0,0,0)

a=random.randint(20,height-20)
b=random.randint(20,width-20)

Ball=pygame.Rect(a , b , 20,20)
Player=pygame.Rect(10,width/2 - 45 ,4,90)
COM=pygame.Rect(height-14,width/2 - 45 ,4,90)




Ball_speed_x=random.randrange(-6,12,12)
Ball_speed_y=random.randrange(-6,12,6)

Player_speed=0
COM_speed=0


window=pygame.display.set_mode((height,width))







while True :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                Player_speed=-7
            if event.key == pygame.K_DOWN:
                Player_speed=7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                Player_speed=0
            if event.key == pygame.K_DOWN:
                Player_speed=0



    window.fill(Gray)
    scoreP = font.render(f'{i}',False,White)
    scoreC = font.render(f'{j}',False,White)
    window.blit(scoreP,(height/2-50,10))
    window.blit(scoreC,(height/2+40,10))
    pygame.draw.ellipse(window,White,Ball)
    pygame.draw.aaline(window,White,(height/2,0),(height/2,width))
    pygame.draw.rect(window,White,Player)
    pygame.draw.rect(window,White,COM)

    

    Ball_anim()
    Player_anim()
    Ball_Crash()
    AI()

    pygame.display.update()
    clock.tick(60)

# Abdessamad KERROU
