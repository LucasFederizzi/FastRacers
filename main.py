import pygame
import random

pygame.init()
tamanho = (1061,800)
clock = pygame.time.Clock()
tela = pygame.display.set_mode( tamanho )
icone = pygame.image.load("Recursos/logo.ico")
pygame.display.set_icon(icone)
pygame.display.set_caption("F1: 3024")
branco = (255,255,255)
vermelho = (255,0,0)
preta = (0,0,0) 
verde = (0,255,0)
azulP = (0,0,255)
azulA = (20,170,255)
azulRB = (1,11,155)

fundo = pygame.image.load("Recursos/interlagos4Block.png")

carroMax = pygame.image.load("Recursos/carro1.png")

carro1 = pygame.image.load("Recursos/sennaMCLaren.png")
carro2 = pygame.image.load("Recursos/alonsoRenault.png")
carro3 = pygame.image.load("Recursos/prostWilliams.png")
fonte = pygame.font.Font("freesansbold.ttf",60)
fonteMenor = pygame.font.Font("freesansbold.ttf",30)


distCar12 = 0
distCar13 = 0

distCar21 = 0
distCar23 = 0
 
distCar31 = 0
distCar32 = 0  

movXcarMax = -170
posYcarMax = 0

movXCar1 = 125
movXCar2 = 125
movXCar3 = 125
posYCar1 = 50
posYCar2 = 270
posYCar3 = 155

maxMusica = pygame.mixer.Sound("Recursos/maxMusica.mp3")
vitoria = pygame.mixer.Sound("Recursos/vitoria.mp3")
espanha = pygame.mixer.Sound("Recursos/espanha.mp3")
franca = pygame.mixer.Sound("Recursos/frances.mp3")
sennaScream = pygame.mixer.Sound("Recursos/sennaScream.mp3")
vitoria.set_volume(0.5)
sennaScream.set_volume(0.5)
espanha.set_volume(0.5)
franca.set_volume(0.5)
max = random.randint(1,11) #10% chance Max (aka sid da era do gelo) verstapen de aparecer e ganhar instantaneamente
pygame.mixer.music.load("Recursos/trilha.mp3")
pygame.mixer.music.play(-1) #-1 looping, 1,2 3 vezes
acabou = False
vitoriaSenna = False
vitoriaProst = False
vitoriaAlonso = False
vitoriaMax = False

sennaPrimeiro = False
sennaSegundo = False
sennaTerceiro = False
prostPrimeiro = False
prostSegundo = False
prostTerceiro = False
alonsoPrimeiro = False
alonsoSegundo = False
alonsoTerceiro = False


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
    tela.blit(carroMax, (movXcarMax,posYcarMax))
    
    if not acabou :
        movXCar1 = movXCar1 + random.randint(0,10)
        movXCar2 = movXCar2 + random.randint(0,10)
        movXCar3 = movXCar3 + random.randint(0,10)
        if max == 10:
            movXcarMax = movXcarMax + 30


    elif acabou and vitoriaSenna:
        pygame.mixer.music.stop()
        if somDaVitoria == False:
            pygame.mixer.Sound.play(vitoria)
            pygame.mixer.Sound.play(sennaScream)
            somDaVitoria = True

    elif acabou and vitoriaProst:
        pygame.mixer.music.stop()
        if somDaVitoria == False:
            pygame.mixer.Sound.play(franca)
            somDaVitoria = True

    elif acabou and vitoriaAlonso:
        pygame.mixer.music.stop()
        if somDaVitoria == False:
            pygame.mixer.Sound.play(espanha)
            somDaVitoria = True
    elif acabou and vitoriaMax:
        pygame.mixer.music.stop()
        if somDaVitoria == False:
            pygame.mixer.Sound.play(maxMusica)
            somDaVitoria = True

    
    if movXcarMax >1000:
        movXcarMax = 0
        posYcarMax = 570

    if movXCar1 > 1000:
        movXCar1 = 0
        posYCar1 = 450
        
    if movXCar2 > 1000:
        movXCar2 = 0
        posYCar2 = 670

    if movXCar3 > 1000:
        movXCar3 = 0
        posYCar3 = 555
    
    textoSenna = fonte.render("Ayrton Senna do Brasil!!!!"  , True, verde)
    textoAlonso = fonte.render("Fernando Alonso Ganhou!", True, azulA)
    textoProst = fonte.render("Prost ganhou!", True, azulP)
    textoEmpate = fonte.render("empatou!!", True, branco)
    textoMax = fonte.render("MAX VERSTAPPEN DUDUDUDU!!", True, branco)

    ganhandoSenna = fonteMenor.render("Ayrton senna liderando a corrida!", True, verde)
    ganhandoProst = fonteMenor.render("Prost está em primeiro lugar", True, azulP)
    ganhandoAlonso = fonteMenor.render("Alonso em primeiro pela Renault", True, azulA)
    maxOMG = fonteMenor.render("HOLLY SHIT ITS MAX VERSTAPPEN!!!?!", True, azulRB)

    p1 = fonte.render("P1", True, verde)
    p2 = fonte.render("P2", True, azulP)
    p3 = fonte.render("p3", True, vermelho)



    if not acabou and max == 10: #and movXcarMax > movXCar1 and movXcarMax > movXCar2 and movXcarMax > movXCar3:
        tela.blit(maxOMG, (-15,400))

    elif not acabou and max != 10 and movXCar1 > movXCar2 and movXCar1 > movXCar3:
        tela.blit(ganhandoSenna, (100,50))
        tela.blit(p1, ((movXCar1 + 40),(posYCar1 - 30)))

    elif not acabou and max != 10 and movXCar2 > movXCar1 and movXCar2 > movXCar3:
        tela.blit(ganhandoAlonso, (100,50))
        tela.blit(p1, ((movXCar2 + 40),(posYCar2 - 30)))

    elif not acabou and max != 10 and movXCar3 > movXCar1 and movXCar3 > movXCar2:
        tela.blit(ganhandoProst, (100,50))
        tela.blit(p1, ((movXCar3 + 40),(posYCar3 - 30)))



    
    
    if (movXCar3 > 900 and posYCar3 == 555) or (movXCar1 > 900 and posYCar1 == 450) or (movXCar2 > 900 and posYCar2 == 670):
        if movXCar1 == movXCar2 or movXCar3 == movXCar2 or movXCar1 == movXCar3:
             tela.blit(textoEmpate, (270,70))
             acabou = True

    if posYCar1 == 450 and movXCar1 >= 900 and movXCar1 > movXCar2 and movXCar1 > movXCar3:
        tela.blit(textoSenna, (270,70))
        acabou = True
        vitoriaSenna = True
        pygame.mixer.music.stop()
        
    elif posYCar2 == 670 and movXCar2 >= 900 and movXCar2 > movXCar1 and movXCar2 > movXCar3:
        tela.blit(textoAlonso, (270,180))
        acabou = True
        vitoriaAlonso = True
        pygame.mixer.music.stop()

    elif posYCar3 == 555 and movXCar3 >= 900 and movXCar3 > movXCar1 and movXCar3 > movXCar2:
        tela.blit(textoProst, (270,480))
        acabou = True
        vitoriaProst = True
        pygame.mixer.music.stop()

    elif posYcarMax == 570 and movXcarMax >= 900 and movXcarMax > movXCar1 and movXcarMax > movXCar2 and movXcarMax > movXCar3:
        tela.blit(textoMax, (270,480))
        acabou = True
        vitoriaMax = True
        pygame.mixer.music.stop()

    pygame.display.update()
    clock.tick(60)
pygame.quit()