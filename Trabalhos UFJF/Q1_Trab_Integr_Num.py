import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def Funcao_Probabilidade(x):
    return 0.15 * np.exp(-0.15 * (x - 0.5))

def Integral_De_Riemann(f, a, b, n):
    dx = (b - a) / n
    integral_sum = 0
    for i in range(n):
        x = a + i * dx
        integral_sum += f(x) * dx
    return integral_sum

def Integral_Trapezoidal(f, a, b, n):
    dx = (b - a) / n
    integral_sum = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        x = a + i * dx
        integral_sum += f(x)
    return integral_sum * dx

# Intervalo de x para o gráfico
intervalo_x = np.linspace(-4, 20, 1000)

# Probabilidade de até x=15 usando os métodos
prob_15_riemann = Integral_De_Riemann(Funcao_Probabilidade, -4, 15, 100)
prob_15_trapezoidal = Integral_Trapezoidal(Funcao_Probabilidade, -4, 15, 100)

print("Probabilidade de no máximo 15 avanços de sinais de carros (Riemann):", prob_15_riemann)
print("Probabilidade de no máximo 15 avanços de sinais de carros (Trapezoidal):", prob_15_trapezoidal)

# Criar DataFrame
data = {
    'Método': ['Riemann', 'Trapézios'],
    'Probabilidade de até x=15': [prob_15_riemann, prob_15_trapezoidal]
}

df = pd.DataFrame(data)
print(df)

# Gráfico comparativo
plt.figure(figsize=(10, 6))
plt.plot(intervalo_x, [Integral_De_Riemann(Funcao_Probabilidade, -4, x, 100) for x in intervalo_x], label='Riemann Sums', linestyle='--')
plt.plot(intervalo_x, [Integral_Trapezoidal(Funcao_Probabilidade, -4, x, 100) for x in intervalo_x], label='Trapezoidal Rule')
plt.fill_between(intervalo_x, 0, Funcao_Probabilidade(intervalo_x), alpha=0.2)
plt.title('Método dos Retângulos de Riemann vs. Regra dos Trapézios')
plt.xlabel('x')
plt.ylabel('Integral Aproximada')
plt.legend()
plt.show()

# Gráfico da função densidade de probabilidade
plt.figure(figsize=(10, 6))
plt.plot(intervalo_x, Funcao_Probabilidade(intervalo_x), label='Densidade de Probabilidade')
plt.fill_between(intervalo_x, 0, Funcao_Probabilidade(intervalo_x), alpha=0.2)
plt.title('Função Densidade de Probabilidade')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.show()
