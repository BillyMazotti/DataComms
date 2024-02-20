# import ujson as json
import json
import numpy as np
import time
import matplotlib.pyplot as plt
from tqdm import tqdm
from write_json import set_message_send_rate


# requires 
send_message_rate = set_message_send_rate()     # Hz
recieve_message_rate = 800                     # Hz
num_messages_to_recieve = 1e4                   # number of messages

speeds = np.zeros(int(num_messages_to_recieve))
times = np.zeros(int(num_messages_to_recieve))          # time when message was read
timestamps = np.zeros(int(num_messages_to_recieve))     # time when message was sent
missed = np.zeros(int(num_messages_to_recieve))

tstart = time.time()
print("\nRecieving Messages...")
for i in tqdm(range(int(num_messages_to_recieve))):
    t0 = time.time() - tstart
    time.sleep(1/recieve_message_rate)
    
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

# determine longest dealy
print("\nCalculating Longest Delay...")
longest_delay_for_message_read = 1/speeds.min()

longest_delay_for_new_messaged_read = 0.0
for i in tqdm(range(int(num_messages_to_recieve)-1)):
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
        while k < num_messages_to_recieve-2:
            k += 1
            if timestamps[k] != 0.0:
                after_delay_timestamp = timestamps[k]
                break
    else:
        after_delay_timestamp = timestamps[i+1]
    if before_delay_timestamp != -1.0 and after_delay_timestamp != -1.0:
        delay = after_delay_timestamp - before_delay_timestamp
        if delay > longest_delay_for_new_messaged_read: longest_delay_for_new_messaged_read = delay
if (longest_delay_for_new_messaged_read == 0.0): longest_delay_for_message_read = 1e-12

times_missed = times[missed == 1]
times_not_missed = times[missed == 0]
speeds_missed = speeds[missed == 1]
speeds_not_missed = speeds[missed == 0]

plt.figure(figsize=(6,7))

#plot lines in the background
plt.plot(times,speeds,zorder=-1)   

# plot missed and not missed messages as points in the foreground
missed_pnts = plt.scatter(times_missed,speeds_missed,color='r')
not_missed_pnts = plt.scatter(times_not_missed,speeds_not_missed,color='b')

title_line_1 = f"Python JSON Comms Test | Msg Type = {type(data)}"
title_line_2 = f"{int(num_messages_to_recieve)} Msgs Sent at {send_message_rate}\
Hz and Received at {recieve_message_rate}Hz"
title_line_3 = f"Slowest Read Message Speed: {round(1/longest_delay_for_message_read)}Hz"
title_line_4 = f"Slowest New Message Speed: {round(1/longest_delay_for_new_messaged_read)}Hz: \
| Dropout: {round(100*missed.sum()/num_messages_to_recieve,1)}%"

plt.title(f"{title_line_1} \
          \n{title_line_2} \
          \n{title_line_3} \
          \n{title_line_4}")
plt.xlabel('read message time [s]')
plt.ylabel('read message speed [Hz]')
plt.legend([missed_pnts,not_missed_pnts],['missed','accepted'])
plt.show()
