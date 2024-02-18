import h5py
import time
import matplotlib.pyplot as plt
import numpy as np

n = int(1e3)
rec = np.zeros((n,))
time_rec = np.zeros((n,))
missed = 0

for i in range(n):
    t0 = time.time()
    time_rec[i] = t0
    time.sleep(0.008)
    print(i)
    try:
        h5f = h5py.File('test_connection.h5','r')
        b = h5f['joints_dataset'][:]
        rec[i] = b[0]
        print(rec[i])
    except:
        missed+=1
        rec[i] = 0
    print(f"Update Frequency {int(1/(time.time()-t0))} hz")

print()        
print(100*missed/n)

time_rec = time_rec - time_rec[0]
rec = rec.max() - rec

plt.figure()
plt.scatter(time_rec,rec)
plt.plot(time_rec,rec)
plt.show()
