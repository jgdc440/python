# The Collatz conjecture

import simplegui

n = 217
counter = 0

def calcular():
    global counter, n
    if n == 1:
        timer.stop()
        print
        print counter
    else:
        if (n % 2) == 0:
            n = (n / 2)
        else:
            n = (n * 3 + 1)  
        print n
        counter +=1
    
    
# Create frame and timer
frame = simplegui.create_frame("", 200, 200)
timer = simplegui.create_timer(10, calcular)

# Start timer
frame.start()
timer.start()


