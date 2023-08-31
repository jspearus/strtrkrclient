import json
import os
import datetime as dt

def json_store(pal, case, alsle, store, slot):
    file_time = dt.datetime.now()
    date = file_time.strftime("%m:%d:%Y:%H:%M")
    with open(f'order_{date}.json', 'w', encoding='utf-8') as f:
        data = {"created": date, 
                "numPalets": pal, "numItems": case, 
                           "categories": alsle, "storeNum": store, "lane": slot}
        json.dump(data, f, ensure_ascii=False, indent=4)
        
#  test
json_store(12, 350, 41, 52, 10)