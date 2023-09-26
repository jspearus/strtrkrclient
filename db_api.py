import requests
import json, os
from pathlib import Path

time_api_url = "http://ordr.jspearlab.com/api/timestores/"
record_api_url = "http://ordr.jspearlab.com/api/records/"


def get_store_times():
    # record = {"NumPalets": 4.0,  "NumItems": 250, "categories":'41-2, 421-1.1', "StoreNum": 20, "Lane": 10 }
    header = {"Content-Type":"application/json"}
    response = requests.get(time_api_url, headers=header)

    print (response.status_code)
    print(response.json())
    with open("store_times.json", "w") as outfile:
        outfile.write(json.dumps(response.json(), indent=4))
    
def update_store_times(file):
    ...
    
#test function
get_store_times()