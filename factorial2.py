def factorial(n):

    fat = 1
    x = 1
    while x <= n:
        fat *= x
        x += 1
    return fat

y = int(raw_input("Introduzca el valor a factorizar: "))

print factorial(y)