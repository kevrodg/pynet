#!/usr/bin/env python

import json
import yaml

from pprint import pprint

with open("my_file.json") as f:
    json_file = json.load(f)


with open("my_file.yaml") as f:
    yaml_file = yaml.load(f)


pprint (json_file)
pprint (yaml_file)
