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


#바둑돌그리기
def draw_stone():
    for y in range(16):
        for x in range(16):
            if board[y][x] > 0:
                background.blit(image_omok[board[y][x]], (x*42+35-21, y*42+97-21))
                    
#변수정의
stone = 1
m_x = 0
m_y = 0
cursor_x = 0
cursor_y = 0

#마우스 위치 보드판형식으로 바꾸기
def mousepos() :
    global mouse_x, mouse_y, m_x, m_y
    if 14 <= mouse_x and mouse_x < 14 + 42 * 16 and 76 <= mouse_y and mouse_y < 76 + 42 * 16:
        m_x = int((mouse_x - 14) / 42)
        m_y = int((mouse_y - 76) / 42)

#승리 검증
def check():
    for y in range(16):
        for x in range(2, 14):
            if board[y][x] > 0:
                if board[y][x - 2 ] == board[y][x - 1] == board[y][x] ==  board[y][x + 2] == board[y][x + 1] and board[y][x]!= 3:
                    for a in range (-2,3,1) :
                        board[y][x+a] = 3
                elif board[y][x] == 0 and x <= 10 :
                    x+=3
                elif board[y][x] == 0 and x > 10 :
                    break

    for y in range(2, 14):
        for x in range(16):
            if board[y][x] > 0:
                if board[y - 2][x] == board[y - 1][x] == board[y][x] == board[y + 2][x] == board[y + 1][x] and board[y][x]!= 3:
                    for a in range (-2,3,1) :
                        board[y + a][x] = 3
                elif board[y][x] == 0 and y <= 10 :
                    x+=3
                elif board[y][x] == 0 and y > 10 :
                    break


    for y in range(2,14):
        for x in range(2, 14):
            if board[y][x] > 0:
                if board[y-2][x - 2] == board[y-1][x - 1] == board[y][x] and  board[y+2][x + 2] == board[y+1][x + 1] == board[y][x]:
                    board[y-2][x - 2] = 3
                    board[y-1][x - 1] = 3
                    board[y][x] = 3
                    board[y+1][x + 1] = 3
                    board[y+2][x + 2] = 3
                if board[y-2][x + 2] == board[y-1][x + 1] == board[y][x] and  board[y+2][x - 2] == board[y+1][x - 1] == board[y][x]:
                    board[y-2][x + 2] = 3
                    board[y-1][x + 1] = 3
                    board[y][x] = 3
                    board[y+1][x - 1] = 3
                    board[y+2][x - 2] = 3
                    
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
            cursor_x = m_x*42+35-27
            cursor_y = m_y*42+97-27
        if event.type == pygame.MOUSEBUTTONDOWN and board[m_y][m_x] == 0:
            if event.button == 1 :
                if stone == 1 :
                    board[m_y][m_x] = 1
                    stone = 2
                elif stone == 2 :
                    board[m_y][m_x] = 2
                    stone = 1
    print("hello world")
    background.blit(image_bg, (0,0))
    background.blit(image_omok[8], (cursor_x, cursor_y))
    draw_stone()
    check()
    pygame.display.update()

pygame.quit()
