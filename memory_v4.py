# implementation of card game - Memory

import simplegui
import random

state = 0
first = 0
second = 0
tries = 0

number_list = range(8)*2

# helper function to initialize globals
def init():
    global tries, exposed, state
    
    tries = 0
    state = 0
    label.set_text('Moves = ' + str(tries))
    exposed = [False]*16
    random.shuffle(number_list)

# define event handlers
def mouseclick(pos):
    # add game state logic here
    chosen_card = pos[0]
    chosen_card = chosen_card // 50
    
    global state, first, second, tries
    
    if state == 0:
        state = 1
        first = chosen_card
        exposed[chosen_card] = True
    elif state == 1:
        if not exposed[chosen_card]:
            state = 2
            second = chosen_card
            exposed[chosen_card] = True
            tries += 1
            label.set_text("Moves = " + str(tries))
    else:
        if not exposed[chosen_card]:
            state = 1
            if number_list[first] != number_list[second]:
                exposed[first] = False
                exposed[second] = False
            
            first = chosen_card
            exposed[chosen_card] = True


# cards are logically 50x100 pixels in size    
def draw(canvas):
    offset = 0
    for number in number_list:
        if exposed[offset]:
            canvas.draw_text(str(number),
                             (50*offset + 13, 60),
                             50,
                             'White')
        else:  # green rectangle
            canvas.draw_polygon(
                [(offset * 50, 0),
                 (offset * 50 + 50, 0),
                 (offset * 50 + 50, 100),
                 (offset * 50, 100)],
                5, "White", "Green")
        
        offset += 1
                         
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Restart", init)
label = frame.add_label("Moves = 0")

# initialize global variables
init()

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
frame.start()