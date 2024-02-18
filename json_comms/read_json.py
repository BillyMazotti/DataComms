# import ujson as json
import json
import numpy as np
import time
import matplotlib.pyplot as plt

# requires 
set_speed_hz = 50
num_messages = int(1e3)

speeds = np.zeros(int(num_messages))
times = np.zeros(int(num_messages))         # host time when message was recorded
timestamps = np.zeros(int(num_messages))    # gest time when message was sent

missed = 0
for i in range(num_messages):
    t0 = time.time()
    times[i] = t0
    time.sleep(0.008)
    print(i)
    try:
        with open('test_connection.json') as json_file:
            data = json.load(json_file)
            timestamps[i] = data["timestamp"]
            print(timestamps[i])
    except Exception as error:
        timestamps[i] = 0
        missed += 1
        print(f"An exception has occured: {error}")
        
    print(f"Update Frequency {int(1/(time.time()-t0))} hz")
        
    
plt.figure()
plt.plot(times,speeds)
plt.scatter(times,speeds)
plt.title(f"Python IP Socket Connection Test Sending {int(n)} Messages \n \
           of np.ones((8))from VM to Host Machine \n \
          Longest Delay: {round(longest_delay,3)} s or {round(1/longest_delay)} Hz")
plt.xlabel('time [s]')
plt.ylabel('message speed [Hz]')
plt.show()
