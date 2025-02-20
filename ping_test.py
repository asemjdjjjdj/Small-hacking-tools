import os
import ipaddress

ip = '(first ip in network)'
ipd = ipaddress.IPv4Address(ip)
limit = ipaddress.IPv4Address("(largest value of ip in the network)")  

while ipd <= limit:
    pingip = str(ipd)  

    response = os.popen(f"ping -n 1 -w 100 {pingip}").read()

    if "Reply from" in response or "bytes=32" in response:  
        print(f"Ping successful: {pingip}")

    ipd += 1  
