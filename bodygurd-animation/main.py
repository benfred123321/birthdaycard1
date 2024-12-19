import pygame
import time 

pygame.init()

WIDTH=600
HIEGHT=600 
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("birthdaycard")

image1 = pygame.image.load("backgroundone.jpg")
image1 = pygame.transform.scale(image1,(600,600))

while True:
    #in pygame in order to use image we have to paform two steps 
    #step 1 - Loading
    #image1 = pygame.image.load("backgroundone.jpg")
    #screen.fill("white")
    #step 2 displaying
    screen.blit(image1,(0,0))

    #adding text to the image .
    #1specifing the font that we want 
    font = pygame.font.SysFont("Times New Roman",77)
    #2 aplying the font to the text
    text = font.render("Happy",True,"purple")
    text2 = font.render("Birthday :)",True,"purple")
    #3 displayin the text
    screen.blit(text,(190,150))
    screen.blit(text2,(140,350))
    pygame.display.update()
    time.sleep(2)

    image2 = pygame.image.load("backgroundtwo.jpg")
    screen.blit(image2,(0,0))
    font2 = pygame.font.SysFont("Arial",20)
    text3 = font.render("Dear: You",True,"red")
    text4 = font.render("Happy Birthday hope",True,"orange")
    text5 = font.render("you have a",True,"yellow")
    text6 = font.render("wonderful day",True,"green")
    
    screen.blit(text3,(100,105))
    screen.blit(text4,(100,195))
    screen.blit(text5,(100,245))
    screen.blit(text6,(100,305))
    pygame.display.update()
    time.sleep(2)

    image3 = pygame.image.load("backround3.jpg")
    screen.fill("purple")
    screen.bilt(image3,(0,0))
    font2 = pygame.font.SysFont("Arial",20)
    text7 = font.render("from your",True,"blue")
    text8 = font.render("bestist pal",True,"indigo")
    text9 = font.render("Me!",True,"violet")
    screen.blit(text7,(100,50))
    screen.blit(text8,(100,100))
    screen.blit(text9,(10,50))
    pygame.display.update()
    time.sleep(5)
