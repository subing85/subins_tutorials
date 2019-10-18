path = '/mnt/bkp/MyScript_/examples/binary/test_shder'

import os

a = os.path.splitext(path)

print a[1]

types = {
    '.ma': 'mayaAscii',
    '.mb': 'mayaBinary'
    } 

print a[1] in types