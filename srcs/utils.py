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
    return dict_km_price

def print_data(data):
    print(f"KM --> Price:")
    for km, price in data.items():
        print(f"{km}\tkm ---> {price}€")
