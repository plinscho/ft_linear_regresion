
def print_data(data):
    for miles, price in data.items():
        print(f"miles: {miles} \t| price: {price}")

def	normalize_element(list, elem):
	return ((elem - min(list)) / (max(list) - min(list)))

# real_value = scaled_value ⋅ (max − min) + min
def	denormalize_element(list, elem):
	return ((elem * (max(list) - min(list))) + min(list))

def check_data(miles, prices):
    if len(miles) != len(prices):
        print("Error.\nLists are not same size!")
        return True
    return False
