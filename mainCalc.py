import numpy as np

def calcularRaiz(f, a, b, erro): 
    
    if np.sign(f(a)) == np.sign(f(b)):
        raise Exception(
         "Intervalo inválido!")
        
    m = (a + b)/2
    
    if np.abs(f(m)) < erro:
        # Para a condição, retorna M como a raíz da função
        return m
    
    elif np.sign(f(a)) == np.sign(f(m)):
        return calcularRaiz(f, m, b, erro)
    
    elif np.sign(f(b)) == np.sign(f(m)):
        return calcularRaiz(f, a, m, erro)

def f1(x):
    return round(np.sqrt(5 - x) - 2 ** (x - 1), 6)

def f2(x):
    return round(np.log(3 * x - 1) + 2 * x, 6)

def f3(x):
    return round(x + 5 * np.log(x) - 2)

print(round(calcularRaiz(f1, 1, 2, 0.01), 6))
print(round(calcularRaiz(f2, 0.34, 0.5, 0.01), 6))
print(round(calcularRaiz(f3, 1, 2, 0.01), 6))