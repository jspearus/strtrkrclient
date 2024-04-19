import json
import os, time
import datetime as dt
from datetime import timedelta

def create_order(pal, case, alsle, store, slot):
    file_time = dt.datetime.now()
    due_time = file_time.replace(hour=11, minute=0, second=0)
    fname = file_time.strftime("%m:%d:%Y:%H:%M")
    start = file_time.strftime("%Y-%m-%d %H:%M")
    due = due_time.strftime("%Y-%m-%d %H:%M")
    with open(f'records/order_{fname}.json', 'w', encoding='utf-8') as f:
        data = {"time_started": start, 
                "palets": pal, "number_of_cases": case, 
                           "aile_numbers": alsle, "store_number": store, "lane_number": slot,
                           "time_due": due,
                           "finished": "TBD"}
        json.dump(data, f, ensure_ascii=False, indent=4)
        
# todo needs to be updated - copy of creaet order
def update_order(pal, case, alsle, store, slot):
    file_time = dt.datetime.now()
    date = file_time.strftime("%m:%d:%Y:%H:%M")
    due_time = file_time.replace(hour=11, minute=0, second=0)
    due = due_time.strftime("%m:%d:%Y:%H:%M")
    with open(f'records/order_{date}.json', 'w', encoding='utf-8') as f:
        data = {"time_started": date, 
                "numPalets": pal, "number_of_cases": case, 
                           "aile_numbers": alsle, "store_number": store, "lane_number": slot,
                           "time_due": due,
                           "finished": "TBD"}
        json.dump(data, f, ensure_ascii=False, indent=4)
        
def finish_order(name):
    pass
        
#  test
# create_order(1.2, 160, 30, 52, 10)
