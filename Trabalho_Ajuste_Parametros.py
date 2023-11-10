import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import differential_evolution

def model_exp(x,c0,c1,c2,c3,c4,c5,c6):
  return c0+c1*np.cos(x)+c2*np.sin(x)+c3*np.cos(2*x)+c4*np.sin(2*x)+c5*np.cos(3*x)+c6*np.sin(3*x)

def model(params):

    sol = model_exp(x,params[0], params[1],params[2],params[3],params[4],params[5],params[6])

    erro = np.linalg.norm(y-sol, np.inf)/np.linalg.norm(y, np.inf)

    return [erro, sol, x]
def model_adj(x):
    result = model(x)
    return result[0]

dados = np.loadtxt('dados.txt')
x = dados[0]
y = dados[1]
bounds = [(-10, 10)]*7
result = differential_evolution(model_adj, bounds, strategy='best1bin', disp=True)
print(result.x)

erro, sol, x = model(result.x)


plt.plot(x, y, 'bo', label='data');
plt.plot(x, sol, label='Model');
plt.legend()
plt.show()