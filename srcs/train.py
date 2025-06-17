"""

"""
import os
import utils
import matplotlib.pyplot as plt
   
def get_path(file):
    print("Found!")
    return os.path.join(os.path.dirname(__file__), file)

def read_data(source="./data.csv"):
    data = {}
    f = open(source)
    fl = False
    for line in f:
        if fl is False:
            fl = True
            continue
        line = line.strip()
        split = line.split(',')
        try:
            miles = (int(split[0]))
            price = (int(split[1]))
            data[miles] = price
        except ValueError as e:
            print(f"ValueError parsing line: {line} => {e}")
    f.close()
    return data


def get_data(data):
    prices = []
    miles = []
    for mile, price in data.items():
        prices.append(price)
        miles.append(mile)
    return miles, prices

# This is called "Min-Max" normalization
# source https://www.codecademy.com/article/normalization
def normalize_data(miles, prices):
    s_prices = []
    min_price = min(prices)
    max_price = max(prices)

    s_miles = []
    min_mile = min(miles)
    max_mile = max(miles)

    for price in prices:
        s_prices.append((price - min_price) / (max_price - min_price))
    for mile in miles:
        s_miles.append((mile - min_mile) / (max_mile - min_mile))

    return (s_miles, s_prices)

def loss_function(t0 :float, t1 :float, miles, prices):
    total_error = 0.0
    for mile, price in zip(miles, prices):
        y_pred = t0 + mile * t1
        total_error += (y_pred - price) ** 2
    return total_error / len(miles)

def gradient_descend(miles :list, prices :list, learning :float, iterations):
    print("Starting gradient descend\n")
    loss_historic = []
    t1_historic = []
    t0_historic = []
    m = len(miles)
    t0 = 0.0
    t1 = 0.0

    for iteration in range(iterations + 1):
        dt0 = 0
        dt1 = 0
        for x, y in zip(miles, prices):
            y_pred = t0 + t1 * x
            error = y_pred - y
            dt0 += error
            dt1 += error * x
        dt0 /= m
        dt1 /= m
        t0 = t0 - learning * dt0
        t1 = t1 - learning * dt1
        cost = loss_function(t0, t1, miles, prices)
        if iteration % 10 == 0:
            print(f"iteration: {iteration} \t | cost: {cost} \t | t0: {t0} \t | t1: {t1}")
        loss_historic.append(cost)
        t0_historic.append(t0)
        t1_historic.append(t1)
    return t0, t1, t0_historic, t1_historic, loss_historic

def main():
    learning_rate = 0.3
    epochs = 500
    data = read_data(get_path('data.csv'))
    miles, prices = get_data(data)
    if (utils.check_data(miles, prices)): return

    s_miles, s_prices = normalize_data(miles, prices)
    print(s_miles)
    print(s_prices)

    t0, t1, t0_hist, t1_hist, loss_hist = gradient_descend(s_miles, s_prices, learning_rate, epochs)
    ######################################
    min_mile = min(miles)
    max_mile = max(miles)
    min_price = min(prices)
    max_price = max(prices)

    x_plot = []
    y_plot = []
    for mile in range(int(min_mile), int(max_mile), 1000):
        norm_mile = (mile - min_mile) / (max_mile - min_mile)
        norm_price = t0 + t1 * norm_mile
        actual_price = utils.denormalize_element(prices, norm_price)
        x_plot.append(mile)
        y_plot.append(actual_price)

    # Plot original data
    plt.scatter(miles, prices, color='blue', label='Original data')

    # Plot regression line
    plt.plot(x_plot, y_plot, color='red', label='Linear regression')

    plt.title("Car Price vs Mileage")
    plt.xlabel("Mileage (in miles)")
    plt.ylabel("Price (in currency units)")
    plt.legend()
    plt.grid(True)
    plt.show()
    #################################################
    # print_data(data)
    return

main()
