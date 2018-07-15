# Counter with buttons

###################################################
# Student should add code where relevant to the following.

import simplegui 

color = "Red"

# Timer handler
def tick():
    global color
    if color == "Red":
        color = "Blue"
    else:
        color = "Red"
    change(color)
        
def change(canvas):
    frame.set_canvas_background(color)
        
        
# Create frame and timer
frame = simplegui.create_frame("Counter with buttons", 200, 200)
frame.set_draw_handler(change)
timer = simplegui.create_timer(3000, tick)

# Start timer
frame.start()
timer.start()

