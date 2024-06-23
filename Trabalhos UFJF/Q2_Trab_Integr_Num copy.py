import numpy as np
import pandas as pd

# Função a ser integrada
def f(x):
    if x == 0 or x == np.pi:
        return 0  # Evita divisão por zero
    return np.cos(x)**2 * np.sin(x)**2 * (8 / (25 * x))

# Método dos retângulos de Riemann
def riemann_integral(f, a, b, n):
    dx = (b - a) / n
    integral_sum = 0
    for i in range(n):
        x = a + i * dx
        integral_sum += f(x) * dx
    return integral_sum

# Método dos trapézios
def trapezoidal_integral(f, a, b, n):
    dx = (b - a) / n
    integral_sum = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        x = a + i * dx
        integral_sum += f(x)
    return integral_sum * dx

# Intervalo de integração
a = -0.002457
b = 0.014554789

# Número de subintervalos para os métodos de Riemann e trapézios
n = 1000

# Cálculo das integrais aproximadas
riemann_result = riemann_integral(f, a, b, n)
trapezoidal_result = trapezoidal_integral(f, a, b, n)

# Cálculo da solução analítica numericamente
analytical_result = riemann_integral(f, a, b, 10000)  # Usando uma resolução mais alta para maior precisão

# Criar um DataFrame para apresentar os resultados
data = {
    'Método': ['Riemann', 'Trapézios', 'Solução Analítica'],
    'Resultado da Integral': [riemann_result, trapezoidal_result, analytical_result]
}

df = pd.DataFrame(data)
print(df)
