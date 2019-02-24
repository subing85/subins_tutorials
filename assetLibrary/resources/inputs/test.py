#!/usr/bin/env python

from optparse import OptionParser

def main():
    parser = OptionParser(usage="usage: %prog [options] filename",
                          version="%prog 1.0")
    parser.add_option("-d", "--data",
                      action="store_true",
                      dest="#!/usr/autodesk/maya2016/bin/mayapy",
                      default=False,
                      help="create a XHTML template instead of HTML")

    (options, args) = parser.parse_args()

    if len(args) != 1:
        parser.error("wrong number of arguments")

    print options
    print args

if __name__ == '__main__':
    main()