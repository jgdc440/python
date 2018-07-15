# Image positioning _ Revisar con Detalle

###################################################
# Student should enter code below

import simplegui

# global constants
WIDTH = 400
HEIGHT = 300
img_pos = [WIDTH / 2, HEIGHT / 2]
test_img_size = [95, 93]
test_img_center = [test_img_size[0] / 2, test_img_size[1] / 2]

# load test image
img = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/asteroid.png")

# mouseclick handler
def click(pos):
    global img_pos
    img_pos = pos
        
# draw handler
def draw(canvas):
    canvas.draw_image(img, test_img_center, test_img_size, 
                      img_pos, test_img_size)
    
# create frame and register draw handler    
frame = simplegui.create_frame("Test image", WIDTH, HEIGHT)
frame.set_canvas_background("Gray")
frame.set_draw_handler(draw)
frame.set_mouseclick_handler(click)

# start frame
frame.start()     
                                       