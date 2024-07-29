import pgzrun
from random import randint
WIDTH=500
HEIGHT=500
TITLE="LOVE"
def draw():
    r=255
    g=0
    b=randint(120,255)
    for i in range(20):
        abby=Rect((0,0),(100,100))
        abby.center=250,250
        screen.draw.rect(abby,(r,g,b))
pgzrun.go()