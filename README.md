easyenc
=======

A simple ENC and compiler for Puppet, fed by a yaml "database". Please keep in mind that this is still a work in progress.

Requires python and python-yaml packages in Ubuntu 12.04. YMMV.

easyenc.py
----------
A simple ENC (External Node Classifier) for Puppet, fed by a yaml "database".

In your puppet master configuration, enter something along the lines of this to use:
```
[master]
  node_terminus = exec
  external_nodes = /usr/local/bin/easyenc.py /var/lib/puppet/easyenc.yaml
```

/var/lib/puppet/easyenc.yaml:
```yaml
---
default:
  environment: unknown
  class: roles::unknown
test.example.com:
  environment: dev
  class: roles::dev::test
another.example.com:
  class: roles::some::role
```

easyenc-compiler.py
-------------------
Compilation of easyenc.yaml from a directory of yaml files. somename.yaml gives environment "somename" for all hosts listed in that file. default.yaml is special...

/etc/easyenc.d/default.yaml:
```yaml
---
environment: unknown
```
/etc/easyenc.d/prod.yaml:
```yaml
---
an.example.com: roles::some::role
another.example.com: roles::prod::web
```
