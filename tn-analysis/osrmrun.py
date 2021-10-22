import pandas as pd
import requests,json,os
import time
import numpy as np
import subprocess,sys
cells=pd.read_csv('/weights/valid_cells.csv')
cells['index']=cells.index
cells=cells.sort_values(by='index')
cells['cell_to']=cells.cell_id.apply(lambda x: "cell_id_"+str(x))
begin='http://127.0.0.1:5000/table/v1/driving/'
cells['combined']=cells.center_lng.apply(str)+','+cells.center_lat.apply(str)
sep=';'
url=begin+sep.join(cells['combined'].tolist()).strip(';')

hour=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,18,19,20,21,22,23]
day=['mon','tue','wed','thur','fri','sat','sun']
month=[1,2,3,4,5,6,7,8,9,10,11,12]

count=0
for m in month:
    for d in day:
        for h in hour:
            filename = f'/weights/segment_speed_data/segment_speed_data_{m}_{d}_{h}.csv'
            targetfile=f'/weights/segment_speed_data/traveltime_{m}_{d}_{h}.parquet'
            if os.path.exists(filename) and not os.path.exists(targetfile):
                os.system(f'osrm-customize /tn/tennessee-latest.osrm --segment-speed-file {filename}')
                proc=subprocess.Popen(["/usr/local/bin/osrm-routed", "--algorithm", "mld", "/tn/tennessee-latest.osrm"])
                time.sleep(1)
                r=requests.get(url)
                data2=r.json()
                durations=np.array(data2['durations'])
                df = pd.DataFrame(durations, columns = cells.cell_to)
                df['cell_from']=cells.cell_to
                df['month']=m
                df['day']=d
                df['hour']=h
                df=df.set_index(['month','day','hour','cell_from'])
                df.to_parquet(f'/weights/segment_speed_data/traveltime_{m}_{d}_{h}.parquet')
                proc.terminate()
                print(proc.poll())
                proc.wait()