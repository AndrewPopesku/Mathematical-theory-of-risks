import numpy as np

# Задані дані
data = {
    "m_n": [50, 40, 50, 50, 40, 30, 40, 30, 50, 30],
    "sigma_n": [20, 15, 20, 20, 15, 12, 15, 14, 20, 13],
    "m_q": 10,
    "x_n": [80, 60, 120, 75, 70, 110, 90, 70, 85, 55],
    "sigma_p_n": [15, 11, 15, 12, 10, 5, 12, 8, 10, 11]
}

def calculate_portfolio_metrics(m_n, sigma_n, m_q, x_n):
    # Обчислення сподіваної норми прибутку портфеля
    m_p = x_n * m_n + (1 - x_n) * m_q
    
    # Обчислення оцінки ризику портфеля
    sigma_q = 0  # оцінка ризику державних облігацій
    rho = 0  # коефіцієнт кореляції між двома активами (тут вказано як 0)
    sigma_p = np.sqrt(x_n**2 * sigma_n**2 + (1 - x_n)**2 * sigma_q**2 + 2 * x_n * (1 - x_n) * rho * sigma_n * sigma_q)
    
    return m_p, sigma_p

def find_portfolio_structure(sigma_p_n, sigma_n, m_q):
    # Пошук структури портфеля, оцінка ризику якого = sigma_p_n
    x_n = np.sqrt((sigma_p_n**2 - (1 - sigma_p_n**2) * sigma_q**2) / (sigma_n**2 - sigma_q**2))
    
    return x_n

# Обчислення метрик для кожного рядка у вхідних даних
for i in range(len(data["m_n"])):
    m_n = data["m_n"][i]
    sigma_n = data["sigma_n"][i]
    m_q = data["m_q"]
    x_n = data["x_n"][i]
    sigma_p_n = data["sigma_p_n"][i]

    m_p, sigma_p = calculate_portfolio_metrics(m_n, sigma_n, m_q, x_n)
    print(f"Для рядка {i + 1}:")
    print(f"Сподівана норма прибутку портфеля: {m_p:.2f}%")
    print(f"Оцінка ризику портфеля: {sigma_p:.2f}%\n")

# Знаходження структури портфеля, оцінка ризику якого = sigma_p_n
for i in range(len(data["sigma_p_n"])):
    sigma_p_n = data["sigma_p_n"][i]
    sigma_n = data["sigma_n"][i]
    x_n = find_portfolio_structure(sigma_p_n, sigma_n, data["m_q"])
    print(f"Для оцінки ризику {sigma_p_n}% структура портфеля повинна бути: {x_n * 100:.2f}% в ринковому портфелі та {(1 - x_n) * 100:.2f}% в державних облігаціях\n")
