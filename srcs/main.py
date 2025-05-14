import os

dict_km_price = {}

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
                km = int(data[0])
                price = int(data[1])
                raw_km_price[km] = price
            except:
                print(f"Error in line: {line}")

    dict_km_price = dict(sorted(raw_km_price.items()))
    print("Data loaded succesfully!")

def print_data():
    print(f"KM --> Price:")
    for km, price in dict_km_price.items():
        print(f"{km}\tkm ---> {price}€")

def get_input_data():
    path = input("data file path: ")
    if not os.path.exists(path):
        print("Error: path does not exist.")
        exit()
    read_data(path)
    print_data()

get_input_data()
