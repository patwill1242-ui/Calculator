import pygame,sys

pygame.init()

screen = pygame.display.set_mode((300,600))

while True:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()  

