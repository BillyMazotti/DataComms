import socket
import time
import matplotlib.pyplot as plt
import numpy as np
import pickle

set_speed_hz = 50

n = 1e4
max_hz_to_report = 100
speeds = np.zeros((int(n))) # recorded message Hz
times = np.zeros((int(n)))  # time at wich message was recorded
longest_delay = 0.0
tstart = time.time()
for i in range(int(n)):
    print(i)
    t0 = time.time() - tstart
    time.sleep(1/set_speed_hz)

    sock = socket.socket()
    data= np.ones((8))
    # sock.connect(('35.3.248.94',8000))  # the line that causes the delay
    sock.connect(('192.168.0.2',8000))
    times[i] = time.time() - tstart
    speeds[i] = int(1/(times[i]-t0))
    serialized_data = pickle.dumps(data, protocol=2)
    sock.sendall(serialized_data)
    sock.close()
    if times[i]-t0 > longest_delay: longest_delay = times[i]-t0
    

plt.figure()
plt.plot(times,speeds)
plt.scatter(times,speeds)
plt.title(f"Python IP Socket Connection Test Sending {int(n)} Messages \n \
           of np.ones((8))from VM to Host Machine \n \
          Longest Delay: {round(longest_delay,3)} s or {round(1/longest_delay)} Hz")
plt.xlabel('time [s]')
plt.ylabel('message speed [Hz]')
plt.show()

