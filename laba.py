x = int(input('Введите число:'))
A = []
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
