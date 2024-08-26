#!/usr/bin/env python3

import whois

def whois(dm):
    dm_info = whois.whois(dm)
    output(dm)
    
def output(dm):
    try: 
        print("Registar:", dm_info.registar)
        print("Creation Date:", dm_info.creation_date)
        print("Expired Date:", dm_info.expired_date)
        print("Country:", dm_info.country)
    except:
        print("Something went wrong")

#Input
dm = input("Masukkan nama domain:")
whois(dm)