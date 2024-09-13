#오목

import tkinter
import random

cursor_x = 0
cursor_y = 0

mouse_x = 0
mouse_y = 0

mouse_c = 0

stone = 0

#
def mouse_move(e):
    global mouse_x, mouse_y
    mouse_x = e.x
    mouse_y = e.y

def mouse_press(e):
    global mouse_c
    mouse_c = 1


neko = [
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

#고양이그리기
def draw_neko():
    for y in range(16):
        for x in range(16):
            if neko[y][x] > 0:
                cvs.create_image(x * 54 + 45, y * 54 + 125, image=img_neko[neko[y][x]], tag="NEKO")
#점수바꾸기
def scorecount():
    global winner
    cvs.create_image(595, 41, image=img_neko[5],tag='score')
    cvs.create_image(725, 41, image=img_neko[5],tag='score')

def yoko_neko():
    for y in range(16):
        for x in range(2, 14):
            if neko[y][x] > 0:
                if neko[y][x - 2 ] == neko[y][x - 1] == neko[y][x] ==  neko[y][x + 2] == neko[y][x + 1] and neko[y][x]!= 7:
                    for a in range (-2,3,1) :
                        neko[y][x+a] = 7
                   
    for y in range(2, 14):
        for x in range(16):
            if neko[y][x] > 0:
                if neko[y - 2][x] == neko[y - 1][x] == neko[y][x] == neko[y + 2][x] == neko[y + 1][x] and neko[y][x]!= 7:
                    for a in range (-2,3,1) :
                        neko[y + a][x] = 7
                   

    for y in range(2,14):
        for x in range(2, 14):
            if neko[y][x] > 0:
                if neko[y-2][x - 2] == neko[y-1][x - 1] == neko[y][x] and  neko[y+2][x + 2] == neko[y+1][x + 1] == neko[y][x]:
                    neko[y-2][x - 2] = 7
                    neko[y-1][x - 1] = 7
                    neko[y][x] = 7
                    neko[y+1][x + 1] = 7
                    neko[y+2][x + 2] = 7
                if neko[y-2][x + 2] == neko[y-1][x + 1] == neko[y][x] and  neko[y+2][x - 2] == neko[y+1][x - 1] == neko[y][x]:
                    neko[y-2][x + 2] = 7
                    neko[y-1][x + 1] = 7
                    neko[y][x] = 7
                    neko[y+1][x - 1] = 7
                    neko[y+2][x - 2] = 7
                    
def game_main():
    global cursor_x, cursor_y, mouse_c, stone
    if 18 <= mouse_x and mouse_x < 18 + 54 * 16 and 98 <= mouse_y and mouse_y < 98 + 54 * 16:
        cursor_x = int((mouse_x - 18) / 54)
        cursor_y = int((mouse_y - 98) / 54)
    if yoko_neko() == True:
        yoko_neko()
        scorecount()
        
    if neko[cursor_y][cursor_x] != 0:
        mouse_c = 0
    if neko[cursor_y][cursor_x] == 0 :
        if mouse_c == 1 and stone != 1 :
            mouse_c = 0
            neko[cursor_y][cursor_x] = 1
            stone = 1

        if mouse_c == 1 and stone == 1 :
            mouse_c = 0
            neko[cursor_y][cursor_x] = 2
            stone = 2
   
    cvs.create_image(605, 47, image=img_neko[5])
    cvs.create_image(705, 47, image=img_neko[5])

    cvs.delete("CURSOR")
    cvs.create_image(cursor_x * 54 + 45, cursor_y * 54 + 125, image=cursor, tag="CURSOR")
    cvs.delete("NEKO")
    draw_neko()
    root.after(100, game_main)

#
root = tkinter.Tk()
root.title("클릭해서 고양이 놓기")
root.resizable(True, True)
root.bind("<Motion>", mouse_move)
root.bind("<ButtonPress>", mouse_press)
cvs = tkinter.Canvas(root, width=900, height=980)
cvs.pack()

#
bg = tkinter.PhotoImage(file="bg2.png")
cursor = tkinter.PhotoImage(file="cursor.png")
img_neko = [
    None,
    tkinter.PhotoImage(file="chu.png"),
    tkinter.PhotoImage(file="mamechi.png"),
    tkinter.PhotoImage(file="score0.png"),
    tkinter.PhotoImage(file="score1.png"),
    tkinter.PhotoImage(file="score2.png"),
    tkinter.PhotoImage(file="score3.png"),
    tkinter.PhotoImage(file="oya.png")
]

cvs.create_image(450, 495, image=bg)
game_main()
root.mainloop()
