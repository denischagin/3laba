def x2(x):
    x /= 2
    return collatz(x)

def x3_1(x):
    x = 3*x+1
    return collatz(x)
