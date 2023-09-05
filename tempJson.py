import json
import os
import datetime as dt

def record_order(pal, case, alsle, store, slot):
    file_time = dt.datetime.now()
    date = file_time.strftime("%m:%d:%Y:%H:%M")
    with open(f'order_{date}.json', 'w', encoding='utf-8') as f:
        data = {"created": date, 
                "numPalets": pal, "numItems": case, 
                           "categories": alsle, "storeNum": store, "lane": slot}
        json.dump(data, f, ensure_ascii=False, indent=4)
        
#  test
record_order(1.2, 160, 30, 52, 10)
record_order(1.9, 180, 30, 25, 20)
record_order(2.5, 350, 41, 40, 32)