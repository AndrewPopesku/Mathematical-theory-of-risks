import itertools
import matplotlib.pyplot as plt

stocks = [
    {"m": 0.10, "sigma": 0.00},
    {"m": 0.30, "sigma": 0.10},
    {"m": 0.45, "sigma": 0.15},
]

correlation_matrix = [
    [1, 0, 0],  # p12, p13, p23
    [0, 1, -0.8],
    [0, 0, 1],
]

def calculate_portfolio_return(weights):
    return sum(w * stock["m"] for w, stock in zip(weights, stocks))

def calculate_portfolio_sigma(weights):
    sigma_squared = sum(
        w1 * w2 * stock1["sigma"] * stock2["sigma"] * corr
        for w1, stock1, corr_row in zip(weights, stocks, correlation_matrix)
        for w2, stock2, corr in zip(weights, stocks, corr_row)
    )
    return sigma_squared ** 0.5

all_weights = itertools.product([i / 10 for i in range(11)], repeat=len(stocks))
efficient_portfolios = []
for weights in all_weights:
    if sum(weights) == 1:
        portfolio_return = calculate_portfolio_return(weights)
        portfolio_sigma = calculate_portfolio_sigma(weights)
        efficient_portfolios.append((weights, portfolio_return, portfolio_sigma))

investor_portfolio_25 = [(0.25, 0.25, 0.5)]
investor_portfolio_25_return, investor_portfolio_25_sigma = efficient_portfolios[
    efficient_portfolios.index(
        min(
            efficient_portfolios,
            key=lambda x: abs(x[1] - investor_portfolio_25[0][0])
        )
    )
][1:]

portfolio_40 = [(0.4, 0.3, 0.3)]
portfolio_40_return, portfolio_40_sigma = efficient_portfolios[
    efficient_portfolios.index(
        min(
            filter(lambda x: x[1] <= 0.4, efficient_portfolios),
            key=lambda x: x[2]
        )
    )
][1:]

print("a) Множина ефективних ПЦП:")
for portfolio in efficient_portfolios:
    print(f"Ваги: {portfolio[0]}, Прибуток: {portfolio[1]*100:.2f}%, Ризик: {portfolio[2]*100:.2f}%")

print("\nb) ПЦП зі сподіваною нормою прибутку 25%:")
print(f"Прибуток: {investor_portfolio_25_return*100:.2f}%, Ризик: {investor_portfolio_25_sigma*100:.2f}%")

print("\nв) ПЦП зі сподіваною нормою прибутку в межах 40%:")
print(f"Прибуток: {portfolio_40_return*100:.2f}%, Ризик: {portfolio_40_sigma*100:.2f}%")

plt.figure(figsize=(10, 6))
for portfolio in efficient_portfolios:
    plt.scatter(portfolio[2] * 100, portfolio[1] * 100, color='blue')
    plt.text(portfolio[2] * 100, portfolio[1] * 100, str(portfolio[0]), fontsize=8)
plt.xlabel('Ризик, %')
plt.ylabel('Прибуток, %')
plt.title('Множина ефективних ПЦП')
plt.grid(True)
plt.show()
