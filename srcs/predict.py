import os
from utils import read_data

"""
Theory: y = m*x + b (This is actually the price equation)
        y = Theta0 * X + Theta1
where: 
        x = Input from the user (km)
        Theta0 = Controlls the slope of the linear function
        Theta1 = Controlls the intersept of the line

We need to mesure HOW BAD our model behaves with the gradient, 
and we use SSE (Sum Squared Errors) to get that information


"""


dict_km_price = {}

class PredictPrice():
    def __init__(self, data="./data.csv"):
        # Init parameters
        self.learning_rate = 0.01
        self.t0 = 0
        self.t1 = 0

        # Init data (its divided by 1000, carefull)
        self.data_raw = read_data(data)
        self.km_raw = [row[0] for row in self.data_raw]
        self.price_raw = [row[1] for row in self.data_raw]
        
def read_data(path):
    first_line = True;
    global dict_km_price
    raw_km_price = {}

    with open(path, 'r') as file:
        for line in file:
            line = line.strip() # Remove white spaces and newlines

            if first_line:
                first_line = False
                continue

            data = line.split(',')
            if len(data) != 2:
                print(f"Skipping invalid line: {line}")
                continue
            try:
                km = int(data[0] / 1000) # we need to reduce values
                price = int(data[1] / 1000) # to have smaller errors
                raw_km_price[km] = price
            except:
                print(f"Error in line: {line}")

    dict_km_price = dict(sorted(raw_km_price.items()))
    print("Data loaded succesfully!")

def print_data():
    print(f"KM --> Price:")
    for km, price in dict_km_price.items():
        print(f"{km}\tkm ---> {price}€")


def get_km_user():
    ok = False;
    while (ok == False):
        try:
            miles_str = input("Write a mileage to get a price: ")
            miles = int(miles_str)
            if miles < 0:
                print("Enter a positive value...")
            else:
                ok = True
                return miles
        except:
            print("Error.\nIntroduce a valid positive int")

def predict_price(km):
   print(km) 


def main():
    #print_data()
    km = get_km_user()
    print_data()
    predict_price(km)

if __name__ == "__main__":
    main()

