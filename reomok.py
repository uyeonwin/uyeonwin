import pygame

pygame.init()

background = pygame.display.set_mode((700,762))
pygame.display.set_caption("omok")

#게임판 생성
board = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]


#변수정의
stone = 1
x = 0
y = 0
cursor_x = 0
cursor_y = 0

#고양이그리기
def draw_neko():
    for y in range(16):
        for x in range(16):
            if board[y][x] > 0:
                background.blit(image_omok[board[y][x]], (x-28,y+28))

#마우스 위치 보드판형식으로 바꾸기
def mousepos() :
    global mouse_x, mouse_y, x, y
    if 14 <= mouse_x and mouse_x < 14 + 42 * 16 and 76 <= mouse_y and mouse_y < 76 + 42 * 16:
        x = int((mouse_x - 14) / 42)
        y = int((mouse_y - 76) / 42)

#이미지들 목록
image_bg = pygame.image.load("image/scorebg.png")
image_omok = [
    None,
    pygame.image.load("image/stone1.png"),
    pygame.image.load("image/stone2.png"),
    pygame.image.load("image/stone3.png"),
    pygame.image.load("image/score0.png"),
    pygame.image.load("image/score1.png"),
    pygame.image.load("image/score2.png"),
    pygame.image.load("image/score3.png"),
    pygame.image.load("image/cursor.png")
]

#게임 실행
play = True
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
        if event.type == pygame.MOUSEMOTION:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            mousepos()
            cursor_x = x*42+35-29
            cursor_y = y*42+97-29
        if event.type == pygame.MOUSEBUTTONDOWN :
            if event.button == 1 :
                if stone == 1 :
                    board[y][x] = 1
                    background.blit(image_omok[stone], (cursor_x, cursor_y))
                    pygame.display.update()
                    stone = 2
                elif stone == 2 :
                    board[y][x] = 2
                    background.blit(image_omok[stone], (cursor_x, cursor_y))
                    pygame.display.update()
                    stone = 1

    background.blit(image_bg, (0,0))
    background.blit(image_omok[8], (cursor_x, cursor_y))
    background.blit(image_omok[stone], (cursor_x, cursor_y))
    pygame.display.update()

pygame.quit()
