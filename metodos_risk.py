lst = ["R1", "R3", "R5", "R10", "R17", "R21"]
print lst[2]

print lst[-1]
print 82 in lst
print 4 in lst
print lst.index("R5")
lst.append("R8")
print lst
lst.pop(-1)
print lst

risk = ("R21")

lst.pop(lst.index(risk))

print lst