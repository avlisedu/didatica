import numpy as np
import matplotlib.pyplot as plt

# Dados fictícios de exemplo
X = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 6, 8, 180])  # Relação linear perfeita só pra ilustrar

# Parâmetros iniciais
m = 0.0  # Inclinação (slope)
b = 0.0  # Intercepto (intercept)
learning_rate = 0.01
epochs = 1000  # Número de iterações

n = len(X)

for epoch in range(epochs):
    # Predição do modelo
    y_pred = m * X + b

    # Cálculo do erro
    error = y_pred - y

    # Cálculo dos gradientes (derivadas parciais)
    m_grad = (2/n) * np.dot(error, X)
    b_grad = (2/n) * np.sum(error)

    # Atualização dos parâmetros
    m -= learning_rate * m_grad
    b -= learning_rate * b_grad

    # Exibição de progresso a cada 200 iterações
    if epoch % 200 == 0:
        mse = np.mean(error ** 2)
        print(f"Iteração {epoch}: MSE={mse:.4f} | m={m:.4f} | b={b:.4f}")

print(f"\nResultado final: y = {m:.2f}x + {b:.2f}")

# Visualização do ajuste
plt.scatter(X, y, color='blue', label='Dados')
plt.plot(X, m * X + b, color='red', label='Reta ajustada')
plt.legend()
plt.title("Gradiente Descendente - Regressão Linear")
plt.xlabel("X")
plt.ylabel("y")
plt.show()
