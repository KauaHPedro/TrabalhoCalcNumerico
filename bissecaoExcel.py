import numpy as np
import pandas as pd

def calcularRaiz(f, a, b, erro): 
    iteracoes = []  
    
    if np.sign(f(a)) == np.sign(f(b)):
        raise Exception("Intervalo inválido!")
        
    while True:
        m = (a + b) / 2
        iteracoes.append({"a": round(a, 6), "b": round(b, 6), "Xk": round(m, 6), "f(a)": round(f(a), 6), "f(Xk)": round(f(m), 6)})
        
        if np.abs(f(m)) < erro:
            break
        
        if np.sign(f(a)) == np.sign(f(m)):
            a = m
        else:
            b = m
            
    return m, iteracoes

def f1(x):
    return round(np.sqrt(5 - x) - 2 ** (x - 1), 6)

def f2(x):
    return round(np.log(3 * x - 1) + 2 * x, 6)

def f3(x):
    return round(x + 5 * np.log(x) - 2, 6)


raizEx1, iteracoesEx1 = calcularRaiz(f1, 1, 2, 0.01)
raizEx2, iteracoesEx2 = calcularRaiz(f2, 0.34, 0.5, 0.01)
raizEx3, iteracoesEx3 = calcularRaiz(f3, 1, 5, 0.01)


df = pd.DataFrame(iteracoesEx1)
df.to_excel("Exercicio1.xlsx", index=False)

df = pd.DataFrame(iteracoesEx2)
df.to_excel("Exercicio2.xlsx", index=False)

df = pd.DataFrame(iteracoesEx3)
df.to_excel("Exercicio3.xlsx", index=False)

print(round(raizEx1, 6))
print(round(raizEx2, 6))
print(round(raizEx3, 6))