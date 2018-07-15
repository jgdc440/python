"""
Solution - Write a function make_dict_lists(length) that returns a dictionary whose keys are in range(length) and whose
corresponding values are lists of zeros with length matching the key
"""


# Add code here
def make_dict_lists(length):
    respuesta = {}
    
    for x in range(length):
        respuesta[x] = [0] * x
        
    return respuesta

# Tests
print(make_dict_lists(0))
print(make_dict_lists(1))
print(make_dict_lists(4))


# Output
#{}
#{0: []}
#{3: [0, 0, 0], 0: [], 4: [0, 0, 0, 0], 1: [0], 2: [0, 0]}

