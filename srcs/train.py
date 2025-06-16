"""

"""

from utils import print_data

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
            miles = int(split[0])
            price = int(split[1])
            data[miles] = price
        except:
            print(f"Error in line: {line}")
    f.close()
    return data


def main():
    data = read_data()
    print_data(data)
    return

main()