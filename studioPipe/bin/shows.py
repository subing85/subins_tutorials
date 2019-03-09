#!/usr/bin/python
import optparse

from pprint import pprint

def create():
    parser = optparse.OptionParser(usage='usage: %prog [options] create your show',
                          version='Studio Pipe 0.0.1')
    option_list = [
        optparse.make_option('--na', '--name',
                    action='store', type='string', dest='show_name'),
        optparse.make_option('--dn', '--displayname',
                    action='store', type='string', dest='display_name'),
        optparse.make_option('--sn', '--shortname',
                    action='store', type='string', dest='short_name'),    
        optparse.make_option('--tp', '--tooltip',
                    action='store', type='string', dest='tooltip_name'),   
        optparse.make_option('--i', '--icon',
                    action='store', type='string', dest='icon_file')
        ]
    
    parser.add_options(option_list)

    parser.add_option('-q', '--query',
                      action='store_true',
                      dest='query',
                      default=False,
                      help='to query')
    parser.add_option('-s', '--shows',
                      action='store', # optional because action defaults to 'store'
                      dest='get the shows',
                      default='True',
                      help='find the exists shows',)
    
    (options, args) = parser.parse_args()
    
    
    if options.query:
        print 'yess'
        


    #if len(args) != 1:
    #    parser.error('wrong number of arguments')


if __name__ == '__main__':
    create() 
    
