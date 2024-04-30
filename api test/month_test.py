import requests
import pandas as pd
import json



with open('/Users/akacoral/Documents/GitHub/API-test-clima/api test/rh_yearly_data.json', 'r', encoding='utf-8') as file:
    json_data = json.load(file)

y_values = [item['y'] for item in json_data if 'y' in item]
base_values = [item['base'] for item in json_data if 'base' in item]
ave_values = [item['customdata'] for item in json_data if 'customdata' in item]

print(y_values)

rounded_data_y = [[round(num, 1) for num in sublist] for sublist in y_values]
rounded_data_base = [[round(num, 1) for num in sublist] for sublist in base_values]
rounded_data_ave = [
    [round(num, 1) if isinstance(num, (int, float)) else num for num in sublist] 
    for sublist in ave_values
]


print(rounded_data_y[0])
print(rounded_data_base[0])
print(rounded_data_ave[0])

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

lst_range_80 = generate_range_list(rounded_data_y[0], rounded_data_base[0])
lst_range_90 = generate_range_list(rounded_data_y[1], rounded_data_base[1])

temp_data = rounded_data_y[3]
tem_range = rounded_data_y[2]

data_with_description = {
    "ASHRAE adaptive comfort (80%) for 80 percentile from the first date to the last date of the year": lst_range_80,
    "ASHRAE adaptive comfort (80%) for 90 percentile from the first date to the last date of the year": lst_range_90,
    "daily temperature average from the first date to the last date of the year": temp_data,
    "daily temperature range from the first date to the last date of the year": tem_range
}

# json_data = json.dumps(data_with_description, indent=4)

# url = "https://api.zerowidth.ai/beta/process/dUakZrqR6iPgiJXslVOE/keL4947TSV17cRgaA1KM"
# headers = {
#     "Authorization": "Bearer sk0w-d4b90953c5f969ae83fd15bbe10b3b53", 
#     "Content-Type": "application/json"
# }

# data = {
#     "data": {
#         "variables": {
#             "DATA": json_data,
#             "MONTH": "FEB"
#         }
#     }
# }

response = requests.post(url, json=data, headers=headers)

print(response.json())

# python "/Users/akacoral/Documents/GitHub/API-test-clima/api test/month_test.py"