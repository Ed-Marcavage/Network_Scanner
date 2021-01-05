# Network_Scanner
Command line tool developed in Python that creates, sends/receives, and stores data within the scope of ARP 

- Full credit to StationX for the [tutorial](https://courses.stationx.net/p/the-complete-python-for-hacking-and-cyber-security-bundle) that taught me this code 

## scapy 
- Use this module to create an ARP packet asking for the target IP adresses on the network (given by user input)
- Create and Ether packet to set the destination MAC address to the broadcast MAC address
- Use scapy to combine the two packets created above 
- Store response in a Python dict

## argparse
- Use this module to create a python object that creates a linux command and saves user input
- Create a help menu for confused users 
