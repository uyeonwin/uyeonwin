import pygame

pygame.init()

background = pygame.display.set_mode((200,100))
pygame.display.set_caption("dfd")

play = True
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False

pygame.quit()