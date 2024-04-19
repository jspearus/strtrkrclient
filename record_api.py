import requests
import json, os
from pathlib import Path

api_url = "http://ordr.jspearlab.com/api/orderrecord/"


def get_all_records():
    for file in os.listdir('records'):
        if '.json' in file:
            with open("records/" + file, 'r') as order:
                record = json.load(order)
                header = {"Content-Type":"application/json"}
                response = requests.post(api_url, data=json.dumps(record), headers=header)
                # print (response.status_code)
                os.remove("records/" + file)
                return response.json()
            
def get_records():
    pass

def update_record(id):
    pass

get_all_records()

