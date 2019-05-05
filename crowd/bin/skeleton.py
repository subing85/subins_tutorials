#!/usr/bin/python
import optparse
from pprint import pprint
from crowd.api import skeleton


def crowd_skeleton():
    parser = optparse.OptionParser(
        usage='usage: %prog [options] create your show',
        version='Studio Pipe 0.0.1')
    option_list = [
        optparse.make_option(
            '--cr', '--create', action='store', type='string', dest='create'),
        ]
    parser.add_options(option_list)

    (options, args) = parser.parse_args()

    if options.create :
        '''
            :example skeleton -cr biped
        '''
        skeleton_object = skeleton.Skeleton()
        skeleton_object.create(options.create)


if __name__ == '__main__':
    crowd_skeleton()
