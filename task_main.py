#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 14:32:41 2022

@author: ahmedseoudy
"""
import json
import address_parser as ap

def main():
    with open('test.txt') as f:
        test_address = f.read().splitlines()
        
    for i in range(len(test_address)):
        address = ap.parse_address(test_address[i])
        json_object = json.dumps(address, indent = 4,ensure_ascii=False) 
        print(json_object)
        with open('json_data.json', 'a') as outfile:
            outfile.write(json_object)

if __name__ == "__main__":
    main()

