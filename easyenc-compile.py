#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
#
# Author      : Mikael Löfstrand
# Home page   : https://github.com/mld/easyenc/

import os
import yaml
import sys

def main():
  if len(sys.argv) > 1:
    dbdir  = sys.argv[1]
  else:
    sys.stderr.write("Error - need to supply dbdir!!\n  {0} <dbdir>\n".format(sys.argv[0]))
    sys.stderr.flush()
    sys.exit(1)

  doc = {}

  fd = os.listdir(dbdir)
  if 'default.yaml' in fd:
    doc['default'] = {}
    dbfile = dbdir + '/' + 'default.yaml'
    with open(dbfile, 'r') as db:
      ydoc = yaml.load(db)
    db.closed
    if 'environment' in ydoc:
      doc['default']['environment'] = ydoc["environment"]
    if 'class' in ydoc:
      doc = doc + "class: " + ydoc["class"] + "\n"
      doc['default']['class'] = ydoc["class"]

  classes = False
  for filename in fd:
    if filename.endswith(".yaml") and filename != 'default.yaml':
      environment = os.path.splitext(filename)[0]
      dbfile = dbdir + '/' + filename
      with open(dbfile, 'r') as db:
        ydoc = yaml.load(db)
      db.closed

      for host in ydoc:
        classes = ydoc[host]
        doc[host] = {'environment': environment, 'class': classes}
        
  print yaml.dump(doc, explicit_start=True,default_flow_style=False)

if __name__ == '__main__':
  main()
