import numpy as np
import pandas as pd

def calcularRaiz(f, a, b, erro): 
    iteracoes = []  # Lista para armazenar as iterações
    
    if np.sign(f(a)) == np.sign(f(b)):
        raise Exception("Intervalo inválido!")
        
    while True:
        m = (a + b) / 2
        iteracoes.append({"a": round(a, 6), "b": round(b, 6), "Xk": round(m, 6), "f(a)": round(f(a), 6), "f(Xk)": round(f(m), 6), "e": round(b-a, 6)})
        
        if np.abs(f(m)) < erro:
            break
        
        if np.sign(f(a)) == np.sign(f(m)):
            a = m
        else:
            b = m
            
    return m, iteracoes  # Retorna a raiz e as iterações

def f1(x):
    return round(np.sqrt(5 - x) - 2 ** (x - 1), 6)

# Exemplo de uso
raiz, iteracoes = calcularRaiz(f1, 1, 2, 0.01)

# Criar DataFrame e salvar em Excel
df = pd.DataFrame(iteracoes)
df.to_excel("iteracoes_bissecao.xlsx", index=False)

print(round(raiz, 6))
