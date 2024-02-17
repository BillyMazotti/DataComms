# import ujson as json
import json
import numpy as np
import time
import matplotlib.pyplot as plt

n = int(1e3)
time_rec = np.zeros((n,))
rec = np.zeros((n,))
missed = 0

for i in range(n):
    t0 = time.time()
    time_rec[i] = t0
    time.sleep(0.008)
    print(i)
    try:
        with open('test_connection.json') as json_file:
            data = json.load(json_file)
            rec[i] = data["timestamp"]
            print(rec[i])
    except:
        rec[i] = 0
        missed += 1
    print(f"Update Frequency {int(1/(time.time()-t0))} hz")
        
    
print()
print(100*missed/n)
time_rec = time_rec - time_rec[0]
rec = rec.max() - rec

plt.figure()
plt.plot(time_rec,rec)
plt.scatter(time_rec,rec)
plt.show()
