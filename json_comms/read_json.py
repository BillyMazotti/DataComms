# import ujson as json
import json
import numpy as np
import time
import matplotlib.pyplot as plt
from tqdm import tqdm


# requires 
set_speed_hz = 1000
num_messages = 1e3

speeds = np.zeros(int(num_messages))
times = np.zeros(int(num_messages))         # host time when message was recorded
timestamps = np.zeros(int(num_messages))    # gest time when message was sent
missed = np.zeros(int(num_messages))

tstart = time.time()
print("\nRecieving Messages...")
for i in tqdm(range(int(num_messages))):
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
        timestamps[i] = 0.0
        missed[i] = 1
        # print(f"An exception has occured: {error}")

plt.figure()
plt.plot(times,speeds)

# plot missed and not missed 
times_missed = times[missed == 1]
times_not_missed = times[missed == 0]
speeds_missed = speeds[missed == 1]
speeds_not_missed = speeds[missed == 0]
plt.scatter(times_missed,speeds_missed,color='r')
plt.scatter(times_not_missed,speeds_not_missed,color='b')

# determine longest dealy
print("\nCalculating Longest Delay...")
longest_delay = 0.0
for i in tqdm(range(int(num_messages)-1)):
    # find the closest oldest back non-zero timestamp
    # if closest oldest timestap esits then don't consider for longest delay
    before_delay_timestamp = -1.0
    after_delay_timestamp = -1.0
    if timestamps[i] == 0.0:
        j = i
        while j > 0:
            j -= 1
            if timestamps[j] != 0.0:
                before_delay_timestamp = timestamps[j]
                break
    else:
        before_delay_timestamp = timestamps[i]
    if timestamps[i+1] == 0.0:
        k = i
        while k < num_messages-2:
            k += 1
            if timestamps[k] != 0.0:
                after_delay_timestamp = timestamps[k]
                break
    else:
        after_delay_timestamp = timestamps[i+1]
    if before_delay_timestamp != -1.0 and after_delay_timestamp != -1.0:
        delay = after_delay_timestamp - before_delay_timestamp
        if delay > longest_delay: longest_delay = delay

plt.title(f"Python JSON  Connection Test Sending {int(num_messages)} Messages \n \
           of dict(timestamp,8 joints) from VM to Host Machine \n \
            Longest Delay: {round(longest_delay,3)}s | Min Hz: {round(1/longest_delay)} | Dropout: {round(100*missed.sum()/num_messages,1)}%")
plt.xlabel('time [s]')
plt.ylabel('message speed [Hz]')
plt.show()
