#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 11:51:03 2022

@author: ahmedseoudy
"""
import re
def parse_address(address):
    
    address_dict = {"street":"","housenumber":""}  
    #Street name then housenumber as numbers only or numbers and single char 
    if bool(re.fullmatch("\s*([a-zA-ZäöüÄÖÜß-]+[\.]?[\s]*)+([\d]*[\s]*,)?[\s]*[0-9]+([/|-]\s*([0-9]*)?)?\s*[a-zA-ZäöüÄÖÜß]*\s*",address)): 
        addresses = address.strip()
        if "," in address:
            list_addresses = addresses.split(",")
            address_dict["street"] = list_addresses[0].strip()
            address_dict["housenumber"] = list_addresses[1].strip()
        # if house number has a space in it (e.g.Nordstrasse 22 A) 
        elif bool(re.search("[0-9]+\s+[a-zA-ZäöüÄÖÜß]?\s*",address)):
            list_addresses = addresses.rsplit(' ', 2)
            address_dict["street"] = list_addresses[0]
            address_dict["housenumber"] = " ".join(list_addresses[1:])
        else:
            list_addresses = addresses.rsplit(' ', 1)
            address_dict["street"] = list_addresses[0].strip()
            address_dict["housenumber"] = list_addresses[1].strip()
        
        # housenumber as numbers only or numbers and single char  space then street name
    elif bool(re.fullmatch("\s*[0-9]+[/|-]?([-][0-9]*)?[\s]*[a-zA-ZäöüÄÖÜß]?\s*,?\s*([a-zA-ZäöüÄÖÜß-]+[\d]*[\.]?\s*)+[\d]*",address)):
        addresses = address.strip()
        if "," in address:
            list_addresses = addresses.split(",")
            address_dict["street"] = list_addresses[1].strip()
            address_dict["housenumber"] = list_addresses[0].strip()
        else:    
            list_addresses = addresses.split(" ",1)
            address_dict["street"] = list_addresses[1].strip()
            address_dict["housenumber"] = list_addresses[0].strip()
            
            # Street name (sing or multiple words) and containing digits then house digits only or alphanumeric containg No./N.
    elif bool(re.fullmatch("(?i)\s*[0-9]*([-][0-9]*)?\s*([a-zA-ZäöüÄÖÜß]+[-]?\s*)+[\.]?[\s]?[0-9]*\s*(NO((\.[\s]?)|[\s]+)|N[\.][\s]?)[0-9]*[/|-]?([-][0-9]*)?[\s\D]*\s*",address)):
        addresses = address.strip()
        #search for the starting index of the word No., No 
        if bool(re.search("(?i) No((\.[\s]?)|[\s]+)", addresses)):
            split_index = re.search("(?i) No((\.[\s]?)|[\s]+)", addresses).start()
         #search for the starting index of the word N.
        else:
            split_index = re.search("(?i)N[\.]", addresses).start()
        address_dict["street"] = addresses[0:split_index].strip()
        address_dict["housenumber"] = addresses[split_index:].strip()
        
        #Street name only
    elif not bool(re.search(r'\d', address)):
        address_dict["street"] = address.strip()
        address_dict["housenumber"] = None
            
    return address_dict        







            
      
      