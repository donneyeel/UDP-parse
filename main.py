import matplotlib.pyplot as plt
import csv

filename = "A-host.csv"

udp_tx = []
udp_rx = []
timestamps = []

with open(filename, "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        udp_tx.append(int(row["udp_tx"]))
        udp_rx.append(int(row["udp_rx"]))
        timestamps.append(int(row["time_stamp"]))

plt.figure(figsize=(10, 6))
plt.plot(timestamps, udp_tx, label="udp_tx (bytes)", marker='o')
plt.plot(timestamps, udp_rx, label="udp_rx (bytes)", marker='x')

plt.xlabel("Time (microseconds)")
plt.ylabel("Bytes")
plt.title("UDP Transmission and Reception Over Time")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
