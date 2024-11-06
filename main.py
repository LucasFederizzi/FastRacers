import pygame
import random



pygame.init()
tamanho = (1061,800)
clock = pygame.time.Clock()
tela = pygame.display.set_mode( tamanho )
icone = pygame.image.load("Recursos/logo.ico")
pygame.display.set_icon(icone)
pygame.display.set_caption("Corrida Maluca")
branco = (255,255,255)
preta = (0,0,0)
verde = (0,255,0)
azulP = (0,0,255)
azulA = (20,170,255)




fundo = pygame.image.load("Recursos/interlagos4Block.png")
carro1 = pygame.image.load("Recursos/sennaMCLaren.png")
carro2 = pygame.image.load("Recursos/carro2.png")
carro3 = pygame.image.load("Recursos/prostWilliams.png")
fonte = pygame.font.Font("freesansbold.ttf",60)










distCar12 = 0
distCar13 = 0

distCar21 = 0
distCar23 = 0
 
distCar31 = 0
distCar32 = 0  



movXCar1 = 0
movXCar2 = 0
movXCar3 = 0
posYCar1 = 50
posYCar2 = 270
posYCar3 = 155

vitoria = pygame.mixer.Sound("Recursos/vitoria.mp3")
vitoria.set_volume(0.5)
pygame.mixer.music.load("Recursos/trilha.mp3")
pygame.mixer.music.play(-1) #-1 looping, 1,2 3 vezes
acabou = False
somDaVitoria = False
while True:
    for evento in pygame.event.get(): 
        if evento.type == pygame.QUIT:
            quit()
   
    tela.fill( branco )
    tela.blit(fundo, (0,0))
    tela.blit(carro1, (movXCar1,posYCar1))
    tela.blit(carro2, (movXCar2,posYCar2))
    tela.blit(carro3, (movXCar3,posYCar3))
    
    if not acabou :
        movXCar1 = movXCar1 + 10#random.randint(0,10)
        movXCar2 = movXCar2 + 10#random.randint(0,10)
        movXCar3 = movXCar3 + 10#random.randint(0,10)
    else:
        pygame.mixer.music.stop()
        if somDaVitoria == False:
            pygame.mixer.Sound.play(vitoria)
            somDaVitoria = True
        
    
    if movXCar1 > 1000:
        movXCar1 = 0
        posYCar1 = 450
        
    if movXCar2 > 1000:
        movXCar2 = 0
        posYCar2 = 670

    if movXCar3 > 1000:
        movXCar3 = 0
        posYCar3 = 555
    
    textoVermelho = fonte.render("Vermelho Ganhou!", True, branco)
    textoAmarelo = fonte.render("Amarelo Ganhou!", True, branco)
    textoAzul = fonte.render("Azul ganhou!", True, branco)
    textoEmpate = fonte.render("empatou!!", True, branco)
    
    #if (movXCar3 > 900 and posYCar3 = 555) or (movXCar1 > 900 and posYCar1 = 450) or (movXCar2 > 900 and posYCar2 = 670):
        #if movXCar1 == movXCar2 or movXCar3 == movXCar2 or movXCar1 == movXCar3:
            # tela.blit(textoEmpate, (270,70))



    if posYCar1 == 350 and movXCar1 >= 900 and movXCar1 > movXCar2 and movXCar1 > movXCar3:
        tela.blit(textoVermelho, (270,70))
        acabou = True
        
    elif posYCar2 == 670 and movXCar2 >= 900 and movXCar2 > movXCar1 and movXCar2 > movXCar3:
        tela.blit(textoAmarelo, (270,180))
        acabou = True
    
    elif posYCar3 == 555 and movXCar3 >= 900 and movXCar3 > movXCar1 and movXCar3 > movXCar2:
        tela.blit(textoAzul, (270,480))
        acabou = True


    

    ganhandoSenna = fonte.render("Ayrton senna liderando a corrida!", True, verde)
    ganhandoProst = fonte.render("Prost está em primeiro lugar", True, azulP)
    ganhandoAlonso = fonte.render("Alonso em primeiro pela Renault", True, azulA)

    if movXCar1 > movXCar2 and movXCar1 > movXCar3:
        tela.blit(ganhandoSenna, (100,100))

    elif movXCar2 > movXCar1 and movXCar2 > movXCar3:
        tela.blit(ganhandoProst, (100,100))

    elif movXCar3 > movXCar1 and movXCar3 > movXCar2:
        tela.blit(ganhandoAlonso, (100,100))
    




    
    pygame.display.update()
    clock.tick(60)
pygame.quit()
    
