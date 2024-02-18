# import ujson as json
import json
import numpy as np
import time
import matplotlib.pyplot as plt
import requests
import os

# requires 
set_speed_hz = 100
num_messages = int(1e2)

speeds = np.zeros(int(num_messages))
times = np.zeros(int(num_messages))         # host time when message was recorded
timestamps = np.zeros(int(num_messages))    # gest time when message was sent
missed = np.zeros(int(num_messages))
longest_delay = 0.0


tstart = time.time()
for i in range(num_messages):
    print(i)
    t0 = time.time() - tstart
    time.sleep(1/set_speed_hz)
    
    try:
        with open('selected_json_file.json','r') as json_file:
            
            data = json.loads(json_file.read())
            times[i] = time.time() - tstart
            speeds[i] = int(1/(times[i]-t0))
            timestamps[i] = data["timestamp"]
    except Exception as error:
        
        times[i] = time.time() - tstart
        speeds[i] = int(1/(times[i]-t0))
        timestamps[i] = 0
        missed[i] = 1
        print(f"An exception has occured: {error}")
    
    if times[i]-t0 > longest_delay: longest_delay = times[i]-t0
            
    
plt.figure()
plt.plot(times,speeds)
for i in range(num_messages):
    if(missed[i] == 1):
        color = 'r'
    else:
        color = 'b'
    plt.scatter(times[i],speeds[i],color=color)

plt.title(f"Python JSON  Connection Test Sending {int(num_messages)} Messages \n \
           of dict(timestamp,8 joints) from VM to Host Machine \n \
            Longest Delay: {round(longest_delay,3)} s")
plt.xlabel('time [s]')
plt.ylabel('message speed [Hz]')
plt.show()
