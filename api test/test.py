import requests
import pandas as pd
import json
import tiktoken


with open('/Users/akacoral/Documents/GitHub/API-test-clima/api test/data.json', 'r', encoding='utf-8') as file:
    json_data = json.load(file)

y_values = [item['y'] for item in json_data if 'y' in item]
rounded_data = [[round(num, 1) for num in sublist] for sublist in y_values]
print(rounded_data)

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

