import requests
import pandas as pd
import json



with open('/Users/akacoral/Documents/GitHub/API-test-clima/api test/rh_yearly_data.json', 'r', encoding='utf-8') as file:
    json_data = json.load(file)

y_values = [item['y'] for item in json_data if 'y' in item]
base_values = [item['base'] for item in json_data if 'base' in item]
ave_values = [item['customdata'] for item in json_data if 'customdata' in item]


rounded_data_y = [[round(num, 1) for num in sublist] for sublist in y_values]
rounded_data_base = [[round(num, 1) for num in sublist] for sublist in base_values]
rounded_data_ave = [[[round(num[0], 1)] + num[1:] for num in sublist] for sublist in ave_values]


def generate_range_list(y_values, base_values):
    lst_range_min = []
    lst_range_max = []

    for i in range(len(base_values)):
        range_min = base_values[i]
        lst_range_min.append(range_min)
        range_max = base_values[i] + y_values[i]
        lst_range_max.append(range_max)
    
    lst_range = []
    for i in range(len(lst_range_min)):
        range_item = [lst_range_min[i], lst_range_max[i]]
        lst_range.append(range_item)
    
    return lst_range

rh_range = generate_range_list(rounded_data_y[1], rounded_data_base[1])
rh_band = generate_range_list(rounded_data_y[0], rounded_data_base[0])

rh_ave = rounded_data_ave[0]

data_with_description = {
    "humidity comfort band(%) from the first date to the last date of the year": rh_band,
    "Relative humidity Range(%) from the first date to the last date of the year": rh_range,
    "Average Relative humidity from the first date to the last date of the year": rh_ave
}

json_data = json.dumps(data_with_description, indent=4)

url = "https://api.zerowidth.ai/beta/process/XmZlDB2W1HFIzS7fmawI/cVpYPLjRmxtZoHbHp24H"
headers = {
    "Authorization": "Bearer sk0w-e1b943077ab9f86493693118eca0dfeb", 
    "Content-Type": "application/json"
}

data = {
    "data": {
        "variables": {
            "DATA": json_data,
        }
    }
}

response = requests.post(url, json=data, headers=headers)

print(response.json())

# python "/Users/akacoral/Documents/GitHub/API-test-clima/api test/rh_data_test.py"