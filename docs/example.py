# --------------------------------------------
# Ejemplo simple de Gradient Descent en Python
# --------------------------------------------

# 1) Datos de ejemplo: solo dos puntos (x_i, y_i)
#    x = kilometraje (en miles), y = precio (en miles de €)
data = [
    (10,  2),   #  10 miles ->  2 (2 000 €)
    (20,  3)    #  20 miles ->  3 (3 000 €)
]
m = len(data)

# 2) Hipótesis inicial: theta0 = 0, theta1 = 0
theta0 = 0.0
theta1 = 0.0

# 3) Hiperparámetros
learning_rate = 0.01
iterations    = 20

# 4) Función para calcular el coste (MSE), solo para imprimir
def compute_cost(theta0, theta1):
    total_error = 0.0
    for x, y in data:
        y_pred = theta0 + theta1 * x
        total_error += (y_pred - y) ** 2
    return total_error / m

# 5) Bucle de entrenamiento: n iteraciones de Gradient Descent
print("Iter |   θ₀    |   θ₁    |   Coste (MSE)")
print("---------------------------------------")
for it in range(1, iterations + 1):
    # 5.1) Calculamos gradientes (derivadas parciales) de la función de coste
    grad0 = 0.0
    grad1 = 0.0
    for x, y in data:
        y_pred = theta0 + theta1 * x
        error  = y_pred - y
        grad0 += error          # derivada parcial w.r.t θ₀: ∑(y_pred - y)
        grad1 += error * x      # derivada parcial w.r.t θ₁: ∑( (y_pred - y) * x )
    grad0 /= m                 # promedio
    grad1 /= m                 # promedio

    # 5.2) Actualizamos los parámetros θ₀ y θ₁
    theta0 = theta0 - learning_rate * grad0
    theta1 = theta1 - learning_rate * grad1

    # 5.3) Imprimimos el estado actual cada iteración
    cost = compute_cost(theta0, theta1)
    print(f"{it:4d} | {theta0:7.4f} | {theta1:7.4f} | {cost:12.6f}")

# 6) Al final, mostramos la recta entrenada
print("\nModelo final:")
print(f"  Precio ≈ {theta0:.4f} + {theta1:.4f} * km")
print("  (Aquí 'km' está en decenas de miles, y el precio está en miles de €)")

