#!/usr/bin/env python

import json
import yaml


my_list = [0, 1, 2, 3, 'whatever', 'hello', {'attribs': [0, 1, 2, 3, 4], 'ip_addr': '10.10.10.239'}] 


with open("my_file.json", "w") as f:
    json.dump(my_list, f)

with open("my_file.yaml", "w") as f:
    f.write(yaml.dump(my_list, default_flow_style=False))
