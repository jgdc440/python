# Space bar status

import simplegui

message = "Nadie toca la barra espaciadora"

# Handlers for keydown and keyup
def keydown(key):
    global message
    if key == simplegui.KEY_MAP["space"]:
        message = "Alguien toca la barra espaciadora"

def keyup(key):
    global message
    if key == simplegui.KEY_MAP["space"]:
        message = "Nadie toca la barra espaciadora"

# Handler to draw on canvas
def draw(canvas):
    canvas.draw_text(message, [25, 112], 42, "Red")

# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("Home", 700, 200)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.set_draw_handler(draw)

# Start the frame animation
frame.start()