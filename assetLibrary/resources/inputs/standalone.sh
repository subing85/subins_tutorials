#!/usr/bin/env python

import os
import optparse

if __name__ == '__main__':
    #    ss !/usr/bin/env python
    parser = optparse.OptionParser()
    parser.add_option('-t', '--type',
            help='execute maya functions')

    options, args = parser.parse_args()

    if options.type=='asset_library':
        
        '''
        from api import tt
        cmd = ''
        os.system(cmd)
        '''
        
        from maya import standalone
        standalone.initialize(name='python')
        
        print help(standalone)
        