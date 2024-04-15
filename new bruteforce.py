import math
import time
N = int(input("enter the value of N: "))
M = int(input("enter number to be encrypted: "))
E = int(input("enter the value of the public key: "))

start_time = time.time()
cpu_time = time.process_time()
cipher = (M**E)%N
print("cipher: ", cipher)

d_values = []
for d in range(1, N):
    if pow(cipher, d)%N == M:
        d_values.append(d)

if d_values:
    print("d values : " ,d_values)
else:
    print("no solution")

execution_time = time.time() - start_time
exc_time = time.process_time - cpu_time
print("time executed in seconds: ",execution_time)
print("time executed by cpu in seconds: ",exc_time)





