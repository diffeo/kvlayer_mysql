kvlayer_mysql
=============

MySQL backend for kvlayer database abstraction.

kvlayer picks this up through setuptools/distutils pkg_resources entry point discovery. When installed kvlayer can be configured for storage_type = 'mysql'.

mysql-connector-python is GPL, isolate it so that only GPL-averse users don't accidentally get it
