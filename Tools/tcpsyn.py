#!/usr/bin/env python3

import nmap
import os

os.system("cls")

scanner = nmap.PortScanner()

ip_add = input("Please, enter the IP Address you want to scan:")
print("Nmap Version: ", scanner.nmap_version())
scanner.scan(ip_add, '1-1000', '-v -sS')
print(scanner.scaninfo())
print("IP Status: ", scanner[ip_add].state())
print(scanner[ip_add].all_protocols)
print("Open Ports: ", scanner[ip_add]['tcp'].keys())