# -*- Python -*-
#
# Plugs into kvlayer/tests/test_interface.py

# For entry point 'kvlayer.test_config'.
# Return yaml blob to configure mysql driver.
def test_config():
    return '''#yaml text
kvlayer:
  storage_type: mysql
  storage_addresses: [localhost]
  user: test
  password: test

'''
