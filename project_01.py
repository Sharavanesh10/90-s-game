import pygame as py
import sys as s


HEIGHT,WIDTH=700,700
WINDOW=py.display.set_mode((WIDTH,HEIGHT))

py.display.set_caption("90's")

FPS=90

def win_display():
    WINDOW.fill((255,255,255))
def main():
    clock=py.time.Clock()
    run=True
    while run:
        clock.tick(FPS)
        for event in py.event.get():
            if event.type == py.QUIT:
                run=False
        win_display()
        
        py.display.update()
    py.quit()
main()
