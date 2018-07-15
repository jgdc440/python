# Define a function that returns formatted minutes and seconds

###################################################
# Time formatting function
# Student should enter function on the next lines.

def format_time(seconds):
    global f_minutes, f_seconds, a
    f_minutes = seconds // 60
    f_seconds = seconds % 60
    a = "Son: " + str(f_minutes) + " minutos, con "+str(f_seconds)
    return a

###################################################
# Tests

print format_time(23)
print format_time(1237)
print format_time(0)
print format_time(1860)

###################################################
# Output to console
#0 minutes and 23 seconds
#20 minutes and 37 seconds
#0 minutes and 0 seconds
#31 minutes and 0 seconds