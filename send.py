import os
import time

times = dict()

#Send the message with given delay 5 times and average the timing
def send(delay=1000):
    t = 0
    for _ in range(5):
        t0 = time.time()
        os.system(f"sudo ./covert_tcp -source 192.168.0.111 -dest 192.168.0.151 -source_port 1234 -dest_port 80 -file message.txt -seq -d {delay}")
        t1 = time.time()
        t += t1 - t0

    times[delay] = t / 5

#Run the tests
for d in list(range(100000,0,-10000)) + list(range(10000,0,-1000)) + list(range(1000,0,-100)):
    send(d)

#Record results
with open("results.csv","w") as f:
    for d,t in times.items():
        f.write(f"{d},{t}\n")