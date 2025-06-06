import numpy as np
import matplotlib as mp
from utils import read_data, print_data

"""
    repeat until convergence
{
    w = w - (learning_rate * (dJ/dw))
    b = b - (learning_rate * (dJ/db))
}

    where w = 
    where b = 

"""

class Train:
    def  __init__(self):
        self.raw_data = read_data('srcs/data.csv')
        self.km = [km for km, prices in self.raw_data.items()]
        self.prices = [price for km, price in self.raw_data.items()]
        self.t0 = 0                 # theta1
        self.t1 = 0                 # theta0
        self.learn_rate = 0.001     # Weight of each iteration
        self.epochs = 100           # Number of iterations

def mean_squared_error(data :Train):
    y = data.prices

def calc_theta(data :Train):
    return ""
    
def calc_mse(data :Train):
    return ""


def main():
    train = Train()
    print(train.raw_data)
    print(len(train.km))
    print(train.prices)
    print(len(train.prices))

main()
