import pygame
import time
import math

from sys import exit
pygame.init()
screna = pygame.display.set_mode((1050,700))
pygame.display.set_caption('arman')
x = 525
y = 325
clock = pygame.time.Clock()



while True:
    screna.fill((0,0,0))


    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    pygame.draw.circle(screna,'Red',(x,y),25)
    
    clock.tick(60)
    a = pygame.key.get_pressed()

    if a[pygame.K_UP] and y > 0:
        y -=20
    if a[pygame.K_DOWN] and y < 650:
        y +=20
    if a[pygame.K_RIGHT] and  x < 1000:
        x +=20
    if a[pygame.K_LEFT] and x > 0 :
        x -=20
    pygame.display.update()
   
#task oclock
pygame.init()
screan = pygame.display.set_mode((1000,650))
pygame.display.set_caption('arman')
photo = pygame.transform.scale(pygame.image.load("/Users/armanbegman/Downloads/clock.png"),(1000,650))
rightarm  = pygame.transform.scale(pygame.image.load("/Users/armanbegman/Downloads/rightarm.png"),(1000,650))
leftarm = pygame.transform.scale(pygame.image.load("/Users/armanbegman/Downloads/leftarm.png"),(1050,650))
clock = pygame.time.Clock()




while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            exit()
    current_time = time.localtime()
    minute = current_time.tm_min
    second = current_time.tm_sec
    minute_angle = minute * 6    + (second / 60) * 6   
    second_angle = second * 6  

    screan.blit(photo,(0,0))
    rotated_rightarm = pygame.transform.rotate(pygame.transform.scale(rightarm, (1050, 650)), -minute_angle)
    rightarmrect = rotated_rightarm.get_rect(center=(458, 300))
    screan.blit(rotated_rightarm, rightarmrect)
    
    rotated_leftarm = pygame.transform.rotate(pygame.transform.scale(leftarm, (40.95, 682.5)), -second_angle)
    leftarmrect = rotated_leftarm.get_rect(center=(1050 // 2, 650 // 2 ))
    screan.blit(rotated_leftarm, leftarmrect)
    

    pygame.display.update()
    clock.tick(60)

#task music
pygame.init()

playlist = []
# музыкалар орналасқан жерге path 
music_folder = "/Users/armanbegman/Desktop/play list"
allmusic = os.listdir(music_folder)

# playlist-қа .mp3 деп аяқталса қосамыз 
for song in allmusic:
    if song.endswith(".mp3"):
        playlist.append(os.path.join(music_folder, song))
# экран бетіне шағатын терезе көлемі, аты
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Darkhan-Juzz")
clock = pygame.time.Clock()



# кнопкалар тұратын жердің фонын жасаймыз, алдымен көлемі, сосын RGB ақ түс
bg = pygame.Surface((500, 200))
bg.fill((255, 255, 255))

# плейлист аты шығып тұратын жер көлемі
font2 = pygame.font.SysFont(None, 20)

# кнопкаларды папкадан енгіземіз
playb = pygame.image.load(os.path.join("/Users/armanbegman/Desktop/play.png"))
pausb = pygame.image.load(os.path.join("/Users/armanbegman/Desktop/pause.png"))
nextb = pygame.image.load(os.path.join("/Users/armanbegman/Desktop/next.png"))
prevb = pygame.image.load(os.path.join("/Users/armanbegman/Desktop/back.png"))

index = 0
aplay = False

pygame.mixer.music.load(playlist[index]) 
pygame.mixer.music.play(0)
aplay = True 

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN: #клавишты басса
            if event.key == pygame.K_SPACE: #егер пробелге тең болса
                if aplay:
                    aplay = False
                    pygame.mixer.music.pause()
                else:
                    aplay = True
                    pygame.mixer.music.unpause()

            if event.key == pygame.K_RIGHT: #егер оң жаққа тең болса
                index = (index + 1) % len(playlist)
                pygame.mixer.music.load(playlist[index])
                pygame.mixer.music.play()

            if event.key == pygame.K_LEFT: #егер сол жаққа тең болса
                index = (index - 1) % len(playlist)
                pygame.mixer.music.load(playlist[index])
                pygame.mixer.music.play()
    #музыка аты шығатын жер 
    text2 = font2.render(os.path.basename(playlist[index]), True, (20, 20, 50))
    
    # әр кнопканың орналасуын, көлемін көрсетеміз
    screen.blit(bg, (155, 500))
    screen.blit(text2, (365, 520))
    playb = pygame.transform.scale(playb, (70, 70))
    pausb = pygame.transform.scale(pausb, (70, 70))
    if aplay:
        screen.blit(pausb, (370, 590))
    else: 
        screen.blit(playb, (370, 590))
    nextb = pygame.transform.scale(nextb, (70, 70))
    screen.blit(nextb, (460, 587))
    prevb = pygame.transform.scale(prevb, (75, 75))
    screen.blit(prevb, (273, 585))

    clock.tick(24)
    pygame.display.update()
