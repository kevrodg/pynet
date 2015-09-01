#!/usr/bin/env python

from snmp_helper import snmp_get_oid,snmp_extract

IP = '50.76.53.27'
COMMUNITY_STRING = 'galileo'
SNMP_PORT_1 = 7961
SNMP_PORT_2 = 8061


rtr_1 = (IP, COMMUNITY_STRING, SNMP_PORT_1)
rtr_2 = (IP, COMMUNITY_STRING, SNMP_PORT_2)


sysDescr = '1.3.6.1.2.1.1.1.0'
sysName = '1.3.6.1.2.1.1.5.0'

for device in (rtr_1, rtr_2):
    for the_oid in (sysDescr, sysName):
        snmp_data = snmp_get_oid(device, oid=the_oid)
        output = snmp_extract(snmp_data)

        print output



