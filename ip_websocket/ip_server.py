from __future__ import print_function
import sys
import socket
import pickle


sock = socket.socket()
sock.bind((b'',8000))
sock.listen(1)

while True:
    c,a = sock.accept()
    data = b''
    while True:
        block = c.recv(4096)
        if not block: break
        data += block
    c.close()
    if sys.version_info.major < 3:
        unserialized_input = pickle.loads(data)
    else:
        unserialized_input = pickle.loads(data,encoding='bytes')
    print(unserialized_input)