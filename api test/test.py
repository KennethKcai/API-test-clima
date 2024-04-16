import requests
import pandas as pd
import json
import tiktoken


with open('/Users/akacoral/Documents/GitHub/API-test-clima/api test/data.json', 'r', encoding='utf-8') as file:
    json_data = json.load(file)

y_values = [item['y'] for item in json_data if 'y' in item]
base_values = [item['base'] for item in json_data if 'base' in item]

rounded_data_y = [[round(num, 1) for num in sublist] for sublist in y_values]
rounded_data_base = [[round(num, 1) for num in sublist] for sublist in base_values]

# print(rounded_data_y[0])
# print(rounded_data_base[0])

AD_80_y = rounded_data_y[0]
AD_80_base = rounded_data_base[0]

lst_range_80_min = []
lst_range_80_max = []

for i in range(len(AD_80_base)):
    range_80_min = AD_80_base[i]
    lst_range_80_min.append(range_80_min)
    range_80_max = AD_80_base[i] + AD_80_y[i]
    lst_range_80_max.append(range_80_max)

print(lst_range_80_min)
print(lst_range_80_max)

# url = "https://api.zerowidth.ai/beta/process/XmZlDB2W1HFIzS7fmawI/fI8ys5r4pBiTnLdlQJdS"
# headers = {
#     "Authorization": "Bearer sk0w-e1b943077ab9f86493693118eca0dfeb", 
#     "Content-Type": "application/json"
# }

# data = {
#     "data": {
#         "variables": {
#             "DATA": json_data
#         }
#     }
# }

# response = requests.post(url, json=data, headers=headers)

# print(response.json())

# python "/Users/akacoral/Documents/GitHub/API-test-clima/api test/test.py"

