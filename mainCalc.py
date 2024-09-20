import math
from xml.etree.ElementTree import tostring


def calcularRaiz(funcao, a, b, erro):
    if funcao(a) * funcao(b) >= 0:
        print('intervalo inválido')

    while (math.fabs(b -a)) / 2 > erro:
        c = round((a + b) / 2, 6)
        if round(funcao(c), 6) == 0 or round((b - a) / 2, 6) < erro:
            return c
        
        if round(funcao(a), 6) * round(funcao(c), 6) < 0:
            b = c
        else:
            a = c
    
    return c

def f1(x):
    return round(math.sqrt(5 - x) - 2 ** (x - 1), 6)

def f2(x):
    return round(math.log(3 * x - 1) + 2 * x, 6)

print(calcularRaiz(f1, 1, 2, 0.01))
print(calcularRaiz(f2, 0.34, 0.5, 0.01))