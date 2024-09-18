import pygame

pygame.init()

background = pygame.display.set_mode((700,762))
pygame.display.set_caption("dfd")

image_bg = pygame.image.load("image/scorebg.png")
image_omok = [
    None,
    pygame.image.load("image/stone1.png"),
    pygame.image.load("image/stone2.png"),
    pygame.image.load("image/stone3.png"),
    pygame.image.load("image/score0.png"),
    pygame.image.load("image/score1.png"),
    pygame.image.load("image/score2.png"),
    pygame.image.load("image/score3.png")
]

play = True
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
        if event.type == pygame.MOUSEMOTION:
            mouse_x, mouse_y = pygame.mouse.get_pos()
    background.blit(image_bg, (0,0))
    pygame.display.update()

pygame.quit()
