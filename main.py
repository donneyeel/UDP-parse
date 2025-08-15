import matplotlib.pyplot as plt
import csv
import numpy as np
np.set_printoptions(suppress=True)

filename1 = "A-host.csv"
filename2 = "A-host_transactions.bin"

udp_tx = []
udp_rx = []
timestamps = []

binary_timesamps = np.fromfile(filename2, dtype=np.uint32) / 1_000_000
binary_indices = np.arange(1, len(binary_timesamps)+1)
transactions_per_second = binary_indices / binary_timesamps

print("Transactions per second:", transactions_per_second)

with open(filename1, "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        udp_tx.append(int(row["udp_tx"]))
        udp_rx.append(int(row["udp_rx"]))
        timestamps.append(int(row["time_stamp"]) / 1_000_000)
        
fig, ax1 = plt.subplots(figsize=(10, 6))

ax1.plot(timestamps, udp_tx, label="udp_tx (bytes)", marker='o', color='b')
ax1.plot(timestamps, udp_rx, label="udp_rx (bytes)", marker='x', color='g')
ax1.set_xlabel("Time (seconds)")
ax1.set_ylabel("Bytes")
ax1.legend(loc="upper left")
ax1.grid(True)

ax2 = ax1.twinx()
ax2.plot(binary_timesamps, transactions_per_second, label="Transactions per Second", marker='x', color='r')
ax2.set_ylabel("TPS")
ax2.legend(loc="upper right")

plt.title("UDP Transmission, Reception, and Transactions per Second")
plt.show()
