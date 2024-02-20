# DataComms

This repo provides python scripts for message passing via local files and local networks.

Inter Process Communicaiton (IPC) as defined [here](https://www.geeksforgeeks.org/inter-process-communication-ipc/):
* message passing via:
    * local file: [json](#json-comms), [hdf5](#hdf5-comms)
    * local network: [IP Websocket](#ip-websocket-comms)
* shared memory via:
    * local memory: [IPC through shared memory](https://www.geeksforgeeks.org/ipc-shared-memory/)

## HDF5 Comms
TODO

provide example

## JSON Comms
Writing to and reading from a .json file using write.json and read.json respectively, we observe the following performance for one small test.

![alt text](figs/json/send300_rec1000.png)

TODO
TODO - further discuss meanings of plot

## IP Websocket Comms
TODO - make the example plot results from the client side similar to json

If you'd like to communicate between machiens using a shared network (e.g. over wifi) you can use Python's "socket" library to get the job done.

### Running IP Websocket Comms
Information can be sent from machine A using ip_client.py to machine B using ip_server.py assuming the following conditions are met:
* both machines are connected to the same network
* the user specifies (a) the IP addresss and (b) port that machine B is reading from as the MACHINE_B_IP_ADDRESS and MACHINE_B_PORT vairables in ip_client.py
* ip_server.py is started first on machine B

### Tinkering Observations

An issue we've observed is that sock.connect is not always consistent in it's connection rate.

![alt text](figs/ip/listen1_1.png)
![alt text](figs/ip/listen1_2.png)
![alt text](figs/ip/listen1_3.png)

This can be an issue if we need a minimum update rate for a long period of time and suggests that an unreliable 

By increasing the client's sock.listen() rate from 1 to 5, we sometimes observe less frequent "drops" in message rates, however as observed in the previous plot, this is not always the case and results are hard to reproduce.

![alt text](figs/ip/listen5_1.png)
![alt text](figs/ip/listen5_2.png)
![alt text](figs/ip/listen5_3.png)

(2/18/24)
Testing Host to Host, we find better drop performance however performance is still inconsistent and was observed to drop below 30Hz (not shown in image).

![alt text](figs/ip/listen1_1_local.png)
![alt text](figs/ip/listen1_2_local.png)


## IPC throgh shared memory



