# implementation of card game - Memory

import simplegui
import random

CARD_SIZE = [50, 100]
CARD_CENTER = [CARD_SIZE[0] / 2, CARD_SIZE[1] / 2]

# load images
front_image = simplegui.load_image("https://dl.dropboxusercontent.com/u/21123500/Coursera/card_front.jpg")
back_image = simplegui.load_image("https://dl.dropboxusercontent.com/u/21123500/Coursera/card_back.jpg")

# helper function to initialize globals
def new_game():
    global cards, exposed, state, flipped, turns, game_over
    
    # set cards numbers and shuffle them
    cards = range(8) + range(8)
    random.shuffle(cards)
    
    # initialize / reset variables for a new game
    exposed = [False] * 16
    state = 0
    flipped = []
    turns = 0
    label.set_text("Turns = " + str(turns))
    game_over = False
    
def check_game_over():
    """ If all cards are exposed then Game is Over """
    global game_over
    
    # return and leave game_over as False if there is a card not exposed
    for i in exposed:
        if not i:
            return
        
    # game is over    
    game_over = True
    print "***************     GAME OVER     ***************"
    print "Congratulations you finished the game in %s turns!" % (turns)
    print ""
    print "Click the 'Reset' button for a new game."
     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global state, flipped, turns
    
    # what card was clicked by its x position
    card_clicked = pos[0] // CARD_SIZE[0]
    
    # validate click only if clicked on a card not exposed
    if not exposed[card_clicked]:
        #set state
        if state == 0:
            state = 1
        elif state == 1:
            # second click
            state = 2
            
            # add turn and change label
            turns += 1
            label.set_text("Turns = " + str(turns))
        else:
            # first click
            state = 1
            
            # check if match and flip if needed
            if cards[flipped[0]] != cards[flipped[1]]:
                exposed[flipped[0]] = exposed[flipped[1]] = False
                
            # clean flipped cards
            flipped = []

        # expose it
        exposed[card_clicked] = True
        
        #Get the card exposed
        flipped.append(card_clicked)
        
        #check if game is over
        check_game_over()
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    #Check if images are loaded
    if front_image.get_width() == 0 or back_image.get_height() == 0:
        canvas.draw_text("Loading...", [300, 65], 50, "White", "sans-serif")
        return
    
    # draw Cards
    for i in range(len(cards)):
        # set different colour for the ones just flipped
        colour = "#e76468"
        if len(flipped) > 0 and not game_over:
            if i == flipped[0] or i == flipped[-1]:
                colour = "#065f72"
        
        # card position
        card_pos = CARD_SIZE[0] * i
        
        # draw card image and text on top
        canvas.draw_image(front_image, CARD_CENTER, CARD_SIZE, [card_pos + CARD_CENTER[0], CARD_CENTER[1]], CARD_SIZE)
        canvas.draw_text(str(cards[i]), [card_pos + 7, 75], 68, colour, "sans-serif")
        
        # draw back of card
        if not exposed[i]:
            canvas.draw_image(back_image, CARD_CENTER, CARD_SIZE, [card_pos + CARD_CENTER[0], CARD_CENTER[1]], CARD_SIZE)
        
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric