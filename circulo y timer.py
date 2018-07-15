import simplegui 

WIDTH = 200
HEIGHT = 200
radius = 1
interval = 1000

# Timer handler
def tick():
    global radius
    radius +=1
    
# Draw handler
def circulo(canvas):
    canvas.draw_circle((WIDTH, HEIGHT), radius, 10, 'Green')
    
# Create frame and timer
frame = simplegui.create_frame("El Circulo", 400, 400)
frame.set_draw_handler(circulo)
timer = simplegui.create_timer(interval, tick) 

# Start program & timer 
frame.start()
timer.start()