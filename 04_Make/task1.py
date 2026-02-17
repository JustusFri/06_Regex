import re

# Read the data
ipAddresses = []
fileHandler = open('04_Make/ipAddresses.txt', 'r')
for ip in fileHandler:
    ipAddresses.append(ip)
fileHandler.close()

# Your code starts here

import re

# Muster für eine Zahl von 0-255
z = r"(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])"
ipv4_regex = re.compile(r"^(" + z + r"\.){3}" + z + r"$")

# Muster für IPv6 (8 Blöcke zu je 1-4 Hex-Stellen)
ipv6_regex = re.compile(r"^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$")

ipAddresses = [
    "192.168.1.1", "256.256.256.256", "2001:0db8:0000:0000:0000:ff00:0042:8329",
    "127.0.0.1", "::1", "not.an.ip.address"
]

ipv4_count = 0
ipv6_count = 0

for ip in ipAddresses:
    if ipv4_regex.match(ip):
        ipv4_count += 1
        print(f"{ip} is IPv4")
    elif ipv6_regex.match(ip):
        ipv6_count += 1
        print(f"{ip} is IPv6")
    else:
        print(f"{ip} is Neither")

print(f"\nErgebnis: {ipv4_count}x IPv4, {ipv6_count}x IPv6")