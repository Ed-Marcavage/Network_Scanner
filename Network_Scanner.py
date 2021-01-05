#!/usr/bin/env python

import scapy.all as scapy
import argparse

def get_arguments():
 parser = argparse.ArgumentParser() # Create parse object for command line tool
 parser.add_argument("-t", "--target", dest="ip", help="insert a Target IP range for network scan")
 options = parser.parse_args() # save user inputs
 if not options.ip: # check the user input a interface
 parser.error("[-] Please specify a target IP range, use --help for more info.")
 return options

def scan(ip):
 arp_request = scapy.ARP(pdst = ip) # ARP request asking for all IPs on NW
 broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff") # set desitination mac to broadcast mac, for ARP req ^
 arp_request_broadcast = broadcast/arp_request # scapy syntax to combine two ARP packet
 answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0] # send/receive packet created above ^


 clients_list = [] # create a list to store ip and mac in a dict
 for element in answered_list: # iter thru each ARP response and store in list
 client_dict = {"ip":element[1].psrc, "MAC":element[1].hwsrc} # create dict and index ARP response
 clients_list.append(client_dict) # append dict values to list
 return clients_list

def print_result(results_list):
 print("IP\t\t\tMAC Address\n----------------------------------------")
 for client in results_list: # iter thru list and print in readable format
 print(client["ip"] +"\t\t"+ client["MAC"])
options = get_arguments()
print_result(scan(options.ip))
