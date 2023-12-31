import requests
import json, os
from pathlib import Path

api_url = "http://ordr.jspearlab.com/api/records/"


def get_all_records():
    # record = {"NumPalets": 4.0,  "NumItems": 250, "categories":'41-2, 421-1.1', "StoreNum": 20, "Lane": 10 }
    for file in os.listdir():
        if 'json' in file:
            with open(file) as order:
                record = json.load(order)
                header = {"Content-Type":"application/json"}
                response = requests.post(api_url, data=json.dumps(record), headers=header)

                print (response.status_code)
                return response.json()
            
def get_records():
    pass

def update_record(id):
    pass

