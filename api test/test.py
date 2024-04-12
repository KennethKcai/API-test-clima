import requests
import pandas as pd
import json

file_path = '/Users/akacoral/Documents/GitHub/API-test-clima/api test/df_Red Bluff Muni AP_USA_Clima_SIunit.csv'
df = pd.read_csv(file_path, nrows=10)
data_list = df.to_dict(orient='records')
json_data = json.dumps(data_list)
# print(data_list)

url = "https://api.zerowidth.ai/beta/process/XmZlDB2W1HFIzS7fmawI/fI8ys5r4pBiTnLdlQJdS"
headers = {
    "Authorization": "Bearer sk0w-e1b943077ab9f86493693118eca0dfeb", 
    "Content-Type": "application/json"
}

data = {
    "data": {
        "variables": {
            "DATA": json_data
        }
    }
}

response = requests.post(url, json=data, headers=headers)

print(response.json())

# python "/Users/akacoral/Documents/GitHub/API-test-clima/api test/test.py"

