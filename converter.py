# Converter Value to Money
# Handle single quantity

import simplegui

# Declare global variables

value = 3.12

def convert_units(val, name):
    result = str(val) + " " + name
    if val > 1:
        result = result + "s"
    return result
        
# convert xx.yy to xx dollars and yy cents
def convert(val):
    # Split into dollars and cents
    dollars = int(val)
    cents = int(round(100 * (val - dollars)))

    # Convert to strings
    dollars_string = convert_units(dollars, "dollar")
    cents_string = convert_units(cents, "cent")

    # return composite string
    if dollars == 0 and cents == 0:
        return "Broke!"
    elif dollars == 0:
        return cents_string
    elif cents == 0:
        return dollars_string
    else:
        return dollars_string + " and " + cents_string
    
# Define function to draw value    
def draw_value(canvas):
    canvas.draw_text(convert(value), (100,100), 24, "White")
    
# Define an input field handler
def input_handler(text):
    global value
    value = float(text)
    

# Create frame
frame = simplegui.create_frame("Converter", 400, 200)

# Draw in Canvas
frame.set_draw_handler(draw_value)
frame.add_input("Enter value", input_handler, 100)
    

# Star Program
frame.start()