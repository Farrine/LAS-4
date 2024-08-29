#!/usr/bin/env python3

import nmap
import os

os.system("cls")

scanner = nmap.PortScanner()

#Basic Interface
print("============================================================\n")
print("================== WELCOME TO SIMPLE NMAP ==================\n")
print("============================================================\n")

respon = input(""" Please enter the type of scan you want to run
               1. TCP SYN Scan
               2. TCP Connect Scan
               3. UDP Scan
Input the number you want to choose: """)

#---------------------------------
if respon == '1':
    os.system("cls")
    ip_add = input("Please, enter the IP Address you want to scan:")

#process
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_add, '1-1000', '-v -sS')
    print(scanner.scaninfo())
    print("IP Status: ", scanner[ip_add].state())
    print(scanner[ip_add].all_protocols)
    print("Open Ports: ", scanner[ip_add]['tcp'].keys())

#---------------------------------
elif respon == '2':
    os.system("cls")
    ip_add = input("Please, enter the IP Address you want to scan:")

#process
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_add, '1-1000', '-v -sT')
    print(scanner.scaninfo())
    print("IP Status: ", scanner[ip_add].state())
    print(scanner[ip_add].all_protocols)
    print("Open Ports: ", scanner[ip_add]['tcp'].keys())

#---------------------------------
elif respon == '3':
    os.system("cls")
    ip_add = input("Please, enter the IP Address you want to scan:")

#process
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_add, '1-1000', '-v -sU')
    print(scanner.scaninfo())
    print("IP Status: ", scanner[ip_add].state())
    print(scanner[ip_add].all_protocols)
    print("Open Ports: ", scanner[ip_add]['udp'].keys())

#---------------------------------
elif respon >= '4':
    print("Please, enter a valid option")