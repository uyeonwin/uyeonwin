import pygame

pygame.init()

background = pygame.display.set_mode((700,762))
pygame.display.set_caption("dfd")

image_bg = pygame.image.load("image/scorebg.png")

play = True
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
    background.blit(image_bg, (0,0))
    pygame.display.update()

pygame.quit()
