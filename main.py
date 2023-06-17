from pygame import *

display.set_caption("Ping Pong Game")
window = display.set_mode((1000,550))
background = transform.scale(image.load("table.jpg"),(1000,550))

class Player():
    def __init__(self,x,y,color):
        self.x = x
        self.y = y
        self.color = color
        self.rect = Rect(x,y,100,20)
    def display(self):
        

clock = time.Clock()

run = True
while run:
    window.blit(background,(0,0))
    display.update()
    clock.tick(60)