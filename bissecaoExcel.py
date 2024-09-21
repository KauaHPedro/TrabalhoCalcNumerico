import numpy as np
import pandas as pd

def calcularRaiz(f, a, b, erro): 
    iteracoes = []  # Lista para armazenar as iterações
    
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
            
    return m, iteracoes  # Retorna a raiz e as iterações

def f1(x):
    return round(np.sqrt(5 - x) - 2 ** (x - 1), 6)

def f2(x):
    return round(np.log(3 * x - 1) + 2 * x, 6)

# Exemplo de uso
raizEx1, iteracoesEx1 = calcularRaiz(f1, 1, 2, 0.01)
raizEx2, iteracoesEx2 = calcularRaiz(f2, 0.34, 0.5, 0.01)

# Criar DataFrame e salvar em Excel
df = pd.DataFrame(iteracoesEx1)
df.to_excel("Exercicio1.xlsx", index=False)

df = pd.DataFrame(iteracoesEx2)
df.to_excel("Exercicio2.xlsx", index=False)

print(round(raizEx1, 6))
print(round(raizEx2, 6))