#!/usr/bin/env python

from ciscoconfparse import CiscoConfParse 

cisco_config = CiscoConfParse('cisco_ipsec.txt')

crypto = cisco_config.find_objects(r"^crypto map CRYPTO")

for map in crypto:
    print map.text
    for child in map.children:
        print child.text

