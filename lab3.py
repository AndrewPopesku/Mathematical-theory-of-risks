from scipy.integrate import quad
import numpy as np

# Параметри задачі
a = 35
c = 0.2
x1 = 0
x2 = 10

# Функція щільності розподілу f(x)
def f(x):
    return 1 / (x2 - x1) if (x1 < x and x <= x2) else 0

# Функція корисності U(x)
def U(x):
    return a * x**c

# Сподіваний виграш (Expected Value)
def expected_value():
    result, _ = quad(lambda x: x * f(x), x1, x2)
    return result

# Детермінований еквівалент (Certain Equivalent)
def certain_equivalent():
    return U(expected_value())

# Премія за ризик (Risk Premium)
def risk_premium():
    return expected_value() - certain_equivalent()

# Ставлення до ризику (Risk Aversion)
def risk_aversion():
    expected_value_result = expected_value()
    derivative_1 = a * c * expected_value_result**(c-1)
    derivative_2 = a * c * (c-1) * expected_value_result**(c-2)
    return -derivative_2 / derivative_1

# Виведення результатів
print(f"Сподіваний виграш: {expected_value()}")
print(f"Детермінований еквівалент: {certain_equivalent()}")
print(f"Премія за ризик: {risk_premium()}")
print(f"Ставлення до ризику: {risk_aversion()}")

# Економічне тлумачення результатів
if risk_premium() < 0:
    print("Ви готові платити за уникнення ризику.")
else:
    print("Вам вигідніше взяти участь у лотереї.")

if risk_aversion() > 0.1:
    print("Ви виявляєте велику обережність та уникнення ризиків.")
else:
    print("Ви готові приймати певний ризик для отримання вигоди.")
