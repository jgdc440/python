# "Guess the number" mini-project JGDC
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
import math

# function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global attempts, num_for_guess, high
    num_for_guess = random.randrange(0, high)
    attempts = math.trunc(math.ceil(math.log(high,2),))
    print "New game. Range is from 0 to " + str(high)
    print "Number to remaining guesses is " + str(attempts)
      
# event handlers for control panel
def range100(): 
    # button that changes the range to [0,1000) and starts a new game
    global high
    high = 100
    print ""
    new_game()
  
def range1000():
    # button that changes the range to [0,1000) and starts a new game
    global high
    high = 1000
    print ""
    new_game()
         
def input_guess(guess):
    # main game logic goes here	
    global attempts
    p_guess = int(guess)
    print ""
    print "Guess was " + guess
    attempts = attempts - 1
    print "Number to remaining guesses is " + str(attempts)
    if attempts == 0 and p_guess != num_for_guess:
        print "You run out of guesses. The number was " + str(num_for_guess)
        print ""
        new_game()
    elif p_guess == num_for_guess: 
        print "Correct!"
        print ""
        new_game()
    elif p_guess < num_for_guess:
        print "Higher!"
    else:
        print "Lower!"
        
#frame 
frame = simplegui.create_frame("Guess the Numner", 200, 200)

# register event handlers for control elements and start frame
frame.add_button("Range is [0, 100)", range100, 200)
frame.add_button("Range is [0, 1000)", range1000, 200)
frame.add_input("Enter a Guess", input_guess, 200)
frame.start()

# Set initial extreme in the variable high
high = 100
# call new_game
new_game()

# always remember to check your completed program against the grading rubric

