###################################
# Interaction with globals


a = [4, 5, 6]

def mutate_part(x):
    a[1] = x

def assign_whole(x):
    a = x

def assign_whole_global(x):
    global a
    a = x

mutate_part(100)
print a

assign_whole(200)
print a

assign_whole_global(300)
print a