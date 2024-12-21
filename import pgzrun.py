import pgzrun
from random import randint

WIDTH = 500
HEIGHT = 500
TITLE = "Shoot the Alien"

message = ""
alien = Actor('alien')
alien.pos = 50,50
def draw():
    screen.clear()
    screen.fill(color="Blue")
    alien.draw()
    screen.draw.text(message,center=(400,10),fontsize=30)

def move_alien():
    alien.x = randint(50,WIDTH-50)
    alien.y = randint(50,HEIGHT-50)


def on_mouse_down(pos):
    global message
    if alien.collidepoint(pos):
       message = "Good shot!"
       move_alien()
    else:
        message = "You missed!"      

pgzrun.go() 