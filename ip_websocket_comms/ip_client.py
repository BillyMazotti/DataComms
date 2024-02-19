import socket
import time
import matplotlib.pyplot as plt
import numpy as np
import pickle

set_speed_hz = 200
num_messages = 1e4
# IP_ADDRESS = '35.3.248.94'      #VM on MWireless
# IP_ADDRESS = '192.168.0.2'      #VM at home
IP_ADDRESS = 'localhost'        # local host   

speeds = np.zeros((int(num_messages))) # recorded message Hz
times = np.zeros((int(num_messages)))  # host time when message was recorded
longest_delay = 0.0
tstart = time.time()
for i in range(int(num_messages)):
    print(i)
    t0 = time.time() - tstart
    time.sleep(1/set_speed_hz)

    sock = socket.socket()
    data= np.ones((8))*i
    
    sock.connect((IP_ADDRESS,8000))  # the line that causes the delay

    times[i] = time.time() - tstart
    speeds[i] = int(1/(times[i]-t0))
    serialized_data = pickle.dumps(data, protocol=2)
    sock.sendall(serialized_data)
    sock.close()
    if times[i]-t0 > longest_delay: longest_delay = times[i]-t0
    

plt.figure()
plt.plot(times,speeds)
plt.scatter(times,speeds)
plt.title(f"Python IP Socket Connection Test Sending {int(num_messages)} Messages \n \
           of np.ones((8))from VM to Host Machine \n \
          Longest Delay: {round(longest_delay,3)} s or {round(1/longest_delay)} Hz")
plt.xlabel('time [s]')
plt.ylabel('message speed [Hz]')
plt.show()

