# Move a ball

###################################################
# Student should add code where relevant to the following.


import simplegui 

# Define globals - Constants are capitalized in Python
HEIGHT = 400
WIDTH = 400
RADIUS_INCREMENT = 5
ball_radius = 20

# Draw handler
def draw(canvas):
    canvas.draw_circle([HEIGHT / 2, WIDTH / 2], ball_radius, 3, "Green")
    
# Error Message
def error(canvas):
    canvas.draw_text("Es el limite", [HEIGHT / 2, WIDTH / 2], 24, "Green")

    # Event handlers for buttons
def increase_radius():
    global ball_radius
    if ball_radius <= RADIUS_INCREMENT: 
       frame.set_draw_handler(error)
    else:
        ball_radius = ball_radius - RADIUS_INCREMENT
        frame.set_draw_handler(draw)

    
def decrease_radius():
    global ball_radius, canvas
    if ball_radius >= (WIDTH / 2):
       frame.set_draw_handler(error)
    else:
        ball_radius = ball_radius + RADIUS_INCREMENT
        frame.set_draw_handler(draw)

# Create frame and assign callbacks to event handlers
frame = simplegui.create_frame("Ball control", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.add_button("Increase radius", increase_radius)
frame.add_button("Decrease radius", decrease_radius)


# Start the frame animation
frame.start()