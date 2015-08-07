#!/usr/bin/env python

from ciscoconfparse import CiscoConfParse 

cisco_config = CiscoConfParse('cisco_ipsec.txt')

crypto = cisco_config.find_objects_wo_child(parentspec=r"^crypto map CRYPTO", childspec=r"set transform-set AES")

for aes in crypto:
    print aes.text
    for child in aes.children:
        print child.text

