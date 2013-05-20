#!/usr/bin/env python
# Author : Basil Kurian <basilkurian[at]gmail[dot]com>

import yaml
import sys

host=sys.argv[1]

db = open("db.yaml", "r")
doc = yaml.load(db)

#for k,v in doc.items():
#  print k, "->", v
#print "\n"

environment = False
classes = False

if doc["default"]:
  environment = doc["default"]["environment"]
  classes = doc["default"]["class"]

if host in doc:
  if "class" in doc[host]:
    classes = doc[host]["class"]
  if "environment" in doc[host]:
    environment = doc[host]["environment"]

#print host, ": ", environment, ", ", classes, ".\n"
#print "\n"

new_yaml={'classes':[classes],'environment':environment}

print yaml.dump(new_yaml, explicit_start=True,default_flow_style=False)

