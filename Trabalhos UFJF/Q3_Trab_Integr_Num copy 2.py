import numpy as np
import matplotlib.pyplot as plt
import math
import pandas as pd

# Função a ser integrada
def f(x):
    return np.cos(x)**2 * np.sin(x)**2 * (8 / (25 * x))

# Método dos retângulos de Riemann
def Integral_De_Riemann(f, a, b, n):
    dx = (b - a) / n
    integral_sum = 0
    for i in range(n):
        x = a + i * dx
        integral_sum += f(x) * dx
    return integral_sum

# Método dos trapézios
def Integral_Trapezoidal(f, a, b, n):
    dx = (b - a) / n
    integral_sum = 0
    integral_sum += (f(a) + f(b)) / 2
    for i in range(1, n):
        x = a + i * dx
        integral_sum += f(x)
    return integral_sum * dx

# Intervalo de integração
a = -0.002457
b = 0.014554789
n = 1000

# Cálculo das integrais aproximadas
resultado_riemann = Integral_De_Riemann(f, a, b, n)
resultado_trapezios = Integral_Trapezoidal(f, a, b, n)

print("Resultado do Método de Riemann:", resultado_riemann)
print("Resultado do Método dos Trapézios:", resultado_trapezios)

data = {
    'Método': ['Riemann', 'Trapézio', 'Solução Analítica'],
    'Resultado da Integral': [resultado_riemann, resultado_trapezios, solucao_analitica]
}

df = pd.DataFrame(data)
print(df)

valores_x = np.linspace(0.001, 0.014554789, 1000)

valores_y = f(valores_x)
valores_riemann = [Integral_De_Riemann(f, a, x, 1000) for x in valores_x]
valores_trapezoidal = [Integral_Trapezoidal(f, a, x, 1000) for x in valores_x]

plt.figure(figsize=(10, 6))
plt.plot(valores_x, valores_y, label='Função')
plt.plot(valores_x, valores_riemann, label='Regra Riemann', linestyle='--')
plt.plot(valores_x, valores_trapezoidal, label='Regra Trapézio')
plt.scatter([0, np.pi], [0, 0], color='red', marker='o', label='Singularidade')
plt.title('Método dos Retângulos de Riemann vs. Regra dos Trapézios vs. Solução Analítica')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()