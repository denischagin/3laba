x = int(input('Введите число:'))
A = []

def x2(x):
  x /= 2
  return collatz(x)

def x3_1(x):
  x = 3*x+1
  return collatz(x)

def x3_1(x):
   x = x*3 + 1
   return collatz(x)

def collatz(x):
    global A
    if x == 1:
        A.append(int(x))
        return x
    elif x%2 == 0:
        A.append(int(x))
        return x2(x)
    else:
        A.append(int(x))
        return x3_1(x)

collatz(x)
print(A)
