#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
#
# Author      : Mikael Löfstrand
# Home page   : https://github.com/mld/easyenc/
# Inspired by : Basil Kurian <basilkurian[at]gmail[dot]com>
#               http://wiki.unixh4cks.com/index.php/Simple_External_Node_Classifier(ENC)_for_puppet_in_python

import yaml
import sys

def main():
  if len(sys.argv) > 2:
    dbfile  = sys.argv[1]
    host = sys.argv[2]
  elif len(sys.argv) > 1:
    dbfile = "./db.yaml"
    host = sys.argv[1]
  else:
    sys.stderr.write("Error - need to at least supply hostname!\n  {0} [<dbfile>] <fqdn>\n".format(sys.argv[0]))
    sys.stderr.flush()
    sys.exit(1)

  db = open(dbfile, "r")
  doc = yaml.load(db)
  
  environment = False
  classes = False
  parameters = False
  
  if 'default' in doc:
    if 'environment' in doc["default"]:
      environment = doc["default"]["environment"]
    if 'class' in doc["default"]:
      classes = doc["default"]["class"]
    if 'parameters' in doc["default"]:
      parameters = doc["default"]["parameters"]
  
  if host in doc:
    if 'class' in doc[host]:
      classes = doc[host]["class"]
    if 'environment' in doc[host]:
      environment = doc[host]["environment"]
    if 'parameters' in doc[host]:
      parameters = doc[host]["parameters"]
  
  new_yaml = {}
  if classes:
    new_yaml['classes'] = classes
  if environment:
    new_yaml['environment'] = environment
  if parameters:
    new_yaml['parameters'] = parameters
  
  print yaml.dump(new_yaml, explicit_start=True,default_flow_style=False)

if __name__ == '__main__':
  main()
