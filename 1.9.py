#!/usr/bin/env python

from ciscoconfparse import CiscoConfParse 

cisco_config = CiscoConfParse('cisco_ipsec.txt')

crypto = cisco_config.find_objects_w_child(parentspec=r"^crypto map CRYPTO", childspec=r"set pfs group2")

for pfs in crypto:
    print pfs.text
    for child in pfs.children:
        print child.text

