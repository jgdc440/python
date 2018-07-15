# Mi propia bola
import simplegui
import math

## Variables
WIDTH = 300
HEIGHT = 300
RADIO = 18
ball_pos = (WIDTH / 3, HEIGHT / 2)
color_ball = "Red"

# Event handler
def distancia(p, q):
    return math.sqrt( (p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2 )
    
def click(pos):
    global ball_pos, color_ball
    if distancia(ball_pos, pos) < RADIO:
        color_ball = "Green"
    else:
        color_ball = "Red"
        ball_pos = list(pos)
    
# Dibujar bola
def draw(canvas):
    canvas.draw_circle(ball_pos, RADIO, 1, "Black", color_ball)
    
# El lienzo de trabajo
frame = simplegui.create_frame("Mis Bolas", WIDTH, HEIGHT)
frame.set_canvas_background("White")

# Activacion de los handlers
frame.set_draw_handler(draw)
frame.set_mouseclick_handler(click)

frame.start()